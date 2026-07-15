from pathlib import Path

from app.index.indexer import ProjectIndexer

index = ProjectIndexer().build(
    Path("examples")
)

print("\nAll Symbols")
print("=" * 50)

for symbol in index.all():
    print(
        symbol.kind,
        symbol.name,
        symbol.parent,
    )

print("\nMethods")
print("=" * 50)

for method in index.methods():
    print(method.name)