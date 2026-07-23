"""
Semantic Project Index.

Stores every symbol discovered in a project using
multiple indexes for fast lookup.

This is the central semantic representation of an analyzed project.

Consumed by:
- Semantic Analysis
- Reference Resolution
- Knowledge Graph
- Call Graph
- Diagnostics
- Workspace Indexer
- LSP Features
- AI Reasoning
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from compiler.document.document import Document
from compiler.uast.language.models import Symbol, SymbolKind


class ProjectIndex:
    """
    Global semantic index for an analyzed workspace.
    """

    def __init__(self):

        #
        # Master symbol collection
        #
        self._symbols: list[Symbol] = []

        #
        # Indexed documents
        #
        self.documents: list[Document] = []

        #
        # Secondary indexes
        #
        self.by_name: dict[str, list[Symbol]] = defaultdict(list)

        self.by_kind: dict[SymbolKind, list[Symbol]] = defaultdict(list)

        self.by_file: dict[Path, list[Symbol]] = defaultdict(list)

        #
        # Fast lookup by id
        #
        self.by_id: dict[str, Symbol] = {}

    # ==========================================================
    # Documents
    # ==========================================================

    def add_document(
        self,
        document: Document,
    ) -> None:

        if document not in self.documents:
            self.documents.append(document)

    # ==========================================================
    # Symbols
    # ==========================================================

    def add(
        self,
        symbol: Symbol,
    ) -> None:

        #
        # Prevent duplicate ids.
        #
        if symbol.id in self.by_id:
            return

        self._symbols.append(symbol)

        self.by_id[symbol.id] = symbol

        self.by_name[symbol.name].append(symbol)

        self.by_kind[symbol.kind].append(symbol)

        self.by_file[symbol.location.file].append(symbol)

    def add_many(
        self,
        symbols: list[Symbol],
    ) -> None:

        for symbol in symbols:
            self.add(symbol)

    # ==========================================================
    # Lookup API
    # ==========================================================

    def lookup(
        self,
        name: str,
    ) -> list[Symbol]:
        """
        Lookup symbols by name.

        Used by:
            ReferenceResolver
            CallResolver
            GraphBuilder
        """

        return self.by_name.get(name, [])

    def find(
        self,
        name: str,
    ) -> list[Symbol]:
        """
        Alias for lookup().
        """

        return self.lookup(name)

    def get(
        self,
        symbol_id: str,
    ) -> Symbol | None:
        """
        Lookup by symbol id.
        """

        return self.by_id.get(symbol_id)

    # ==========================================================
    # Query Helpers
    # ==========================================================

    @property
    def symbols(self) -> list[Symbol]:
        return self._symbols

    def all(self) -> list[Symbol]:
        return self._symbols

    def classes(self):

        return self.by_kind.get(SymbolKind.CLASS, [])

    def methods(self):

        return self.by_kind.get(SymbolKind.METHOD, [])

    def functions(self):

        return self.by_kind.get(SymbolKind.FUNCTION, [])

    def imports(self):

        return self.by_kind.get(SymbolKind.IMPORT, [])

    def variables(self):

        return self.by_kind.get(SymbolKind.VARIABLE, [])

    def parameters(self):

        return self.by_kind.get(SymbolKind.PARAMETER, [])

    def constants(self):

        return self.by_kind.get(SymbolKind.CONSTANT, [])

    def attributes(self):

        return self.by_kind.get(SymbolKind.ATTRIBUTE, [])

    def file(
        self,
        path: Path,
    ) -> list[Symbol]:

        return self.by_file.get(path, [])

    # ==========================================================
    # Advanced Queries
    # ==========================================================

    def children_of(
        self,
        parent: str,
    ) -> list[Symbol]:
        """
        Return every symbol owned by a parent.

        Example:
            class -> methods
            function -> parameters
        """

        return [
            symbol
            for symbol in self._symbols
            if symbol.parent == parent
        ]

    def exists(
        self,
        name: str,
    ) -> bool:

        return name in self.by_name

    def document(
        self,
        path: Path,
    ) -> Document | None:

        for document in self.documents:

            if document.path == path:
                return document

        return None

    # ==========================================================
    # Utilities
    # ==========================================================

    def clear(self):

        self._symbols.clear()

        self.documents.clear()

        self.by_name.clear()

        self.by_kind.clear()

        self.by_file.clear()

        self.by_id.clear()

    # ==========================================================

    def __len__(self):

        return len(self._symbols)

    def __iter__(self):

        return iter(self._symbols)

    def __contains__(
        self,
        symbol: Symbol,
    ):

        return symbol.id in self.by_id