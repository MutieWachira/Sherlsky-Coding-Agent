"""
Semantic Environment.

Stores every visible symbol during
semantic analysis.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from compiler.semantic.types import Type


@dataclass(slots=True)
class Scope:
    parent: "Scope | None" = None

    symbols: dict[str, Type] = field(default_factory=dict)

    children: list["Scope"] = field(default_factory=list)

    def define(
        self,
        name: str,
        type_: Type,
    ):

        self.symbols[name] = type_

    def lookup(
        self,
        name: str,
    ) -> Type | None:

        if name in self.symbols:
            return self.symbols[name]

        if self.parent:
            return self.parent.lookup(name)

        return None


class SemanticEnvironment:
    def __init__(self):

        self.root = Scope()

        self.current = self.root

    def push(self):

        scope = Scope(parent=self.current)

        self.current.children.append(scope)

        self.current = scope

    def pop(self):

        if self.current.parent:
            self.current = self.current.parent

    def define(
        self,
        name: str,
        type_: Type,
    ):

        self.current.define(
            name,
            type_,
        )

    def lookup(
        self,
        name: str,
    ):

        return self.current.lookup(name)
