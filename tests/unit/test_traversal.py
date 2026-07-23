from pathlib import Path

from compiler.semantic.scope import (
    Scope,
    ScopeKind,
)

from compiler.semantic.traversal import TraversalState

from compiler.uast.language.models import (
    Symbol,
    SymbolKind,
    Location,
)


def symbol(name: str) -> Symbol:
    """
    Create a simple class symbol.
    """

    return Symbol(
        name=name,
        kind=SymbolKind.CLASS,
        location=Location(
            Path("sample.py"),
            1,
            0,
        ),
    )


def test_scope_stack():
    """
    Pushing a scope should increase scope depth.
    """

    state = TraversalState()

    state.push_scope(
        Scope(
            name="module",
            kind=ScopeKind.MODULE,
        )
    )

    assert state.scope_depth == 1


def test_owner_stack():
    """
    Owners should be tracked correctly.
    """

    state = TraversalState()

    owner = symbol("User")

    state.push_owner(owner)

    assert state.current_owner == owner


def test_node_stack():
    """
    Nodes should be pushed and popped correctly.
    """

    state = TraversalState()

    node = object()

    state.push_node(node)

    assert state.current_node == node

    state.pop_node()

    assert state.current_node is None


def test_reset():
    """
    Reset should clear all traversal state.
    """

    state = TraversalState()

    state.push_scope(
        Scope(
            name="module",
            kind=ScopeKind.MODULE,
        )
    )

    state.push_owner(symbol("User"))

    state.push_node(object())

    state.reset()

    assert state.scope_depth == 0
    assert state.owner_depth == 0
    assert state.current_node is None
