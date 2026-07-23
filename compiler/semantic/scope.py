"""
Lexical scopes.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from compiler.semantic.errors import (
    DuplicateSymbolError,
)

from compiler.uast.language.models import Symbol
from enum import Enum


class ScopeKind(str, Enum):
    MODULE = "module"

    CLASS = "class"

    FUNCTION = "function"

    BLOCK = "block"

    LOOP = "loop"

    COMPREHENSION = "comprehension"


@dataclass(slots=True)
class Scope:
    """
    Represents a lexical scope.
    """

    name: str

    kind: ScopeKind = ScopeKind.BLOCK

    parent: "Scope | None" = None

    children: list["Scope"] = field(default_factory=list)

    symbols: dict[str, Symbol] = field(default_factory=dict)

    # ------------------------

    def create_child(
        self,
        name: str,
        kind: ScopeKind = ScopeKind.BLOCK,
    ):

        child = Scope(
            name=name,
            kind=kind,
            parent=self,
        )

        self.children.append(child)

        return child

    # ------------------------

    def define(self, symbol: Symbol) -> None:

        if symbol.name in self.symbols:
            raise DuplicateSymbolError(symbol.name)

        self.symbols[symbol.name] = symbol

    # ------------------------

    def lookup_local(self, name: str):

        return self.symbols.get(name)

    # ------------------------

    def lookup(
        self,
        name: str,
    ):
        """
        Search this scope and parents.
        """

        scope = self

        while scope:
            symbol = scope.symbols.get(name)

            if symbol:
                return symbol

            scope = scope.parent

        return None

    # ------------------------

    def contains(self, name: str) -> bool:

        return name in self.symbols

    # ------------------------

    def __len__(self):

        return len(self.symbols)

    # ------------------------

    def __iter__(self):

        return iter(self.symbols.values())
