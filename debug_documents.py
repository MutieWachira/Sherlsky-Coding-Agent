from pathlib import Path

from app.index.indexer import ProjectIndexer

indexer = ProjectIndexer()

indexer.build(Path("examples"))

print("=== Documents ===")

for document in indexer.documents.documents():

    print()

    print(document.path.name)

    print(f"Version : {document.version}")

    print(f"Symbols : {len(document.symbols)}")

    for symbol in document.symbols:

        print(f"  {symbol.kind.value:10} {symbol.name}")