from pathlib import Path

from app.document.manager import DocumentManager


def test_document_pipeline():

    manager = DocumentManager()

    doc = manager.open(
        Path("examples/sample.py")
    )

    assert doc.tree

    assert doc.source

    assert doc.path.exists()