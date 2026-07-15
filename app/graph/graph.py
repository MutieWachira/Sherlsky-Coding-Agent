"""
Knowledge Graph implementation.
"""

from collections import defaultdict

from app.graph.models import (
    GraphNode,
    Relationship,
)


class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}

        self.edges = {}

        self.outgoing = defaultdict(list)

        self.incoming = defaultdict(list)

    def add_node(self, symbol):

        if symbol.id in self.nodes:

            return self.nodes[symbol.id]

        node = GraphNode(
            id=symbol.id,
            symbol=symbol,
        )

        self.nodes[node.id] = node

        return node

    def add_edge(self, edge: Relationship):

        self.edges[edge.id] = edge

        self.outgoing[
            edge.source
        ].append(edge.id)

        self.incoming[
            edge.target
        ].append(edge.id)

    def get_node(self, node_id):

        return self.nodes.get(node_id)

    def get_edge(self, edge_id):

        return self.edges.get(edge_id)
    
    def relationships(self):
        """
        Return all relationships in the graph.

        Keeping this method preserves backward compatibility
        while allowing the internal storage to remain optimized.
        """
        return list(self.edges.values())