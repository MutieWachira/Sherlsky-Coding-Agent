from pathlib import Path

from compiler.uast.language.symbols import SymbolExtractor
from compiler.uast.language.models import SymbolKind
from compiler.document.manager import DocumentManager


def test_global_function_is_not_method():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    extractor = SymbolExtractor()

    symbols = extractor.extract(document)

    hello = next(symbol for symbol in symbols if symbol.name == "hello")

    assert hello.kind == SymbolKind.FUNCTION
    assert hello.parent is None
