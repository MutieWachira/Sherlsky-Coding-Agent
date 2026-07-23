from pathlib import Path

from compiler.document.manager import DocumentManager

manager = DocumentManager()

document = manager.open(Path("examples/sample.py"))

print()

print("SYMBOLS")

print("-------")

for symbol in document.symbols:
    print(
        symbol.kind.value,
        symbol.name,
        symbol.parent,
    )
