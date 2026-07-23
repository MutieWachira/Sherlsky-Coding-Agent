from pathlib import Path

from app.index.indexer import ProjectIndexer


def test_project_index():

    indexer = ProjectIndexer()

    index = indexer.build(Path("examples"))

    assert len(index.all()) > 0
