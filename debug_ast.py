from pathlib import Path

from app.language.parser.adapter import TreeSitterAdapter
from app.language.parser.walker import ASTWalker

parser = TreeSitterAdapter("python")
tree = parser.parse(Path("examples/sample.py"))

walker = ASTWalker()

for node in walker.walk(tree.root_node):
    print(node.type)