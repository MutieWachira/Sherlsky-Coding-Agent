"""
Document cache.

Keeps parsed documents in memory.
"""

from pathlib import Path

from app.document.document import Document


class DocumentCache:

    def __init__(self):

        self._documents: dict[Path, Document] = {}

    def add(
        self,
        document: Document,
    ):

        self._documents[
            document.path
        ] = document

    def get(
        self,
        path: Path,
    ):

        return self._documents.get(path)

    def all(self):

        return list(
            self._documents.values()
        )

    def clear(self):

        self._documents.clear()

    def remove(
        self,
        path: Path,
    ):

        self._documents.pop(
            path,
            None,
        )