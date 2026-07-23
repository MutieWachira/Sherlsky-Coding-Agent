from __future__ import annotations

from tree_sitter import Node


class LiteralInferencer:
    """
    Infers the type of literal nodes.
    """

    def infer(self, node: Node):

        match node.type:
            case "integer":
                return "int"

            case "float":
                return "float"

            case "string":
                return "str"

            case "true":
                return "bool"

            case "false":
                return "bool"

            case "none":
                return "None"

            case _:
                return None