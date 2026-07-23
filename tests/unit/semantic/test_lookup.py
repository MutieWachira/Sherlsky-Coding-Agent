from pathlib import Path

from compiler.semantic.lookup import LookupService
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
            Path("sample.py"),
            1,
            0,
        ),
    )


def test_lookup():

    root = Scope("root")

    root.define(create_symbol("User"))

    lookup = LookupService(root)

    symbol = lookup.resolve(root, "User")

    assert symbol.name == "User"


def test_exists():

    root = Scope("root")

    root.define(create_symbol("User"))

    lookup = LookupService(root)

    assert lookup.exists(root, "User")

    assert not lookup.exists(root, "Missing")
