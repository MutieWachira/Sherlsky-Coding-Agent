from pathlib import Path

from compiler.parser.adapter import TreeSitterAdapter
from compiler.parser.walker import ASTWalker

parser = TreeSitterAdapter("python")
tree = parser.parse(Path("examples/sample.py"))

walker = ASTWalker()

for node in walker.walk(tree.root_node):
    print(node.type)
