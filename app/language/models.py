from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class SymbolKind(Enum):
    CLASS = "class"
    FUNCTION = "function"
    METHOD = "method"
    IMPORT = "import"


@dataclass(slots=True)
class Location:
    file: Path
    line: int
    column: int


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
        return (
            f"{self.location.file}:"
            f"{self.location.line}:"
            f"{self.name}"
        )
@dataclass(slots=True)
class ImportSymbol(Symbol):
    """
    Represents an import statement.
    """

    module: str | None = None

    imported_name: str | None = None

    alias: str | None = None

    is_from_import: bool = False   
