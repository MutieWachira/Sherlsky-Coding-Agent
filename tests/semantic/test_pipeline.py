from pathlib import Path

from app.document.manager import DocumentManager
from app.semantic.pipeline import SemanticPipeline


def test_pipeline_returns_analysis():

    manager = DocumentManager()

    document = manager.open(
        Path("examples/sample.py")
    )

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert analysis is not None


def test_pipeline_creates_root_scope():

    manager = DocumentManager()

    document = manager.open(
        Path("examples/sample.py")
    )

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert len(analysis.scopes) == 1

    assert analysis.scopes[0].name == "module"


def test_pipeline_walks_ast():

    manager = DocumentManager()

    document = manager.open(
        Path("examples/sample.py")
    )

    pipeline = SemanticPipeline()

    analysis = pipeline.analyze(document)

    assert "module" in analysis.calls

    assert "class_definition" in analysis.calls