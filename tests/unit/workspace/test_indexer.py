from pathlib import Path

from compiler.workspace.indexer import WorkspaceIndexer


def test_index_single_file():

    indexer = WorkspaceIndexer()

    document = indexer.index_file(Path("examples/sample.py"))

    assert document is not None

    assert len(document.symbols) > 0

    assert len(indexer.symbols) > 0


def test_lookup():

    indexer = WorkspaceIndexer()

    indexer.index_file(Path("examples/sample.py"))

    results = indexer.lookup("login")

    assert isinstance(results, list)


def test_clear():

    indexer = WorkspaceIndexer()

    indexer.index_file(Path("examples/sample.py"))

    indexer.clear()

    assert len(indexer.symbols) == 0
