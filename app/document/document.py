"""
Document Model.

Represents one source file inside Forge.

Every subsystem shares the same Document object.
"""

from dataclasses import dataclass, field
from pathlib import Path
from tree_sitter import Tree

from app.language.models import Symbol


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
    # Semantic symbols
    #
    symbols: list[Symbol] = field(default_factory=list)

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
    metadata: dict = field(default_factory=dict)