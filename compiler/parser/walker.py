"""
AST Walker.

Traverses a Tree-sitter AST while preserving ancestry.

Provides two traversal APIs:

1. walk()
   Returns raw Tree-sitter Node objects.
   This preserves backwards compatibility with older code.

2. walk_context()
   Returns ASTContext objects containing ancestry information.
   This is the API used by Forge's semantic analysis engine.
"""

from dataclasses import dataclass
from enum import Enum, auto
from tree_sitter import Node


class WalkEvent(Enum):
    ENTER = auto()
    LEAVE = auto()


@dataclass(slots=True)
class ASTContext:
    """
    Context for every visited node.
    """

    node: Node
    parent: Node | None
    ancestors: tuple[Node, ...]
    depth: int


@dataclass(slots=True)
class ASTEvent:
    event: WalkEvent
    node: Node
    parent: Node | None
    ancestors: tuple[Node, ...]
    depth: int


class ASTWalker:
    """
    Depth-first Tree-sitter AST traversal.
    """

    # ---------------------------------------------------------
    # Public API (Backwards Compatible)
    # ---------------------------------------------------------
    def walk(self, node: Node):
        """
        Yield raw Tree-sitter nodes.

        This preserves compatibility with older tests and
        existing code that expects `Node` objects.
        """
        yield node
        for child in node.children:
            yield from self.walk(child)

    # ---------------------------------------------------------
    # New Semantic API
    # ---------------------------------------------------------

    def walk_context(
        self,
        node: Node,
        parent: Node | None = None,
        ancestors: tuple[Node, ...] = (),
    ):
        """
        Yield ASTContext objects.

        This is the traversal used by the semantic analyzer,
        symbol extractor, and future call graph builder.
        """

        yield ASTContext(
            node=node,
            parent=parent,
            ancestors=ancestors,
            depth=len(ancestors),
        )

        new_ancestors = ancestors + (node,)

        for child in node.children:
            yield from self.walk_context(
                child,
                node,
                new_ancestors,
            )

    def walk_events(
        self,
        node: Node,
        parent: Node | None = None,
        ancestors: tuple[Node, ...] = (),
    ):

        yield ASTEvent(
            event=WalkEvent.ENTER,
            node=node,
            parent=parent,
            ancestors=ancestors,
            depth=len(ancestors),
        )

        new_ancestors = ancestors + (node,)

        for child in node.children:
            yield from self.walk_events(
                child,
                node,
                new_ancestors,
            )

        yield ASTEvent(
            event=WalkEvent.LEAVE,
            node=node,
            parent=parent,
            ancestors=ancestors,
            depth=len(ancestors),
        )