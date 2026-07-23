from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class SymbolKind(Enum):
    MODULE = "module"
    IMPORT = "import"
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    VARIABLE = "variable"
    PARAMETER = "parameter"
    ATTRIBUTE = "attribute"
    CONSTANT = "constant"


@dataclass(slots=True)
class Location:
    """
    Physical location of a symbol.
    """
    file: Path
    line: int
    column: int
#
# Older tests still import SymbolLocation.
#
SymbolLocation = Location

@dataclass(slots=True)
class Symbol:
    name: str

    kind: SymbolKind

    location: Location

    parent: str | None = None

    module: str | None = None

    is_async: bool = False

    decorators: list[str] | None = None

    @property
    def id(self) -> str:
        """
        Stable identifier.

        Example:
        examples/sample.py:6:login
        """
        return f"{self.location.file}:{self.location.line}:{self.name}"


@dataclass(slots=True)
class ImportSymbol(Symbol):
    """
    Represents an import statement.
    """

    module: str | None = None

    imported_name: str | None = None

    alias: str | None = None

    is_from_import: bool = False


