from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.uast.language.symbols import SymbolExtractor


def test_document_stores_symbols():

    manager = DocumentManager()

    extractor = SymbolExtractor()

    document = manager.open(Path("examples/sample.py"))

    document.symbols = extractor.extract(document)

    assert len(document.symbols) > 0
