"""
Graph Query API.
"""

from compiler.graph.graph import KnowledgeGraph


class GraphQuery:
    def __init__(self, graph: KnowledgeGraph):

        self.graph = graph

    def children(self, node_id):

        result = []

        for edge_id in self.graph.outgoing[node_id]:
            edge = self.graph.get_edge(edge_id)

            result.append(self.graph.get_node(edge.target))

        return result

    def parents(self, node_id):

        result = []

        for edge_id in self.graph.incoming[node_id]:
            edge = self.graph.get_edge(edge_id)

            result.append(self.graph.get_node(edge.source))

        return result
