from compiler.semantic.environment import SemanticEnvironment
from compiler.semantic.types import INT

env = SemanticEnvironment()

env.define("global", INT)

env.push()

env.define("local", INT)

print(env.lookup("global"))
print(env.lookup("local"))

env.pop()

print(env.lookup("global"))
print(env.lookup("local"))
