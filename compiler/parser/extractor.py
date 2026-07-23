from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from tree_sitter import Node

from compiler.document.document import Document
from compiler.parser.walker import ASTWalker
from compiler.uast.language.models import (
    Location,
    Symbol,
    SymbolKind,
)


@dataclass(slots=True)
class ScopeContext:
    name: str
    kind: SymbolKind


class SymbolExtractor:
    """
    Extracts semantic symbols from a Tree-sitter AST.
    """

    def __init__(self):
        self.walker = ASTWalker()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def extract(
        self,
        document: Document,
    ) -> list[Symbol]:

        tree = document.tree
        file = document.path

        symbols: list[Symbol] = []
        scope_stack: list[ScopeContext] = []

        for ctx in self.walker.walk_context(tree.root_node):

            #
            # Leave scopes we've exited.
            #
            while len(scope_stack) > ctx.depth:
                scope_stack.pop()

            node = ctx.node

            symbol = self._extract_symbol(
                node,
                file,
                scope_stack,
            )

            if symbol is None:
                continue

            symbols.append(symbol)

            #
            # Parameters belong to functions/methods.
            #
            if symbol.kind in (
                SymbolKind.FUNCTION,
                SymbolKind.METHOD,
            ):
                symbols.extend(
                    self._extract_parameters(
                        node,
                        file,
                        symbol.name,
                    )
                )

            #
            # Push new scope.
            #
            if symbol.kind in (
                SymbolKind.CLASS,
                SymbolKind.FUNCTION,
                SymbolKind.METHOD,
            ):
                scope_stack.append(
                    ScopeContext(
                        name=symbol.name,
                        kind=symbol.kind,
                    )
                )

        return symbols

    # ---------------------------------------------------------
    # Symbol Recognition
    # ---------------------------------------------------------

    def _extract_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol | None:

        node_type = node.type

        if node_type == "class_definition":
            return self._class_symbol(
                node,
                file,
                scope_stack,
            )

        if node_type == "function_definition":
            return self._function_symbol(
                node,
                file,
                scope_stack,
            )

        if node_type in ("import_statement", "import_from_statement"):
            return self._import_symbol(
                node,
                file,
                scope_stack,
            )

        attribute = self._attribute_symbol(
            node,
            file,
            scope_stack,
        )
        if attribute:
            return attribute

        variable = self._variable_symbol(
            node,
            file,
            scope_stack,
        )
        if variable:
            return variable

        return None

    def _extract_parameters(
        self,
        node: Node,
        file: Path,
        parent_name: str,
    ) -> list[Symbol]:

        parameters: list[Symbol] = []
        params = node.child_by_field_name("parameters")

        if params is None:
            return parameters

        for child in params.children:
            if child.type != "identifier":
                continue

            parameters.append(
                Symbol(
                    name=child.text.decode(),
                    kind=SymbolKind.PARAMETER,
                    location=Location(
                        file=file,
                        line=child.start_point[0] + 1,
                        column=child.start_point[1] + 1,
                    ),
                    parent=parent_name,
                )
            )

        return parameters

    def _variable_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol | None:

        if node.type != "assignment":
            return None

        left = node.child_by_field_name("left")

        if left is None or left.type != "identifier":
            return None

        var_name = left.text.decode()
        kind = (
            SymbolKind.CONSTANT
            if var_name.isupper()
            else SymbolKind.VARIABLE
        )

        return Symbol(
            name=var_name,
            kind=kind,
            location=Location(
                file=file,
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            parent=scope_stack[-1].name if scope_stack else None,
        )

    def _attribute_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol | None:

        if node.type != "assignment":
            return None

        left = node.child_by_field_name("left")

        if left is None or left.type != "attribute":
            return None

        name_node = left.child_by_field_name("attribute")

        if name_node is None:
            return None

        return Symbol(
            name=name_node.text.decode(),
            kind=SymbolKind.ATTRIBUTE,
            location=Location(
                file=file,
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            parent=scope_stack[-1].name if scope_stack else None,
        )

    # ---------------------------------------------------------
    # Builders
    # ---------------------------------------------------------

    def _class_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol:

        name_node = node.child_by_field_name("name")

        return Symbol(
            name=name_node.text.decode() if name_node else "UnnamedClass",
            kind=SymbolKind.CLASS,
            location=Location(
                file=file,
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            parent=scope_stack[-1].name if scope_stack else None,
        )

    def _function_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol:

        name_node = node.child_by_field_name("name")

        kind = (
            SymbolKind.METHOD
            if (scope_stack and scope_stack[-1].kind == SymbolKind.CLASS)
            else SymbolKind.FUNCTION
        )

        return Symbol(
            name=name_node.text.decode() if name_node else "UnnamedFunction",
            kind=kind,
            location=Location(
                file=file,
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            parent=scope_stack[-1].name if scope_stack else None,
            is_async=False,
        )

    def _import_symbol(
        self,
        node: Node,
        file: Path,
        scope_stack: list[ScopeContext],
    ) -> Symbol:

        return Symbol(
            name=node.text.decode(),
            kind=SymbolKind.IMPORT,
            location=Location(
                file=file,
                line=node.start_point[0] + 1,
                column=node.start_point[1] + 1,
            ),
            parent=scope_stack[-1].name if scope_stack else None,
        )