from pathlib import Path

from compiler.graph.builder import GraphBuilder
from app.index.indexer import ProjectIndexer


def test_complete_pipeline():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    assert len(index.all()) > 0

    assert len(graph.nodes) > 0

    assert len(graph.edges) > 0
