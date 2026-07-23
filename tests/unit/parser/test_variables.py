from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.uast.language.models import SymbolKind


def test_parameters():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    params = [s for s in document.symbols if s.kind == SymbolKind.PARAMETER]

    assert len(params) > 0


def test_variables():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    variables = [s for s in document.symbols if s.kind == SymbolKind.VARIABLE]

    assert variables is not None
