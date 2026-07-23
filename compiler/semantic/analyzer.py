from __future__ import annotations

from dataclasses import dataclass, field

from compiler.document.document import Document
from compiler.parser.extractor import SymbolExtractor
from compiler.semantic.binder import SemanticBinder
from compiler.semantic.inference import TypeInferenceEngine


@dataclass(slots=True)
class SemanticAnalysis:
    """
    Result of semantic analysis.
    """

    document: Document

    scope: object | None = None

    scopes: list = field(default_factory=list)

    symbols: list = field(default_factory=list)

    references: list = field(default_factory=list)

    diagnostics: list = field(default_factory=list)

    calls: dict = field(default_factory=dict)


class SemanticAnalyzer:

    def __init__(self):

        self.extractor = SymbolExtractor()

        self.binder = SemanticBinder()

        self.inferencer = TypeInferenceEngine()

    def analyze(
        self,
        document: Document,
    ) -> SemanticAnalysis:

        document.symbols = self.extractor.extract(document)

        scope = self.binder.bind(document)

        self.inferencer.infer(
            document.tree.root_node
        )

        analysis = SemanticAnalysis(
            document=document,
            scope=scope,
            scopes=[scope],
            symbols=document.symbols,
            references=document.references,
            diagnostics=document.diagnostics,
            calls={
                "module": [],
            },
        )

        return analysis