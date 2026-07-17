from pathlib import Path

from app.language.models import (
    Symbol,
    SymbolKind,
    Location,
)

from app.reference.scope import Scope


def make_symbol(name: str):

    return Symbol(

        name=name,

        kind=SymbolKind.FUNCTION,

        location=Location(

            file=Path("sample.py"),

            line=1,

            column=0,

        ),

    )


def test_add_symbol():

    scope = Scope("global")

    symbol = make_symbol("login")

    scope.add_symbol(symbol)

    assert len(scope) == 1


def test_contains():

    scope = Scope("global")

    symbol = make_symbol("login")

    scope.add_symbol(symbol)

    assert "login" in scope


def test_resolve():

    scope = Scope("global")

    symbol = make_symbol("login")

    scope.add_symbol(symbol)

    assert scope.resolve("login") == symbol


def test_unknown_symbol():

    scope = Scope("global")

    assert scope.resolve("missing") is None