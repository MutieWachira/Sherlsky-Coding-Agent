from pathlib import Path

from compiler.document.manager import DocumentManager

manager = DocumentManager()

document = manager.open(Path("examples/sample.py"))

print()

print("Document")
print("----------------")

print(document.path)

print()

print("Symbols")
print("----------------")

for symbol in document.symbols:
    print(symbol)

print()

print("Diagnostics")
print("----------------")

for diagnostic in document.diagnostics:
    print(diagnostic)
