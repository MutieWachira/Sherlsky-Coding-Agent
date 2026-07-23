import time
from pathlib import Path

from app.index.indexer import ProjectIndexer


def test_index_speed():
    start = time.perf_counter()

    ProjectIndexer().build(Path("examples"))

    elapsed = time.perf_counter() - start

    # Adjust this threshold as your project grows.
    assert elapsed < 1.0
