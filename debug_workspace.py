from pathlib import Path

from compiler.workspace.indexer import WorkspaceIndexer

indexer = WorkspaceIndexer()

document = indexer.index_file(Path("examples/sample.py"))

print()

print("=" * 60)
print("Indexed Document")
print("=" * 60)

print(document.path)

print()

print("Extracted Symbols")

for symbol in document.symbols:
    print(
        symbol.kind.name,
        symbol.name,
    )

print()

print("=" * 60)
print("Global Symbol Table")
print("=" * 60)

for symbol in indexer.symbols.all():
    print(
        symbol.kind.name,
        symbol.name,
    )

print()

print("Lookup(login)")

for symbol in indexer.lookup("login"):
    print(symbol)
