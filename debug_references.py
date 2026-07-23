from pathlib import Path

from compiler.document.manager import DocumentManager

manager = DocumentManager()

document = manager.open(Path("examples/sample.py"))

print()

print("References")

print("----------------")

for reference in document.references:
    print(
        reference.identifier,
        "->",
        reference.target.name,
    )
