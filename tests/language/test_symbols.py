from pathlib import Path

from app.language.parser.adapter import TreeSitterAdapter
from app.language.symbols import SymbolExtractor


def test_symbol_extraction():

    parser = TreeSitterAdapter("python")

    tree = parser.parse(
        Path("examples/sample.py")
    )

    extractor = SymbolExtractor()

    symbols = extractor.extract(
        tree,
        Path("examples/sample.py"),
    )

    names = {
        symbol.name
        for symbol in symbols
    }

    assert "UserService" in names

    assert "login" in names

    assert "hello" in names

    assert "math" in names
