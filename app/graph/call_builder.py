"""
Call Graph Builder.
"""

from app.graph.models import Relationship
from app.graph.relationships import RelationshipType
from app.graph.resolver import CallResolver
from app.language.parser.walker import ASTWalker


class CallGraphBuilder:

    def __init__(self):

        self.walker = ASTWalker()

        self.resolver = CallResolver()

    def build(
        self,
        tree,
        source_symbol,
        graph,
        index,
    ):

        for node in self.walker.walk(
            tree.root_node
        ):

            if node.type != "call":
                continue

            function = node.child_by_field_name(
                "function"
            )

            if function is None:
                continue

            if function.type != "identifier":
                continue

            target = self.resolver.resolve(
                function.text.decode(),
                index,
            )

            if target is None:
                continue

            edge = Relationship.create(
                source_symbol.id,
                target.id,
                RelationshipType.CALLS,
            )

            graph.add_edge(edge)