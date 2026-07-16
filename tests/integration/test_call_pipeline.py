from pathlib import Path

from app.graph.builder import GraphBuilder
from app.index.indexer import ProjectIndexer


def test_call_pipeline():

    index = ProjectIndexer().build(
        Path("examples")
    )

    graph = GraphBuilder().build(index)

    assert any(
        edge.relation.value == "calls"
        for edge in graph.relationships()
    )