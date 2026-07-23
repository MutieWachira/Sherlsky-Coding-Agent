from compiler.semantic.assignment import AssignmentInferencer
from compiler.semantic.types import INT


class FakeNode:
    def __init__(self, type_):

        self.type = type_
        self.children = []


def test_assignment():

    value = FakeNode("integer")

    assign = FakeNode("assignment")

    assign.children = [
        FakeNode("identifier"),
        FakeNode("="),
        value,
    ]

    inferred = AssignmentInferencer().infer(assign)

    assert inferred == INT
