"""
Semantic Project Index.

Stores every symbol discovered in a project using
multiple indexes for fast lookup.

This is the central semantic representation of an analyzed project.
Every subsystem (graph building, planners, diagnostics, AI reasoning,
etc.) consumes this object.
"""

from collections import defaultdict
from pathlib import Path

from app.document.document import Document
from app.language.models import Symbol, SymbolKind


class ProjectIndex:
    """
    High-performance semantic project index.

    Maintains multiple indexes so symbols can be queried
    efficiently without scanning the entire project.
    """

    def __init__(self):
        """
        Initialize all indexes.
        """

        #
        # Master symbol collection.
        #
        self._symbols: list[Symbol] = []

        #
        # Documents that belong to this project.
        #
        self.documents: list[Document] = []

        #
        # Secondary indexes.
        #

        # login -> [Symbol]
        self.by_name: dict[str, list[Symbol]] = defaultdict(list)

        # SymbolKind.CLASS -> [...]
        self.by_kind: dict[SymbolKind, list[Symbol]] = defaultdict(list)

        # auth.py -> [...]
        self.by_file: dict[Path, list[Symbol]] = defaultdict(list)

    @property
    def symbols(self) -> list[Symbol]:
        """
        Read-only access to every indexed symbol.
        """

        return self._symbols

    def add(self, symbol: Symbol):
        """
        Add a symbol to every index.
        """

        self._symbols.append(symbol)

        self.by_name[symbol.name].append(symbol)

        self.by_kind[symbol.kind].append(symbol)

        self.by_file[symbol.location.file].append(symbol)

    def all(self) -> list[Symbol]:
        """
        Return every symbol.
        """

        return self._symbols

    def find(self, name: str) -> list[Symbol]:
        """
        Find symbols by name.
        """

        return self.by_name.get(name, [])

    def classes(self) -> list[Symbol]:
        """
        Return all classes.
        """

        return self.by_kind.get(
            SymbolKind.CLASS,
            [],
        )

    def methods(self) -> list[Symbol]:
        """
        Return all methods.
        """

        return self.by_kind.get(
            SymbolKind.METHOD,
            [],
        )

    def functions(self) -> list[Symbol]:
        """
        Return all standalone functions.
        """

        return self.by_kind.get(
            SymbolKind.FUNCTION,
            [],
        )

    def imports(self) -> list[Symbol]:
        """
        Return all imports.
        """

        return self.by_kind.get(
            SymbolKind.IMPORT,
            [],
        )

    def file(self, path: Path) -> list[Symbol]:
        """
        Return every symbol defined inside a file.
        """

        return self.by_file.get(path, [])

    def __len__(self) -> int:
        """
        Number of indexed symbols.
        """

        return len(self._symbols)

    def __iter__(self):
        """
        Iterate over every symbol.
        """

        return iter(self._symbols)

    def __contains__(self, symbol: Symbol) -> bool:
        """
        Membership test.
        """

        return symbol in self._symbols