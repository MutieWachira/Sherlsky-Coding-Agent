from pathlib import Path

from compiler.uast.nodes import (
    Language,
    NodeKind,
    SourceLocation,
    UASTNode,
)


def test_add_child():

    root = UASTNode(
        id="1",
        kind=NodeKind.MODULE,
        language=Language.PYTHON,
        location=SourceLocation(
            Path("main.py"),
            1,
            0,
            1,
            10,
        ),
    )

    child = UASTNode(
        id="2",
        kind=NodeKind.DECLARATION,
        language=Language.PYTHON,
        location=SourceLocation(
            Path("main.py"),
            2,
            0,
            2,
            10,
        ),
    )

    root.add_child(child)

    assert child.parent == root

    assert len(root.children) == 1


def test_depth():

    root = UASTNode(
        "1",
        NodeKind.MODULE,
        Language.PYTHON,
        SourceLocation(Path("a.py"), 1, 0, 1, 1),
    )

    child = UASTNode(
        "2",
        NodeKind.DECLARATION,
        Language.PYTHON,
        SourceLocation(Path("a.py"), 2, 0, 2, 1),
    )

    root.add_child(child)

    assert child.depth == 1


def test_walk():

    root = UASTNode(
        "1",
        NodeKind.MODULE,
        Language.PYTHON,
        SourceLocation(Path("a.py"), 1, 0, 1, 1),
    )

    child = UASTNode(
        "2",
        NodeKind.DECLARATION,
        Language.PYTHON,
        SourceLocation(Path("a.py"), 2, 0, 2, 1),
    )

    root.add_child(child)

    nodes = list(root.walk())

    assert len(nodes) == 2
