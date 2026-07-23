from pathlib import Path

from compiler.graph.builder import GraphBuilder
from app.index.indexer import ProjectIndexer


def test_call_graph():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    call_edges = [
        edge for edge in graph.relationships() if edge.relation.value == "calls"
    ]

    assert len(call_edges) == 3
