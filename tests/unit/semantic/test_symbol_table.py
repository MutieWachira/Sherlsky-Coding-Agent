from pathlib import Path

from compiler.uast.language.models import (
    Symbol,
    SymbolKind,
    SymbolTable,
    Location,
)


def make_symbol(name: str):

    return Symbol(
        name=name,
        kind=SymbolKind.FUNCTION,
        location=Location(
            file=Path("example.py"),
            line=1,
            column=0,
        ),
    )


def test_add_symbol():

    table = SymbolTable()

    symbol = make_symbol("login")

    table.add(symbol)

    assert len(table) == 1


def test_lookup():

    table = SymbolTable()

    table.add(make_symbol("login"))

    assert len(table.lookup("login")) == 1


def test_get_by_id():

    table = SymbolTable()

    symbol = make_symbol("login")

    table.add(symbol)

    assert table.get(symbol.id) == symbol


def test_clear():

    table = SymbolTable()

    table.add(make_symbol("login"))

    table.clear()

    assert len(table) == 0
