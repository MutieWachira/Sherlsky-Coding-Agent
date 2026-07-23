"""
Semantic Analyzer.

Runs the complete semantic pipeline for a document.

Pipeline

Tree
 ↓
Symbol Extraction
 ↓
Binding
 ↓
Type Inference
 ↓
Diagnostics
"""

from __future__ import annotations

from compiler.document.document import Document

from compiler.parser.extractor import SymbolExtractor
from compiler.semantic.binder import SemanticBinder
from compiler.semantic.inference import TypeInferenceEngine

"""
    High-level semantic pipeline.

    Every opened document should pass through here.
"""


class SemanticAnalyzer:
    def __init__(self):

        self.extractor = SymbolExtractor()

        self.binder = SemanticBinder()

        self.inferencer = TypeInferenceEngine()

    def analyze(self,document: Document,):

        #
        # STEP 1
        #
        document.symbols = self.extractor.extract(document)

        #
        # STEP 2
        #
        document.scope = self.binder.bind(document)

        #
        # STEP 3
        #
        self.inferencer.infer(document.tree.root_node)

        return document.scope
