from pathlib import Path

from app.index.indexer import ProjectIndexer
from compiler.graph.builder import GraphBuilder
from compiler.graph.relationships import RelationshipType


def test_call_pipeline():

    index = ProjectIndexer().build(
        Path("examples")
    )

    graph = GraphBuilder().build(index)

    calls = [

        edge

        for edge in graph.relationships()

        if edge.relation == RelationshipType.CALLS

    ]

    assert len(calls) > 0

    for edge in calls:

        assert graph.get_node(edge.source) is not None

        assert graph.get_node(edge.target) is not None