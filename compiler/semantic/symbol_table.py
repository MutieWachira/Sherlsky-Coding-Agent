"""
Global Symbol Table.

Indexes every symbol inside the workspace.
"""

from __future__ import annotations

from collections import defaultdict

from compiler.uast.language.models import Symbol


class SymbolTable:
    def __init__(self):

        #
        # name -> symbols
        #
        self._symbols = defaultdict(list)

        #
        # id -> symbol
        #
        self._ids = {}

    # ---------------------------------------------------------

    def add(self, symbol: Symbol):

        self._symbols[symbol.name].append(symbol)

        self._ids[symbol.id] = symbol

    # ---------------------------------------------------------

    def add_many(self, symbols: list[Symbol]):

        for symbol in symbols:
            self.add(symbol)

    # ---------------------------------------------------------

    def lookup(self, name: str):

        return self._symbols.get(name, [])

    # ---------------------------------------------------------

    def get(self, symbol_id: str):

        return self._ids.get(symbol_id)

    # ---------------------------------------------------------

    def all(self):

        return list(self._ids.values())

    # ---------------------------------------------------------

    def clear(self):

        self._symbols.clear()

        self._ids.clear()

    # ---------------------------------------------------------

    def __len__(self):

        return len(self._ids)
