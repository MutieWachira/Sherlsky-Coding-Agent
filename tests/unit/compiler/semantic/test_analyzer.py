from pathlib import Path

from compiler.document.manager import DocumentManager


def test_document_analysis():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    assert document.tree is not None

    assert len(document.symbols) > 0
