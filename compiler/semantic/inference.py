"""
Type Inference Engine.

Infers types from the AST.

Current supported:

✓ literals
✓ assignments
✓ variable references
✓ binary operators
✓ function definitions
✓ return statements

Future:

- function calls
- imports
- member access
- generic types
- class inference
- lambda inference
"""

from __future__ import annotations

from tree_sitter import Node

from compiler.semantic.environment import SemanticEnvironment
from compiler.semantic.types import (
    BOOL,
    FLOAT,
    FunctionType,
    INT,
    NONE,
    STRING,
    Type,
    UNKNOWN,
)


class TypeInferenceEngine:
    def __init__(self):

        self.environment = SemanticEnvironment()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def infer(
        self,
        node: Node,
    ) -> Type:

        method = getattr(
            self,
            f"infer_{node.type}",
            self.infer_default,
        )

        return method(node)

    # ---------------------------------------------------------
    # Default
    # ---------------------------------------------------------

    def infer_default(
        self,
        node: Node,
    ) -> Type:

        for child in node.children:
            self.infer(child)

        return UNKNOWN

    # ---------------------------------------------------------
    # Integer
    # ---------------------------------------------------------

    def infer_integer(
        self,
        node: Node,
    ):

        return INT

    # ---------------------------------------------------------
    # Float
    # ---------------------------------------------------------

    def infer_float(
        self,
        node: Node,
    ):

        return FLOAT

    # ---------------------------------------------------------
    # String
    # ---------------------------------------------------------

    def infer_string(
        self,
        node: Node,
    ):

        return STRING

    # ---------------------------------------------------------
    # True / False
    # ---------------------------------------------------------

    def infer_true(
        self,
        node,
    ):

        return BOOL

    def infer_false(
        self,
        node,
    ):

        return BOOL

    # ---------------------------------------------------------
    # None
    # ---------------------------------------------------------

    def infer_none(
        self,
        node,
    ):

        return NONE

    # ---------------------------------------------------------
    # Identifier
    # ---------------------------------------------------------

    def infer_identifier(
        self,
        node,
    ):

        name = node.text.decode()

        symbol = self.environment.lookup(name)

        if symbol:
            return symbol

        return UNKNOWN

    # ---------------------------------------------------------
    # Assignment
    # ---------------------------------------------------------

    def infer_assignment(
        self,
        node,
    ):

        left = node.child_by_field_name("left")

        right = node.child_by_field_name("right")

        if left is None or right is None:
            return UNKNOWN

        inferred = self.infer(right)

        self.environment.define(
            left.text.decode(),
            inferred,
        )

        return inferred

    # ---------------------------------------------------------
    # Binary operators
    # ---------------------------------------------------------

    def infer_binary_operator(
        self,
        node,
    ):

        left = self.infer(node.children[0])

        right = self.infer(node.children[-1])

        if left == FLOAT or right == FLOAT:
            return FLOAT

        if left == INT and right == INT:
            return INT

        return UNKNOWN

    # ---------------------------------------------------------
    # Function definition
    # ---------------------------------------------------------

    def infer_function_definition(
        self,
        node,
    ):

        name = node.child_by_field_name("name").text.decode()

        function = FunctionType(
            name=name,
            returns=UNKNOWN,
        )

        self.environment.define(
            name,
            function,
        )

        self.environment.push()

        body = node.child_by_field_name("body")

        if body:
            for child in body.children:
                self.infer(child)

        self.environment.pop()

        return function

    # ---------------------------------------------------------
    # Return statement
    # ---------------------------------------------------------

    def infer_return_statement(
        self,
        node,
    ):

        if len(node.children) == 1:
            return NONE

        return self.infer(node.children[-1])
