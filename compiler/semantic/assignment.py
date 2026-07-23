"""
Assignment inference.

Infers the type of assignment expressions.
"""

from __future__ import annotations

from tree_sitter import Node

from compiler.semantic.literal import LiteralInferencer


class AssignmentInferencer:
    """
    Infers assignment value types.
    """

    def __init__(self):
        self.literal = LiteralInferencer()

    def infer(self, node: Node):
        """
        Infer the type of an assignment node.

        Example:
            x = 123
            x = "hello"
            x = True
        """

        if node.type != "assignment":
            return None

        value = node.child_by_field_name("right")

        if value is None:
            return None

        return self.literal.infer(value)