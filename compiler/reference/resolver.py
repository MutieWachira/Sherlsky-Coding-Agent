"""
Reference Resolver.

Resolves identifier usages to the symbols that define them.

Example

x = 10

print(x)

The identifier "x" inside print()
must resolve back to the variable x.
"""

from __future__ import annotations

from tree_sitter import Node

from compiler.document.document import Document
from compiler.reference.models import Reference
from compiler.semantic.symbol_table import SymbolTable


class ReferenceResolver:
    """
    Resolves identifier usages to symbols.
    """

    def __init__(
        self,
        symbols: SymbolTable,
    ):
        self.symbols = symbols

    def resolve_document(
        self,
        document: Document,
    ) -> list[Reference]:

        references: list[Reference] = []

        self._visit(
            document.tree.root_node,
            document,
            references,
        )

        document.references = references
        return references

    def _visit(
        self,
        node: Node,
        document: Document,
        references: list[Reference],
    ):

        if node.type == "identifier":
            self._resolve_identifier(
                node,
                document,
                references,
            )

        for child in node.children:
            self._visit(
                child,
                document,
                references,
            )

    def _resolve_identifier(
        self,
        node,
        document,
        references,
    ):
        """
        Resolve one identifier node.
        """

        name = node.text.decode("utf-8")

        candidates = self.symbols.lookup(name)

        if not candidates:
            return

        #
        # Temporary implementation:
        # choose the first matching symbol.
        #
        target = candidates[0]

        reference = Reference(
            identifier=name,
            source=target,
            target=target,
            kind=target.kind,
        )

        references.append(reference)
