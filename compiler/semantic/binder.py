"""
AST-driven Semantic Binder.

Builds the lexical scope tree directly from the syntax tree.
"""

from __future__ import annotations

from compiler.document.document import Document
from compiler.parser.walker import ASTWalker
from compiler.semantic.scope import Scope, ScopeKind


class SemanticBinder:
    def __init__(self):

        self.walker = ASTWalker()

    def bind(
        self,
        document: Document,
    ) -> Scope:

        #
        # Root module scope
        #
        root = Scope(
            name=document.path.stem,
            kind=ScopeKind.MODULE,
        )

        #
        # Current lexical scope
        #
        self._scope_stack = [root]

        #
        # Build tree
        #
        self._visit(
            document.tree.root_node,
            document,
        )

        document.scope = root

        return root

    def _visit(
        self,
        node,
        document,
    ):

        enter_scope = False

        #
        # Enter class scope
        #
        if node.type == "class_definition":
            name = node.child_by_field_name("name")

            if name:
                scope = self._scope_stack[-1].create_child(
                    name.text.decode(),
                    ScopeKind.CLASS,
                )

                self._scope_stack.append(scope)

                enter_scope = True

        #
        # Enter function scope
        #
        elif node.type == "function_definition":
            name = node.child_by_field_name("name")

            if name:
                scope = self._scope_stack[-1].create_child(
                    name.text.decode(),
                    ScopeKind.FUNCTION,
                )

                self._scope_stack.append(scope)

                enter_scope = True

        #
        # Register symbols that belong to this node
        #
        self._attach_symbols(
            node,
            document,
        )

        #
        # Visit children
        #
        for child in node.children:
            self._visit(
                child,
                document,
            )

        #
        # Leave scope
        #
        if enter_scope:
            self._scope_stack.pop()

    def _attach_symbols(
        self,
        node,
        document,
    ):

        current = self._scope_stack[-1]

        line = node.start_point[0] + 1

        for symbol in document.symbols:
            if symbol.location.line != line:
                continue

            #
            # Prevent duplicates
            #
            if current.contains(symbol.name):
                continue

            current.define(symbol)
