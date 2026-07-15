from pathlib import Path

from app.language.parser.adapter import TreeSitterAdapter
from app.language.parser.walker import ASTWalker

parser = TreeSitterAdapter("python")

tree = parser.parse(Path("examples/sample.py"))

walker = ASTWalker()


def print_tree(node, level=0):
    print(" " * level + node.type)

    for child in node.children:
        print_tree(child, level + 2)


print_tree(tree.root_node)