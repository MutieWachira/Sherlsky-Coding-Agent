from pathlib import Path

from app.language.services.python import PythonService

def test_python_service_parse():
    service = PythonService()
    tree = service.parse(Path("examples/sample.py"))
   
    assert tree is not None

    assert tree.root_node.type == "module"

def test_returns_tree():

    service = PythonService()

    tree = service.parse(
        Path("examples/sample.py")
    )

    from tree_sitter import Tree

    assert isinstance(
        tree,
        Tree,
    )