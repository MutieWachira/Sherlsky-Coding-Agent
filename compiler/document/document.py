"""
Document Model.

Represents one source file inside Forge.

Every subsystem shares the same Document object.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING

from tree_sitter import Tree

from compiler.uast.language.models import Symbol

#
# Import only for static type checking.
# This avoids circular imports at runtime.
#
if TYPE_CHECKING:
    from compiler.semantic.scope import Scope
    from compiler.reference.models import Reference


@dataclass(slots=True)
class Document:
    """
    Represents one source file.
    """

    #
    # File path
    #
    path: Path

    #
    # Original source code
    #
    source: str

    #
    # Parsed Tree-sitter AST
    #
    tree: Tree

    #
    # Symbols discovered in this file
    #
    symbols: list[Symbol] = field(default_factory=list)

    #
    # Root lexical scope
    #
    scope: Scope | None = None

    #
    # Identifier references
    #
    references: list[Reference] = field(default_factory=list)

    #
    # Diagnostics
    #
    diagnostics: list = field(default_factory=list)

    #
    # Incremented whenever the file changes
    #
    version: int = 1

    #
    # Arbitrary metadata
    #
    metadata: dict[str, object] = field(default_factory=dict)