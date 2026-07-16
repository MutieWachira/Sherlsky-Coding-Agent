"""
Call Graph Builder.

Creates CALLS relationships between functions and methods by
walking the Tree-sitter AST stored inside each Document.
"""

from app.graph.models import Relationship
from app.graph.relationships import RelationshipType
from app.graph.resolver import CallResolver
from app.language.parser.walker import ASTWalker


class CallGraphBuilder:
    """
    Builds CALLS relationships for a document.
    """

    def __init__(self):
        """
        Initialize helpers.
        """
        self.walker = ASTWalker()
        self.resolver = CallResolver()

    def build(
        self,
        document,
        graph,
        index,
    ):
        """
        Build every CALLS relationship inside one document.

        Parameters
        ----------
        document : Document
            Parsed document.

        graph : KnowledgeGraph
            Graph being constructed.

        index : ProjectIndex
            Used for resolving function names.
        """

        #
        # Safety check.
        #
        if document.tree is None:
            return

        #
        # Walk every node in the syntax tree.
        #
        for node in self.walker.walk(document.tree.root_node):

            #
            # Interested only in function definitions.
            #
            if node.type not in (
                "function_definition",
                "method_definition",
            ):
                continue

            #
            # Find the Symbol that owns this AST node.
            #
            source_symbol = self._find_symbol(
                document,
                node,
            )

            if source_symbol is None:
                continue

            #
            # Walk only inside this function.
            #
            self._build_calls(
                node,
                source_symbol,
                graph,
                index,
            )

    def _build_calls(
        self,
        function_node,
        source_symbol,
        graph,
        index,
    ):
        """
        Scan one function body for calls.
        """

        for node in self.walker.walk(function_node):

            #
            # Skip non-call nodes.
            #
            if node.type != "call":
                continue

            function = node.child_by_field_name(
                "function"
            )

            if function is None:
                continue

            #
            # Ignore attribute calls for now.
            #
            if function.type != "identifier":
                continue

            target = self.resolver.resolve(
                function.text.decode(),
                index,
            )

            if target is None:
                continue

            graph.add_edge(
                Relationship.create(
                    source=source_symbol.id,
                    target=target.id,
                    relation=RelationshipType.CALLS,
                )
            )

    def _find_symbol(
        self,
        document,
        node,
    ):
        """
        Return the Symbol represented by a function AST node.
        """

        #
        # Tree-sitter lines are zero-based.
        #
        line = node.start_point[0] + 1

        for symbol in document.symbols:

            if symbol.location.line != line:
                continue

            if symbol.kind.name not in (
                "FUNCTION",
                "METHOD",
            ):
                continue

            return symbol

        return None