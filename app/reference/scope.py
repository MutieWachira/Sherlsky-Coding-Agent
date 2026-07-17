"""
Lexical Scope.

A Scope represents one lexical region of a source file.

Scopes form a tree.

Example
-------

Module
│
├── Class
│      │
│      └── Method
│
└── Function

Scopes are responsible for:

- Registering symbols
- Resolving identifiers
- Shadowing rules
- Parent lookups
- Child scope management
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Iterator, TYPE_CHECKING

from tree_sitter import Node

from app.language.models import Symbol

if TYPE_CHECKING:
    from app.document.document import Document


class ScopeKind(Enum):
    """
    Types of lexical scopes.
    """

    MODULE = auto()

    CLASS = auto()

    FUNCTION = auto()

    METHOD = auto()

    LAMBDA = auto()

    COMPREHENSION = auto()

    BLOCK = auto()


@dataclass(slots=True)
class Scope:
    """
    Represents one lexical scope.

    Parameters
    ----------
    name
        Human-readable scope name.

    kind
        Scope type.

    document
        Document that owns this scope.

    owner
        Symbol that created this scope.

    node
        Tree-sitter AST node.

    parent
        Parent lexical scope.

    start_line
        First line covered.

    end_line
        Last line covered.
    """

    name: str

    kind: ScopeKind

    document: Document | None = None

    owner: Symbol | None = None

    node: Node | None = None

    parent: "Scope | None" = None

    children: list["Scope"] = field(default_factory=list)

    symbols: dict[str, Symbol] = field(default_factory=dict)

    start_line: int = 0

    end_line: int = 0

    # ---------------------------------------------------------
    # Symbol Management
    # ---------------------------------------------------------

    def add_symbol(
        self,
        symbol: Symbol,
    ) -> None:
        """
        Register a symbol inside this scope.
        """

        self.symbols[symbol.name] = symbol

    def remove_symbol(
        self,
        name: str,
    ) -> None:
        """
        Remove a symbol if it exists.
        """

        self.symbols.pop(name, None)

    def has_local(
        self,
        name: str,
    ) -> bool:
        """
        Return True if this scope defines the symbol locally.
        """

        return name in self.symbols

    # ---------------------------------------------------------
    # Resolution
    # ---------------------------------------------------------

    def resolve(
        self,
        name: str,
    ) -> Symbol | None:
        """
        Resolve a symbol.

        Resolution starts from the current scope and
        walks upward until the global scope.

        Returns
        -------
        Symbol | None
        """

        if name in self.symbols:
            return self.symbols[name]

        if self.parent is not None:
            return self.parent.resolve(name)

        return None

    # ---------------------------------------------------------
    # Tree Management
    # ---------------------------------------------------------

    def add_child(
        self,
        child: "Scope",
    ) -> None:
        """
        Attach a child scope.
        """

        child.parent = self
        self.children.append(child)

    # ---------------------------------------------------------
    # Iterators
    # ---------------------------------------------------------

    def iter_symbols(self) -> Iterator[Symbol]:
        """
        Iterate over local symbols.
        """

        yield from self.symbols.values()

    def iter_children(self) -> Iterator["Scope"]:
        """
        Iterate over child scopes.
        """

        yield from self.children

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def is_global(self) -> bool:
        """
        True if this is the module scope.
        """

        return self.kind == ScopeKind.MODULE

    @property
    def depth(self) -> int:
        """
        Compute nesting depth.

        Module = 0
        Class = 1
        Method = 2
        ...
        """

        depth = 0

        scope = self.parent

        while scope is not None:
            depth += 1
            scope = scope.parent

        return depth

    # ---------------------------------------------------------
    # Magic Methods
    # ---------------------------------------------------------

    def __contains__(
        self,
        name: str,
    ) -> bool:
        return name in self.symbols

    def __len__(self) -> int:
        return len(self.symbols)

    def __iter__(self) -> Iterator[Symbol]:
        yield from self.symbols.values()

    def __repr__(self) -> str:
        return (
            f"Scope("
            f"name={self.name!r}, "
            f"kind={self.kind.name}, "
            f"symbols={len(self.symbols)}, "
            f"children={len(self.children)}"
            f")"
        )