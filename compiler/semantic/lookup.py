"""
Semantic lookup utilities.

Provides helper methods used by the SymbolTable and
future semantic passes.
"""

from __future__ import annotations

from compiler.semantic.scope import Scope
from compiler.uast.language.models import Symbol


class LookupService:
    """
    Performs semantic symbol resolution.
    """

    def __init__(self, root: Scope):

        self.root = root

    # --------------------------------------------------

    def resolve(self, scope: Scope, name: str) -> Symbol:
        """
        Resolve a symbol using lexical scope rules.
        """
        return scope.lookup(name)

    # --------------------------------------------------

    def exists(self, scope: Scope, name: str) -> bool:
        """
        Returns True if the symbol exists.
        """

        try:
            scope.lookup(name)

            return True

        except Exception:
            return False

    # --------------------------------------------------

    def globals(self):

        return list(self.root.symbols.values())
