from pathlib import Path

from compiler.workspace.indexer import WorkspaceIndexer

indexer = WorkspaceIndexer()

document = indexer.index_file(Path("examples/sample.py"))

print()

print("Symbols")
print("----------------")

for symbol in document.symbols:
    print(symbol.kind.name, symbol.name)

print()

print("References")
print("----------------")

for ref in document.references:
    print(
        ref.identifier,
        "->",
        ref.target.name,
    )
