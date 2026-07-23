"""
Semantic analysis exceptions.

These exceptions are raised during symbol resolution,
scope analysis and semantic validation.
"""

from __future__ import annotations


class SemanticError(Exception):
    """Base semantic exception."""


class DuplicateSymbolError(SemanticError):
    """Raised when a symbol already exists in a scope."""


class SymbolNotFoundError(SemanticError):
    """Raised when a symbol cannot be resolved."""
