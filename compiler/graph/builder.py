"""
Knowledge Graph Builder.

Builds a semantic Knowledge Graph from a ProjectIndex.

Current relationships:
- Class -> Method (OWNS)
- Function -> Function (CALLS)

Future relationships:
- IMPORTS
- REFERENCES
- INHERITS
- IMPLEMENTS
"""

from compiler.graph.call_builder import CallGraphBuilder
from compiler.graph.graph import KnowledgeGraph
from compiler.graph.models import Relationship
from compiler.graph.relationships import RelationshipType


class GraphBuilder:
    """
    Builds a KnowledgeGraph from a ProjectIndex.
    """

    def __init__(self):
        """
        Initialize graph builders.
        """
        self.call_builder = CallGraphBuilder()

    def build(self, index):
        """
        Build the complete knowledge graph.

        Parameters
        ----------
        index : ProjectIndex
            The indexed project containing documents and symbols.

        Returns
        -------
        KnowledgeGraph
        """

        graph = KnowledgeGraph()

        # --------------------------------------------------
        # STEP 1
        # Register every symbol as a graph node.
        # --------------------------------------------------
        for symbol in index.all():
            graph.add_node(symbol)

        # --------------------------------------------------
        # STEP 2
        # Build Class -> Method ownership relationships.
        # --------------------------------------------------
        for method in index.methods():
            if method.parent is None:
                continue

            owners = index.find(method.parent)

            if not owners:
                continue

            owner = owners[0]

            if owner.id == method.id:
                continue

            graph.add_edge(
                Relationship.create(
                    source=owner.id,
                    target=method.id,
                    relation=RelationshipType.OWNS,
                )
            )

        # --------------------------------------------------
        # STEP 3
        # Build function call relationships.
        # --------------------------------------------------
        for document in index.documents:
            self.call_builder.build(
                document=document,
                graph=graph,
                index=index,
            )

        return graph
