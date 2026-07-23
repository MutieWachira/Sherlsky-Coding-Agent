"""
Universal Abstract Syntax Tree (UAST).

Every language supported by Forge is converted into this representation.

Examples
--------
Python

    class User:

becomes

    ClassDeclaration

TypeScript

    class User {}

also becomes

    ClassDeclaration

The semantic engine never works directly with Tree-sitter.
Instead it consumes the language-independent UAST.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any

# ============================================================
# Source Location
# ============================================================


@dataclass(slots=True, frozen=True)
class SourceLocation:
    """
    Represents where a node exists in source code.
    """

    file: Path

    start_line: int
    start_column: int

    end_line: int
    end_column: int


# ============================================================
# Languages
# ============================================================


class Language(Enum):
    """
    Languages supported by Forge.
    """

    PYTHON = "python"

    TYPESCRIPT = "typescript"

    JAVASCRIPT = "javascript"

    CPP = "cpp"

    CSHARP = "csharp"

    KOTLIN = "kotlin"

    JAVA = "java"

    GO = "go"

    RUST = "rust"


# ============================================================
# Node Kinds
# ============================================================


class NodeKind(Enum):
    """
    Base kinds understood by every language.
    """

    MODULE = "module"

    DECLARATION = "declaration"

    STATEMENT = "statement"

    EXPRESSION = "expression"

    TYPE = "type"

    COMMENT = "comment"

    UNKNOWN = "unknown"


# ============================================================
# Base UAST Node
# ============================================================


@dataclass(slots=True)
class UASTNode:
    """
    Base class for every node in the Universal AST.

    Every language-specific construct inherits from this.

    Children are language-independent.
    """

    id: str

    kind: NodeKind

    language: Language

    location: SourceLocation

    parent: "UASTNode | None" = None

    children: list["UASTNode"] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    # --------------------------------------------------------

    def add_child(self, child: "UASTNode") -> None:
        """
        Adds a child to this node.
        """

        child.parent = self

        self.children.append(child)

    # --------------------------------------------------------

    def walk(self):
        """
        Depth-first traversal.

        Yields every descendant.
        """

        yield self

        for child in self.children:
            yield from child.walk()

    # --------------------------------------------------------

    def find(self, kind: NodeKind):
        """
        Returns every node matching a kind.
        """

        return [node for node in self.walk() if node.kind == kind]

    # --------------------------------------------------------

    @property
    def depth(self) -> int:
        """
        Calculates node depth.
        """

        depth = 0

        current = self.parent

        while current:
            depth += 1

            current = current.parent

        return depth

    # --------------------------------------------------------

    @property
    def root(self):

        node = self

        while node.parent:
            node = node.parent

        return node

    # --------------------------------------------------------

    def pretty(self, indent: int = 0):

        prefix = "    " * indent

        print(f"{prefix}{self.kind.value}")

        for child in self.children:
            child.pretty(indent + 1)
