from pathlib import Path

from app.graph.builder import GraphBuilder
from app.index.indexer import ProjectIndexer

index = ProjectIndexer().build(Path("examples"))
graph = GraphBuilder().build(index)

print("=== Nodes ===")
for node in graph.nodes.values():
    print(f"{node.id[:8]} {node.symbol.kind.value:10} {node.symbol.name}")

print("\n=== Edges ===")
for edge in graph.edges.values():
    source = graph.get_node(edge.source)
    target = graph.get_node(edge.target)

    print(
        f"{source.symbol.name} --{edge.relation.value}--> {target.symbol.name}"
    )