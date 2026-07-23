from compiler.semantic.environment import SemanticEnvironment
from compiler.semantic.inference import TypeInferenceEngine
from compiler.semantic.types import INT


def test_environment_define():

    env = SemanticEnvironment()

    env.define("x", INT)

    assert env.lookup("x") == INT


def test_environment_scope():

    env = SemanticEnvironment()

    env.define("x", INT)

    env.push()

    assert env.lookup("x") == INT

    env.pop()

    assert env.lookup("x") == INT


def test_engine_creation():

    engine = TypeInferenceEngine()

    assert engine.environment is not None
