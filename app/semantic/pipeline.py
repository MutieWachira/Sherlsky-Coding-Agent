"""
Semantic Pipeline.
"""

from app.semantic.analysis import SemanticAnalysis
from app.semantic.context import SemanticContext
from app.semantic.state import SemanticState
from app.semantic.visitor import SemanticVisitor


class SemanticPipeline:
    """
    Entry point for semantic analysis.
    """

    def __init__(self):

        self.visitor = SemanticVisitor()

    def analyze(self, document):
        """
        Perform semantic analysis.
        """

        analysis = SemanticAnalysis()

        context = SemanticContext(
            document=document,
            analysis=analysis,
            state=SemanticState(),
        )

        self.visitor.visit(context)

        return analysis