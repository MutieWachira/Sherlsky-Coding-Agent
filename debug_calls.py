from pathlib import Path

from app.index.indexer import ProjectIndexer
from compiler.graph.builder import GraphBuilder


index = ProjectIndexer().build(Path("examples"))

graph = GraphBuilder().build(index)

print("\nNODES\n")

for node in graph.nodes.values():

    print(
        node.symbol.kind.name,
        node.symbol.name,
    )

print("\nCALLS\n")

for edge in graph.relationships():

    if edge.relation.value != "calls":
        continue

    src = graph.get_node(edge.source).symbol

    dst = graph.get_node(edge.target).symbol

    print(
        f"{src.name} -> {dst.name}"
    )