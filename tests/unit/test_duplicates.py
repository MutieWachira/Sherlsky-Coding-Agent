from pathlib import Path

from app.index.indexer import ProjectIndexer
from app.index.duplicate import DuplicateDetector


def test_duplicates():

    index = ProjectIndexer().build(Path("examples"))

    detector = DuplicateDetector()

    duplicates = detector.find_duplicates(index)

    assert isinstance(
        duplicates,
        dict,
    )
