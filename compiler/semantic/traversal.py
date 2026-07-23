"""
Semantic traversal utilities.

Maintains traversal state while walking the AST or
semantic graph.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from compiler.semantic.scope import Scope


@dataclass(slots=True)
class TraversalState:
    """
    Current semantic traversal state.

    Used by:

    - Binder
    - ScopeBuilder
    - ReferenceResolver
    - GraphBuilder
    """

    current_scope: Scope | None = None

    scope_stack: list[Scope] = field(default_factory=list)

    depth: int = 0

    # ---------------------------------------------------------

    def push(self, scope: Scope):

        self.scope_stack.append(scope)

        self.current_scope = scope

        self.depth += 1

    # ---------------------------------------------------------

    def pop(self):

        if not self.scope_stack:
            return None

        scope = self.scope_stack.pop()

        self.depth -= 1

        self.current_scope = (
            self.scope_stack[-1]
            if self.scope_stack
            else None
        )

        return scope

    # ---------------------------------------------------------

    @property
    def root(self):

        if not self.scope_stack:
            return None

        return self.scope_stack[0]