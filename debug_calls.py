from pathlib import Path

from app.graph.builder import GraphBuilder
from app.index.indexer import ProjectIndexer

index = ProjectIndexer().build(
    Path("examples")
)

graph = GraphBuilder().build(index)

print()

print("Call Graph")

print("----------------")

for edge in graph.relationships():

    if edge.relation.value != "calls":
        continue

    source = graph.get_node(edge.source)

    target = graph.get_node(edge.target)

    print(
        f"{source.symbol.name}"
        f" ---> "
        f"{target.symbol.name}"
    )