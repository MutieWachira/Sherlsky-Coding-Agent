"""
code Indexer

Responsible for building a searchable index of every symbol inside the project
"""

from app.indexer.models import FileIndex

class CodeIndexer:
    def __init__(self):
        self.index = []

    def add(self, file_index:FileIndex):
        """
        Add a parsed file to the index
        """
        self.index.append(file_index)

    def total_files(self):
        return len(self.index)