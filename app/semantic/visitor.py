"""
Semantic Visitor.

Performs a single traversal of the Tree-sitter AST and
dispatches semantic events to specialized visitor methods.

During this traversal the visitor will gradually build the
SemanticAnalysis object by creating symbols, scopes,
references, call graph edges, and diagnostics.

Current Phase
-------------
Phase 2A

Only AST traversal and dispatch are implemented.
Specific node handlers will be implemented in Phase 2B.
"""

from app.language.parser.walker import ASTWalker


class SemanticVisitor:
    """
    Performs one semantic traversal of a document.
    """

    def __init__(self):
        """
        Initialize reusable helpers.
        """

        self.walker = ASTWalker()

    def visit(self, context):
        """
        Analyze one document.

        Parameters
        ----------
        context : SemanticContext
            Shared analysis context containing the
            document, semantic state, and analysis results.

        Returns
        -------
        SemanticAnalysis
            The populated semantic analysis object.
        """

        document = context.document
        tree = document.tree
        root = tree.root_node

        #
        # Store the root node for future semantic passes.
        #
        context.state.root_node = root

        #
        # Walk the entire AST exactly once.
        #
        for node in self.walker.walk(root):
            self._dispatch(node, context)

        #
        # Return the completed analysis.
        #
        return context.analysis

    def _dispatch(self, node, context):
        """
        Dispatch AST nodes to their specialized handlers.
        """

        dispatch_table = {
            "class_definition": self.visit_class,
            "function_definition": self.visit_function,
            "call": self.visit_call,
        }

        handler = dispatch_table.get(node.type)

        if handler is not None:
            handler(node, context)

    def visit_class(self, node, context):
        """
        Handle a class definition.

        Implemented in Phase 2B.
        """
        pass

    def visit_function(self, node, context):
        """
        Handle a function or method definition.

        Implemented in Phase 2B.
        """
        pass

    def visit_call(self, node, context):
        """
        Handle a function or method call.

        Implemented in Phase 2C.
        """
        pass