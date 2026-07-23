"""
Call Resolver.

Resolves function and method call sites into semantic symbols.
"""

from compiler.uast.language.models import Symbol


class CallResolver:

    def resolve(
        self,
        name: str,
        index,
    ) -> Symbol | None:

        matches = index.lookup(name)

        if not matches:
            return None

        #
        # Prefer executable symbols.
        #

        for symbol in matches:

            if symbol.kind.name in (
                "FUNCTION",
                "METHOD",
            ):
                return symbol

        return matches[0]