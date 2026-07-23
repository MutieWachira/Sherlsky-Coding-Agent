from pathlib import Path

from compiler.document.manager import DocumentManager


def test_extract_symbols():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    assert len(document.symbols) > 0


def test_has_class():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    assert any(s.name == "UserService" for s in document.symbols)


def test_has_method():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    assert any(s.name == "login" for s in document.symbols)
