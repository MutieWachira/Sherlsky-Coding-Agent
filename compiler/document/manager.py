"""
Document Manager.

Responsible for loading and caching Documents.
"""

from pathlib import Path

from compiler.document.cache import DocumentCache
from compiler.document.loader import DocumentLoader
from compiler.semantic.analyzer import SemanticAnalyzer


class DocumentManager:
    def __init__(self):

        self.loader = DocumentLoader()

        self.cache = DocumentCache()

        self.semantic = SemanticAnalyzer()

    def open(
        self,
        path: Path,
    ):

        document = self.loader.load(path)

        #
        # Run semantic analysis
        #

        self.semantic.analyze(document)

        self.cache.add(document)

        return document

    def close(
        self,
        path: Path,
    ):

        self.cache.remove(path)

    def documents(self):

        return self.cache.all()

    def clear(self):

        self.cache.clear()
