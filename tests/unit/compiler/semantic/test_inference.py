from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.inference import TypeInferenceEngine
from compiler.semantic.types import FunctionType


def test_infer_document():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    engine = TypeInferenceEngine()

    env = engine.infer_document(document)

    assert env is not None


def test_function_registered():

    manager = DocumentManager()

    document = manager.open(Path("examples/sample.py"))

    env = TypeInferenceEngine().infer_document(document)

    assert any(isinstance(value, FunctionType) for value in env.symbols.values())
