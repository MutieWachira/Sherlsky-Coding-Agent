from pathlib import Path
import pytest

from compiler.document.manager import DocumentManager
from compiler.reference.builder import ScopeBuilder, Scope
from compiler.uast.language.models import SymbolKind


def test_build_scope_tree_hierarchy(tmp_path: Path):
    sample_code = """
class UserService:
    def login(self, username):
        pass

def top_level_func():
    pass
"""
    file_path = tmp_path / "sample.py"
    file_path.write_text(sample_code)

    manager = DocumentManager()
    doc = manager.open(file_path)

    builder = ScopeBuilder()
    root_scope = builder.build(doc)

    assert root_scope.kind == SymbolKind.MODULE
    assert len(root_scope.children) == 2

    # Verify Class Scope
    class_scope = next((s for s in root_scope.children if s.name == "UserService"), None)
    assert class_scope is not None
    assert class_scope.kind == SymbolKind.CLASS
    assert class_scope.parent == root_scope

    # Verify Method Scope nested inside Class Scope
    method_scope = next((s for s in class_scope.children if s.name == "login"), None)
    assert method_scope is not None
    assert method_scope.kind == SymbolKind.METHOD  # <--- Changed from SymbolKind.FUNCTION
    assert method_scope.parent == class_scope

    # Verify Top-Level Function Scope
    func_scope = next((s for s in root_scope.children if s.name == "top_level_func"), None)
    assert func_scope is not None
    assert func_scope.kind == SymbolKind.FUNCTION
    assert func_scope.parent == root_scope


def test_scope_lookup():
    root = Scope(name="module", kind=SymbolKind.MODULE)
    child = Scope(name="fn", kind=SymbolKind.FUNCTION)
    root.add_child(child)

    class DummySymbol:
        def __init__(self, name):
            self.name = name

    sym = DummySymbol("my_var")
    root.symbols=sym

    # Lexical search from child scope up to root
    found_scope = child.lookup("my_var")
    assert found_scope == root