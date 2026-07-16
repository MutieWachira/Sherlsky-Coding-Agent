"""
Knowledge Graph Builder.

Responsible for building every semantic relationship inside the
Knowledge Graph.

Current relationships:
- Class -> Method (OWNS)
- Function -> Function (CALLS)

Future relationships:
- IMPORTS
- REFERENCES
- INHERITS
- IMPLEMENTS
"""

from pathlib import Path

from app.graph.call_builder import CallGraphBuilder
from app.graph.graph import KnowledgeGraph
from app.graph.models import Relationship
from app.graph.relationships import RelationshipType
from app.language.manager import LanguageManager


class GraphBuilder:
    """
    Converts a ProjectIndex into a KnowledgeGraph.
    """

    def __init__(self):
        """
        Initialize helper services.
        """

        self.languages = LanguageManager()

        self.call_builder = CallGraphBuilder()

    def build(self, index):
        """
        Build the complete Knowledge Graph.

        Parameters
        ----------
        index : ProjectIndex

        Returns
        -------
        KnowledgeGraph
        """

        graph = KnowledgeGraph()

        #
        # -------------------------------------------------
        # STEP 1
        # Register every symbol as a graph node.
        # -------------------------------------------------
        #

        for symbol in index.all():

            graph.add_node(symbol)

        #
        # -------------------------------------------------
        # STEP 2
        # Build ownership relationships.
        # -------------------------------------------------
        #

        for method in index.methods():

            if method.parent is None:
                continue

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

        #
        # -------------------------------------------------
        # STEP 3
        # Build call graph.
        # -------------------------------------------------
        #

        analyzed_files = set()

        for function in (
            index.functions()
            + index.methods()
        ):

            file = function.location.file

            #
            # Avoid parsing the same file multiple times.
            #
            if file in analyzed_files:
                continue

            analyzed_files.add(file)

            service = self.languages.registry.get_service(
                file.suffix
            )

            if service is None:
                continue

            tree = service.parse(file)

            self.call_builder.build(

                tree=tree,

                source_file=file,

                graph=graph,

                index=index,

            )

        return graph