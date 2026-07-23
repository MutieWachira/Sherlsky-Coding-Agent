from pathlib import Path

from compiler.parser.adapter import TreeSitterAdapter
from compiler.parser.walker import ASTWalker


def test_walk_tree():

    parser = TreeSitterAdapter("python")

    tree = parser.parse(Path("examples/sample.py"))

    walker = ASTWalker()

    nodes = list(walker.walk(tree.root_node))

    assert len(nodes) > 0

    assert nodes[0].type == "module"
