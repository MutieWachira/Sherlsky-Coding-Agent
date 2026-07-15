from pathlib import Path

from app.index.indexer import ProjectIndexer
from app.index.statistics import IndexStatistics


def test_statistics():

    index = ProjectIndexer().build(
        Path("examples")
    )

    stats = IndexStatistics().summary(
        index
    )

    assert stats["symbols"] > 0