from compiler.semantic.literal import LiteralInferencer
from compiler.semantic.types import INT


class FakeNode:
    def __init__(self, type_):

        self.type = type_


def test_integer():

    node = FakeNode("integer")

    assert LiteralInferencer.infer(node) == INT
