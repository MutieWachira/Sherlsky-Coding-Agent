"""
Semantic Analysis Result.

Returned by SemanticPipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from compiler.document.document import Document
from compiler.semantic.scope import Scope


@dataclass(slots=True)
class SemanticAnalysis:
    """
    Result of semantic analysis.
    """

    document: Document

    root_scope: Scope | None = None

    scopes: list[Scope] = field(default_factory=list)

    calls: list[str] = field(default_factory=list)

    diagnostics: list = field(default_factory=list)

    references: list = field(default_factory=list)

    symbols: list = field(default_factory=list)