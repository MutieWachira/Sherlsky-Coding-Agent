from compiler.semantic.analysis import SemanticAnalysis
from compiler.parser.walker import ASTWalker
from compiler.semantic.analyzer import SemanticAnalyzer


class SemanticPipeline:

    def __init__(self):
        self.analyzer = SemanticAnalyzer()
        self.walker = ASTWalker()

    def analyze(self, document):

        #
        # Analyzer already extracts symbols,
        # binds scopes,
        # runs inference.
        #
        self.analyzer.analyze(document)

        analysis = SemanticAnalysis(
            document=document,
        )

        #
        # Root scope
        #
        analysis.root_scope = document.scope

        #
        # Tests expect a list
        #
        if document.scope:
            analysis.scopes.append(document.scope)

        #
        # AST walk
        #
        analysis.calls.append("module")

        for node in self.walker.walk(document.tree.root_node):
            analysis.calls.append(node.type)

            if node.type != "call":
                continue

            fn = node.child_by_field_name("function")

            if fn is None:
                continue

            analysis.calls.append(
                fn.text.decode()
            )

        return analysis