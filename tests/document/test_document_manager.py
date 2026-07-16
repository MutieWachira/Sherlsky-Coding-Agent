from pathlib import Path

from app.document.manager import DocumentManager


def test_document_cache():

    manager = DocumentManager()

    doc1 = manager.open(
        Path("examples/sample.py")
    )

    doc2 = manager.open(
        Path("examples/sample.py")
    )

    #
    # Cached object should be reused.
    #
    assert doc1 is doc2


def test_document_source():

    manager = DocumentManager()

    doc = manager.open(
        Path("examples/sample.py")
    )

    assert "UserService" in doc.source


def test_document_tree():

    manager = DocumentManager()

    doc = manager.open(
        Path("examples/sample.py")
    )

    assert doc.tree is not None