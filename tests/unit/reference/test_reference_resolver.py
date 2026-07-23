from pathlib import Path

from compiler.workspace.indexer import WorkspaceIndexer


def test_reference_resolution():

    indexer = WorkspaceIndexer()

    document = indexer.index_file(Path("examples/sample.py"))

    assert len(document.references) > 0
