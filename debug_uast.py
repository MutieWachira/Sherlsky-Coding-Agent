from pathlib import Path

from compiler.uast.nodes import (
    Language,
    NodeKind,
    SourceLocation,
    UASTNode,
)

root = UASTNode(
    "module",
    NodeKind.MODULE,
    Language.PYTHON,
    SourceLocation(Path("sample.py"), 1, 0, 1, 1),
)

child = UASTNode(
    "class",
    NodeKind.DECLARATION,
    Language.PYTHON,
    SourceLocation(Path("sample.py"), 2, 0, 10, 0),
)

root.add_child(child)

root.pretty()
