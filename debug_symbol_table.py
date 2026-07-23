from pathlib import Path

from compiler.semantic.symbol_table import SymbolTable
from compiler.uast.language.models import (
    Symbol,
    SymbolKind,
    Location,
)

table = SymbolTable()

symbol = Symbol(
    name="login",
    kind=SymbolKind.FUNCTION,
    location=Location(
        file=Path("sample.py"),
        line=10,
        column=4,
    ),
)

table.add(symbol)

print()

print("Total symbols:", len(table))

print()

print("Lookup login")

for s in table.lookup("login"):
    print(s)

print()

print("By ID")

print(table.get(symbol.id))
