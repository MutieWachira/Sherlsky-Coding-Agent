"""
Workspace Indexer.

Responsible for building and maintaining the semantic
index for an entire project.

Pipeline

Files
   │
   ▼
DocumentLoader
   │
   ▼
Tree-sitter Parser
   │
   ▼
SymbolExtractor
   │
   ▼
SemanticBinder
   │
   ▼
SymbolTable
"""

from __future__ import annotations

from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.symbol_table import SymbolTable
from compiler.reference.resolver import ReferenceResolver
from compiler.semantic.analyzer import SemanticAnalyzer


class WorkspaceIndexer:
    def __init__(self):

        self.documents = DocumentManager()

        self.analyzer = SemanticAnalyzer()

        self.symbols = SymbolTable()

        self.resolver = ReferenceResolver(self.symbols)

    # ---------------------------------------------------------

    def index_file(
        self,
        path: Path,
    ):

        document = self.documents.open(path)

        self.analyzer.analyze(document)

        self.symbols.add_many(document.symbols)

        document.references = self.resolver.resolve_document(document)

        return document

    # ---------------------------------------------------------

    def index_directory(
        self,
        root: Path,
    ):

        for file in root.rglob("*"):
            if file.suffix == ".py":
                self.index_file(file)

    # ---------------------------------------------------------

    def lookup(
        self,
        name: str,
    ):

        return self.symbols.lookup(name)

    # ---------------------------------------------------------

    def clear(self):

        self.symbols.clear()

        self.documents.clear()
