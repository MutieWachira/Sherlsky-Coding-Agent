"""
Call Resolver.

Resolves call expressions to symbols.
"""

from app.language.models import SymbolKind


class CallResolver:

    def resolve(
        self,
        function_name,
        index,
    ):
        """
        Resolve a function name to a symbol.
        """

        candidates = index.find(
            function_name
        )

        for symbol in candidates:

            if symbol.kind in (
                SymbolKind.FUNCTION,
                SymbolKind.METHOD,
            ):

                return symbol

        return None