from pathlib import Path

from app.language.models import (
    Symbol,
    SymbolKind,
    Location,
)

from app.reference.scope import Scope


def symbol(name):

    return Symbol(

        name=name,

        kind=SymbolKind.FUNCTION,

        location=Location(

            Path("sample.py"),

            1,

            0,

        ),

    )


def test_parent_lookup():

    root = Scope("global")

    child = Scope("function")

    root.add_child(child)

    login = symbol("login")

    root.add_symbol(login)

    assert child.resolve("login") == login


def test_shadowing():

    root = Scope("global")

    child = Scope("function")

    root.add_child(child)

    global_symbol = symbol("value")

    local_symbol = Symbol(

        name="value",

        kind=SymbolKind.VARIABLE,

        location=Location(

            Path("sample.py"),

            5,

            4,

        ),

    )

    root.add_symbol(global_symbol)

    child.add_symbol(local_symbol)

    assert child.resolve("value") == local_symbol