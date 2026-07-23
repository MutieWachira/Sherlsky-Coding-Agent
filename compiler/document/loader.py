"""
Loads Documents from disk.
"""

from pathlib import Path

from compiler.document.document import Document
from compiler.uast.language.manager import LanguageManager


class DocumentLoader:
    def __init__(self):
        self.languages = LanguageManager()

    def load(
        self,
        path: Path,
    ):

        source = path.read_text(encoding="utf-8")

        service = self.languages.registry.get_service(path.suffix)

        if service is None:
            raise ValueError(f"No language service for {path}")

        tree = service.parse(path)

        return Document(
            path=path,
            source=source,
            tree=tree,
        )
