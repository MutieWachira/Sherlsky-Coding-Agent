"""
Semantic Type System

Defines every type understood by Sherlsky.
This layer is language independent.
"""

from __future__ import annotations
from dataclasses import dataclass, field


# ---------------------------------------------------------
# Base Type
# ---------------------------------------------------------
@dataclass(slots=True)
class Type:
    name: str

    def __str__(self):
        return self.name


# ---------------------------------------------------------
# Primitive Types
# ---------------------------------------------------------
class PrimitiveType(Type):
    pass


INT = PrimitiveType("int")
FLOAT = PrimitiveType("float")
BOOL = PrimitiveType("bool")
STRING = PrimitiveType("str")
NONE = PrimitiveType("None")
UNKNOWN = PrimitiveType("unknown")
FUNCTION = PrimitiveType("function")
CLASS = PrimitiveType("class")
MODULE = PrimitiveType("module")

# ---------------------------------------------------------
# Function Type
# ---------------------------------------------------------


@dataclass(slots=True)
class FunctionType(Type):
    parameters: list[Type] = field(default_factory=list)

    returns: Type = field(default_factory=lambda: UNKNOWN)


# ---------------------------------------------------------
# Class Type
# ---------------------------------------------------------


@dataclass(slots=True)
class ClassType(Type):
    methods: dict[str, FunctionType] = field(default_factory=dict)

    fields: dict[str, Type] = field(default_factory=dict)

    bases: list["ClassType"] = field(default_factory=list)


# ---------------------------------------------------------
# Module Type
# ---------------------------------------------------------


@dataclass(slots=True)
class ModuleType(Type):
    symbols: dict[str, Type] = field(default_factory=dict)


# ---------------------------------------------------------
# Container Types
# ---------------------------------------------------------


@dataclass(slots=True)
class ListType(Type):
    element: Type = field(default_factory=lambda: UNKNOWN)


@dataclass(slots=True)
class DictType(Type):
    key: Type = field(default_factory=lambda: UNKNOWN)
    value: Type = field(default_factory=lambda: UNKNOWN)


@dataclass(slots=True)
class TupleType(Type):
    elements: list[Type] = field(default_factory=list)


# ---------------------------------------------------------
# Optional
# ---------------------------------------------------------


@dataclass(slots=True)
class OptionalType(Type):
    wrapped: Type = field(default_factory=lambda: UNKNOWN)


# ---------------------------------------------------------
# Union
# ---------------------------------------------------------


@dataclass(slots=True)
class UnionType(Type):
    options: list[Type] = field(default_factory=list)


# ---------------------------------------------------------
# Named Type
# ---------------------------------------------------------


@dataclass(slots=True)
class NamedType(Type):
    """
    Represents user-defined types.

    Examples

        User
        Product
        Customer
        Database
    """

    pass
