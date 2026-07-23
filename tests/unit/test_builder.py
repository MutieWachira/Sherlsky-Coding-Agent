from pathlib import Path

from app.index.indexer import ProjectIndexer
from compiler.graph.builder import GraphBuilder
from compiler.graph.relationships import RelationshipType


def test_build_graph():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    relationships = graph.relationships()

    assert len(relationships) > 0

    assert relationships[0].relation == RelationshipType.OWNS
