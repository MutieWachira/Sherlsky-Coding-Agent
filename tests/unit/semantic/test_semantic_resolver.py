from pathlib import Path

from compiler.document.manager import DocumentManager


def test_reference_pipeline():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    assert document.references is not None
