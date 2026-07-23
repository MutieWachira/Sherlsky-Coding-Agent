from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.semantic.scope import Scope
from compiler.semantic.analyzer import SemanticAnalysis
from compiler.semantic.state import SemanticState

manager = DocumentManager()

document = manager.open(Path("examples/sample.py"))

state = SemanticState(
    document=document,
    analysis=SemanticAnalysis(),
)

print()

print("Semantic State")

print("----------------")

print("Depth:", state.depth)

root = Scope("module")

state.push_scope(root)

print("Depth:", state.depth)

child = Scope("function")

state.push_scope(child)

print("Depth:", state.depth)

state.pop_scope()

print("Depth:", state.depth)

state.reset()

print("Depth:", state.depth)
