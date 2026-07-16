"""
Project Indexer.

Builds the semantic index using cached Documents.
"""

from pathlib import Path

from app.document.manager import DocumentManager
from app.index.models import ProjectIndex
from app.index.scanner import ProjectScanner
from app.language.symbols import SymbolExtractor


class ProjectIndexer:

    def __init__(self):

        self.scanner = ProjectScanner()

        self.documents = DocumentManager()

        self.extractor = SymbolExtractor()

    def build(self, project_root: Path):

        index = ProjectIndex()

        for file in self.scanner.scan(project_root):

            document = self.documents.open(file)

            symbols = self.extractor.extract(document)

            document.symbols = symbols

            index.documents.append(document)

            for symbol in symbols:

                index.add(symbol)

        return index