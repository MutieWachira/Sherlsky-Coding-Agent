from pathlib import Path

from app.document.manager import DocumentManager
from app.index.indexer import ProjectIndexer


def test_document_pipeline():

    manager = DocumentManager()

    doc = manager.open(
        Path("examples/sample.py")
    )

    assert doc.tree

    assert doc.source

    assert doc.path.exists()

def test_index_populates_documents():

    indexer = ProjectIndexer()

    indexer.build(Path("examples"))

    for document in indexer.documents.documents():

        assert document.tree is not None
        assert len(document.symbols) > 0