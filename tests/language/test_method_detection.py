from pathlib import Path

from app.language.parser.adapter import TreeSitterAdapter
from app.language.symbols import SymbolExtractor
from app.language.models import SymbolKind
from app.document.manager import DocumentManager


def test_global_function_is_not_method():

    manager = DocumentManager()

    document = manager.open(
        Path("examples/sample.py")
    )


    extractor = SymbolExtractor()

    symbols = extractor.extract(
    document
    )

    hello = next(
        symbol
        for symbol in symbols
        if symbol.name == "hello"
    )

    assert hello.kind == SymbolKind.FUNCTION
    assert hello.parent is None