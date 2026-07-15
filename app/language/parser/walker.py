"""
AST Walker.

Traverses a Tree-sitter AST while preserving ancestry.
"""

from dataclasses import dataclass

from tree_sitter import Node


@dataclass(slots=True)
class ASTContext:
    """
    Context for every visited node.
    """

    node: Node
    parent: Node | None
    ancestors: tuple[Node, ...]
    depth: int


class ASTWalker:
    """
    Depth-first AST traversal.
    """

    def walk(
        self,
        node: Node,
        parent: Node | None = None,
        ancestors: tuple[Node, ...] = (),
    ):
        """
        Yield every node together with its traversal context.
        """

        yield ASTContext(
            node=node,
            parent=parent,
            ancestors=ancestors,
            depth=len(ancestors),
        )

        new_ancestors = ancestors + (node,)

        for child in node.children:
            yield from self.walk(
                child,
                node,
                new_ancestors,
            )