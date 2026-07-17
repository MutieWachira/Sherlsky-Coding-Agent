from pathlib import Path

from app.document.manager import DocumentManager
from app.semantic.pipeline import SemanticPipeline

manager = DocumentManager()
document = manager.open(Path("examples/sample.py"))

pipeline = SemanticPipeline()
analysis = pipeline.analyze(document)

print("Semantic Analysis")
print("-----------------")
print(f"Symbols    : {len(analysis.symbols)}")
print(f"Scopes     : {len(analysis.scopes)}")
print(f"References : {len(analysis.references)}")
print(f"Calls      : {len(analysis.calls)}")