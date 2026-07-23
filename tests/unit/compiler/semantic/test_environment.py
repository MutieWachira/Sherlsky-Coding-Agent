from compiler.semantic.environment import SemanticEnvironment
from compiler.semantic.types import INT


def test_define():

    env = SemanticEnvironment()

    env.define(
        "x",
        INT,
    )

    assert env.lookup("x") == INT


def test_nested_scope():

    env = SemanticEnvironment()

    env.define(
        "x",
        INT,
    )

    env.push()

    assert env.lookup("x") == INT

    env.pop()

    assert env.lookup("x") == INT


def test_shadowing():

    env = SemanticEnvironment()

    env.define(
        "x",
        INT,
    )

    env.push()

    env.define(
        "x",
        INT,
    )

    assert env.lookup("x") == INT
