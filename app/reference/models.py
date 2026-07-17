"""
Reference Models.

Defines the data structures used by the
Reference Resolution Engine.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from app.language.models import Symbol


class ReferenceKind(Enum):
    """
    Types of semantic references.
    """

    FUNCTION = "function"

    METHOD = "method"

    CLASS = "class"

    VARIABLE = "variable"

    IMPORT = "import"

    PARAMETER = "parameter"

    ATTRIBUTE = "attribute"


@dataclass(slots=True)
class Reference:
    """
    Represents a resolved identifier.

    Example

    login()

    login -> Function Symbol
    """

    identifier: str

    source: Symbol

    target: Symbol

    kind: ReferenceKind