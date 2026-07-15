"""
Knowledge Graph Builder.

Builds a semantic knowledge graph from the ProjectIndex.
"""

from app.graph.graph import KnowledgeGraph
from app.graph.models import Relationship
from app.graph.relationships import RelationshipType


class GraphBuilder:
    """
    Converts a ProjectIndex into a KnowledgeGraph.
    """

    def build(self, index):
        """
        Build a knowledge graph from the indexed project.

        Parameters
        ----------
        index : ProjectIndex
            The semantic project index.

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
        # Create Class -> Method ownership relationships.
        # --------------------------------------------------
        for method in index.methods():

            # Skip standalone functions.
            if method.parent is None:
                continue

            # Find the class that owns this method.
            owners = index.find(method.parent)

            if not owners:
                continue

            owner = owners[0]

            edge = Relationship.create(
                source=owner.id,
                target=method.id,
                relation=RelationshipType.OWNS,
            )

            graph.add_edge(edge)

        # --------------------------------------------------
        # Future relationship builders
        #
        # - IMPORTS
        # - CALLS
        # - REFERENCES
        # - INHERITS
        # - IMPLEMENTS
        # --------------------------------------------------

        return graph