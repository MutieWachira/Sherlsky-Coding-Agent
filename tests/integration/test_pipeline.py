from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.pipeline import SemanticPipeline


def test_pipeline_returns_analysis():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert analysis is not None


def test_pipeline_creates_root_scope():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert analysis.root_scope.kind.name == "MODULE"

    assert analysis.root_scope.name == "sample"


def test_pipeline_walks_ast():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert "module" in analysis.calls

    assert "class_definition" in analysis.calls
