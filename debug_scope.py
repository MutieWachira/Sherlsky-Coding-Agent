from pathlib import Path

from app.language.models import (
    Symbol,
    SymbolKind,
    Location,
)

from app.reference.scope import Scope

root = Scope("global")

root.add_symbol(

    Symbol(

        name="authenticate",

        kind=SymbolKind.FUNCTION,

        location=Location(

            Path("sample.py"),

            1,

            0,

        ),

    )

)

function = Scope("login")

root.add_child(function)

print()

print("Global Scope")

print("----------------")

for symbol in root.symbols.values():

    print(symbol.name)

print()

print("Function Scope")

print("----------------")

print(function.resolve("authenticate"))