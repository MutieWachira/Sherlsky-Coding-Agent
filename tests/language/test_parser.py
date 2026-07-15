from pathlib import Path

from app.language.parser.adapter import TreeSitterAdapter


def test_parser():

    parser = TreeSitterAdapter("python")

    tree = parser.parse(
        Path("examples/sample.py")
    )

    assert tree is not None

    assert tree.root_node.type == "module"