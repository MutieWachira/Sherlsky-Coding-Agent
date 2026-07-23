from pathlib import Path

from compiler.document.manager import DocumentManager

manager = DocumentManager()

document = manager.open(Path("examples/sample.py"))

for symbol in document.symbols:
    print(f"{symbol.kind.value:<12}{symbol.name:<20}parent={symbol.parent}")
