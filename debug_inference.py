from compiler.semantic.environment import SemanticEnvironment
from compiler.semantic.types import INT

env = SemanticEnvironment()

env.define("age", INT)

print()

print("Environment")

print("----------------")

print(env.lookup("age"))

env.push()

print(env.lookup("age"))

env.pop()

print(env.lookup("age"))
