from pathlib import Path

from compiler.uast.language.models import(
    Symbol,
    SymbolKind,
    SymbolLocation,
)


def test_symbol_creation():

    symbol = Symbol(
        name="User",
        kind=SymbolKind.CLASS,
        location=SymbolLocation(
            Path("a.py"),
            1,
            0,
        ),
    )

    assert symbol.name == "User"

    assert symbol.kind == SymbolKind.CLASS


def test_reference_tracking():

    symbol = Symbol(
        name="login",
        kind=SymbolKind.METHOD,
        location=SymbolLocation(
            Path("a.py"),
            10,
            4,
        ),
    )

    symbol.add_reference(
        SymbolLocation(
            Path("b.py"),
            15,
            8,
        )
    )

    assert symbol.reference_count == 1
