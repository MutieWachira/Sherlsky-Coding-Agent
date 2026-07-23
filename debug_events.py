from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.parser.walker import ASTWalker

doc = DocumentManager().open(Path("examples/sample.py"))

walker = ASTWalker()

for event in walker.walk_events(doc.tree.root_node):
    print(
        event.event.name,
        event.depth,
        event.node.type,
    )
