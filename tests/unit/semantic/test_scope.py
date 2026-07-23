from pathlib import Path

import pytest

from compiler.semantic.errors import (
    DuplicateSymbolError,
    SymbolNotFoundError,
)

from compiler.semantic.scope import Scope

from compiler.uast.language.models import(
    Symbol,
    SymbolKind,
    SymbolLocation,
)


def create_symbol(name):

    return Symbol(
        name=name,
        kind=SymbolKind.CLASS,
        location=SymbolLocation(
            Path("a.py"),
            1,
            0,
        ),
    )


def test_define():

    scope = Scope("global")

    scope.define(create_symbol("User"))

    assert scope.contains("User")


def test_lookup_parent():

    root = Scope("root")

    child = root.create_child("child")

    root.define(create_symbol("User"))

    assert child.lookup("User").name == "User"


def test_duplicate():

    scope = Scope("root")

    scope.define(create_symbol("User"))

    with pytest.raises(DuplicateSymbolError):
        scope.define(create_symbol("User"))


def test_missing():

    scope = Scope("root")

    with pytest.raises(SymbolNotFoundError):
        scope.lookup("Missing")
