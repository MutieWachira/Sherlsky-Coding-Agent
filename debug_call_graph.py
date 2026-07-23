from pathlib import Path

from app.index.indexer import ProjectIndexer
from compiler.graph.builder import GraphBuilder

index = ProjectIndexer().build(Path("examples"))

print("\nFunctions")
print("-" * 40)

for f in index.functions():
    print(f.name)

graph = GraphBuilder().build(index)

print("\nRelationships")
print("-" * 40)

for edge in graph.relationships():

    source = graph.get_node(edge.source).symbol.name
    target = graph.get_node(edge.target).symbol.name

    print(
        source,
        edge.relation.value,
        target,
    )