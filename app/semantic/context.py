"""
Semantic analysis context.
"""

from dataclasses import dataclass

from app.document.document import Document
from app.semantic.analysis import SemanticAnalysis
from app.semantic.state import SemanticState


@dataclass(slots=True)
class SemanticContext:
    """
    Shared context during semantic analysis.
    """

    document: Document

    analysis: SemanticAnalysis

    state: SemanticState