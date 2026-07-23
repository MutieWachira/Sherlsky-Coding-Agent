"""
Tests for nested lexical scopes.
"""

from pathlib import Path

from compiler.semantic.scope import (
    Scope,
    ScopeKind,
)

from compiler.uast.language.models import (
    Symbol,
    SymbolKind,
    Location,
)


def symbol(name: str) -> Symbol:
    """
    Create a simple function symbol.
    """

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
    """
    Child scopes should resolve symbols
    defined in parent scopes.
    """

    root = Scope(
        name="module",
        kind=ScopeKind.MODULE,
    )

    child = Scope(
        name="function",
        kind=ScopeKind.FUNCTION,
    )

    root.add_child(child)

    login = symbol("login")

    root.add_symbol(login)

    assert child.resolve("login") == login


def test_shadowing():
    """
    Local symbols should shadow parent symbols.
    """

    root = Scope(
        name="module",
        kind=ScopeKind.MODULE,
    )

    child = Scope(
        name="function",
        kind=ScopeKind.FUNCTION,
    )

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
