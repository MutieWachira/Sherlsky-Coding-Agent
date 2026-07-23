from compiler.semantic.scope import Scope
from compiler.semantic.traversal import TraversalState

state = TraversalState()

state.push_scope(Scope("module"))

state.push_scope(Scope("function"))

print()

print("Scope Depth")

print(state.scope_depth)

state.pop_scope()

print(state.scope_depth)
