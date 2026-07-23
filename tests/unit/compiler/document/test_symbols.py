from pathlib import Path

from compiler.uast.language.symbols import SymbolExtractor
from compiler.document.manager import DocumentManager


def test_symbol_extraction():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    extractor = SymbolExtractor()

    symbols = extractor.extract(document)

    names = {symbol.name for symbol in symbols}

    assert "UserService" in names

    assert "login" in names

    assert "hello" in names

    assert "math" in names
