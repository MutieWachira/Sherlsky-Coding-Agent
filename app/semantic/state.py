"""
Semantic analysis state.
"""

from dataclasses import dataclass, field

from app.reference.scope import Scope


class SemanticState:

    def __init__(self):

        self.scope_stack = []

        self.current_class = None

        self.current_function = None

        self.root_node = None

    def add_symbol(self, symbol):

        self.symbols.append(symbol)

    def push_scope(self, scope):

        self.scope_stack.append(scope)

    def pop_scope(self):

        return self.scope_stack.pop()

    @property
    def current_scope(self):

        return self.scope_stack[-1] if self.scope_stack else None