from pathlib import Path

from compiler.document.manager import DocumentManager
from compiler.parser.walker import ASTWalker
from compiler.parser.walker import WalkEvent


def test_enter_leave_balance():

    doc = DocumentManager().open(Path("examples/sample.py"))

    walker = ASTWalker()

    enters = 0
    leaves = 0

    for event in walker.walk_events(doc.tree.root_node):
        if event.event == WalkEvent.ENTER:
            enters += 1

        else:
            leaves += 1

    assert enters == leaves
