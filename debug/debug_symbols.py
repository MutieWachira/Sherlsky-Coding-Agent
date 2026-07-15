from pathlib import Path

from app.index.indexer import ProjectIndexer

index = ProjectIndexer().build(Path("examples"))

print("\n=== SYMBOLS ===")

for symbol in index.all():
    print(
        f"{symbol.kind.value:10}"
        f"{symbol.name:20}"
        f"parent={symbol.parent}"
    )