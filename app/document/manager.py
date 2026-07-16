"""
Document Manager.

Responsible for loading and caching Documents.
"""

from pathlib import Path

from app.document.cache import DocumentCache
from app.document.loader import DocumentLoader


class DocumentManager:

    def __init__(self):

        self.loader = DocumentLoader()

        self.cache = DocumentCache()

    def open(
        self,
        path: Path,
    ):

        document = self.cache.get(path)

        if document:

            return document

        document = self.loader.load(path)

        self.cache.add(document)

        return document

    def close(
        self,
        path: Path,
    ):

        self.cache.remove(path)

    def documents(self):

        return self.cache.all()

    def clear(self):

        self.cache.clear()