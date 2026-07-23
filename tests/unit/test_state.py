from pathlib import Path

from compiler.document.manager import DocumentManager

from compiler.semantic.scope import Scope
from compiler.semantic.analyzer import SemanticAnalysis
from compiler.semantic.state import SemanticState


def create_state():
    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    return SemanticState(
        document=document,
        analysis=SemanticAnalysis(),
    )


def test_push_scope():
    state = create_state()
    scope = Scope("global")
    state.push_scope(scope)
    assert state.current_scope == scope
    assert state.depth == 1


def test_pop_scope():
    state = create_state()
    scope = Scope("global")
    state.push_scope(scope)
    popped = state.pop_scope()
    assert popped == scope
    assert state.current_scope is None


def test_nested_scopes():
    state = create_state()
    root = Scope("module")
    child = Scope("function")
    state.push_scope(root)
    state.push_scope(child)
    assert state.depth == 2
    assert state.current_scope == child
    state.pop_scope()
    assert state.current_scope == root


def test_reset():
    state = create_state()

    state.push_scope(Scope("module"))
    state.reset()
    assert state.depth == 0
    assert state.current_scope is None
