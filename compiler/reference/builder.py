from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from tree_sitter import Node

from compiler.document.document import Document
from compiler.parser.walker import ASTWalker, WalkEvent
from compiler.uast.language.models import Location, Symbol, SymbolKind


@dataclass
class Scope:
    """
    Represents a single lexical scope.
    """

    name: str
    kind: SymbolKind
    parent: Optional["Scope"] = None
    symbol: Optional[Symbol] = None
    children: list["Scope"] = field(default_factory=list)

    def add_child(self, child: Scope) -> None:
        child.parent = self
        self.children.append(child)

    def lookup(self, name: str) -> Scope | None:
        """Lexical scope lookup walking up the parent chain."""
        if any(getattr(s, "name", None) == name for s in self.symbols):
            return self
        if self.parent:
            return self.parent.lookup(name)
        return None


class ScopeBuilder:
    """
    Builds a lexical scope tree from a Tree-sitter AST using event-driven traversal.
    """

    def __init__(self) -> None:
        self.walker = ASTWalker()
        

    def build(self, document: Document) -> Scope:
        """
        Build and return the root Scope for the document.
        """
        tree = document.tree
        file_path = document.path

        # 1. Global / Module root scope
        # Example update matching your actual Scope signature:
        root_scope = Scope(
            name=file_path.stem,  # or module symbol
            kind=SymbolKind.MODULE,
            parent=None,
        )

        current_scope = root_scope
        
        # Track (node, Scope) pairs so we only pop when leaving a scope-creating node
        scope_nodes: list[tuple[Node, Scope]] = []

        # 2. Event-driven traversal using walk_events()
        for event in self.walker.walk_events(tree.root_node):
            node = event.node

            # Handle scope creation on ENTER
            if event.event == WalkEvent.ENTER:
                new_scope_info = self._create_scope_for_node(
                    node, file_path, current_scope
                )

                if new_scope_info is not None:
                    scope_name, scope_kind = new_scope_info

                    new_scope = Scope(
                        name=scope_name,
                        kind=scope_kind,
                        parent=current_scope,
                        location=Location(
                            file=file_path,
                            line=node.start_point[0] + 1,
                            column=node.start_point[1] + 1,
                        ),
                    )

                    current_scope.add_child(new_scope)
                    current_scope = new_scope
                    scope_nodes.append((node, new_scope))

            # Handle scope exit on LEAVE
            elif event.event == WalkEvent.LEAVE:
                if scope_nodes and scope_nodes[-1][0] == node:
                    _, exited_scope = scope_nodes.pop()
                    if exited_scope.parent:
                        current_scope = exited_scope.parent

        return root_scope

    # ---------------------------------------------------------
    # Node Inspection Helpers
    # ---------------------------------------------------------

    def _create_scope_for_node(
        self,
        node: Node,
        file_path: Path,
        current_scope: Scope,
    ) -> Optional[tuple[str, SymbolKind]]:
        """
        Returns (scope_name, symbol_kind) if node creates a lexical scope.
        """
        node_type = node.type

        if node_type == "class_definition":
            name_node = node.child_by_field_name("name")
            name = name_node.text.decode() if name_node else "UnnamedClass"
            return name, SymbolKind.CLASS

        if node_type == "function_definition":
            name_node = node.child_by_field_name("name")
            name = name_node.text.decode() if name_node else "UnnamedFunction"

            kind = (
                SymbolKind.METHOD
                if current_scope.kind == SymbolKind.CLASS
                else SymbolKind.FUNCTION
            )
            return name, kind

        return None