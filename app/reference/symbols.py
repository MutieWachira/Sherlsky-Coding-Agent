"""
Reference Models.
"""

from dataclasses import dataclass

from app.language.models import Symbol


@dataclass(slots=True)
class SymbolReference:
    """
    Represents one identifier referring to one symbol.
    """

    identifier: str

    source: Symbol

    target: Symbol