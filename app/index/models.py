"""
Semantic Project Index.

Stores every symbol discovered in a project using
multiple indexes for fast lookup.
"""

from collections import defaultdict
from pathlib import Path

from app.language.models import Symbol, SymbolKind


class ProjectIndex:
    """
    High-performance semantic index.
    """

    def __init__(self):

        # Every symbol
        self.symbols: list[Symbol] = []

        # login -> [Symbol]
        self.by_name = defaultdict(list)

        # SymbolKind.CLASS -> [...]
        self.by_kind = defaultdict(list)

        # auth.py -> [...]
        self.by_file = defaultdict(list)

    def add(self, symbol: Symbol):

        self.symbols.append(symbol)

        self.by_name[symbol.name].append(symbol)

        self.by_kind[symbol.kind].append(symbol)

        self.by_file[symbol.location.file].append(symbol)

    def all(self):

        return self.symbols

    def find(self, name):

        return self.by_name.get(name, [])

    def classes(self):

        return self.by_kind.get(
            SymbolKind.CLASS,
            [],
        )

    def methods(self):

        return self.by_kind.get(
            SymbolKind.METHOD,
            [],
        )

    def functions(self):

        return self.by_kind.get(
            SymbolKind.FUNCTION,
            [],
        )

    def imports(self):

        return self.by_kind.get(
            SymbolKind.IMPORT,
            [],
        )

    def file(self, path: Path):

        return self.by_file.get(path, [])