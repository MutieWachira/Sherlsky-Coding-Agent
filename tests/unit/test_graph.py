from pathlib import Path

from compiler.graph.builder import GraphBuilder
from compiler.graph.query import GraphQuery
from app.index.indexer import ProjectIndexer


def test_graph_contains_nodes():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    assert len(graph.nodes) > 0


def test_graph_contains_edges():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    assert len(graph.edges) > 0


def test_query_children():

    index = ProjectIndexer().build(Path("examples"))

    graph = GraphBuilder().build(index)

    query = GraphQuery(graph)

    owner = next(
        node for node in graph.nodes.values() if node.symbol.name == "UserService"
    )

    children = query.children(owner.id)

    assert len(children) == 1

    assert children[0].symbol.name == "login"
