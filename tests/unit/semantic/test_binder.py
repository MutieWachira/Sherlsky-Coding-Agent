from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.binder import SemanticBinder


def test_bind_document():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    binder = SemanticBinder()

    root = binder.bind(document)

    #
    # Module should contain at least one symbol.
    #

    assert len(root.symbols) > 0

    #
    # UserService should exist.
    #

    assert "UserService" in root.symbols

    #
    # UserService scope should exist.
    #

    scope = next(s for s in root.children if s.name == "UserService")

    assert scope.resolve("login") is not None
