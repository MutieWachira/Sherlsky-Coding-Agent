from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.binder import SemanticBinder
from compiler.semantic.scope import ScopeKind


def test_scope_tree():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    binder = SemanticBinder()

    root = binder.bind(document)

    assert root.kind == ScopeKind.MODULE

    assert len(root.children) > 0

    class_scope = next(
        scope for scope in root.children if scope.kind == ScopeKind.CLASS
    )

    assert class_scope.name == "UserService"
