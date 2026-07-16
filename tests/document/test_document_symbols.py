from pathlib import Path

from app.document.manager import DocumentManager
from app.language.symbols import SymbolExtractor


def test_document_stores_symbols():

    manager = DocumentManager()

    extractor = SymbolExtractor()

    document = manager.open(
        Path("examples/sample.py")
    )

    document.symbols = extractor.extract(document)

    assert len(document.symbols) > 0