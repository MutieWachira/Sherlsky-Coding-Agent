from pathlib import Path

from app.index.models import ProjectIndex
from app.index.scanner import ProjectScanner
from compiler.document.manager import DocumentManager


class ProjectIndexer:

    def __init__(self):
        self.by_id = {}
        self.scanner = ProjectScanner()
        self.documents = DocumentManager()

    def build(
        self,
        project_root: Path,
    ) -> ProjectIndex:

        index = ProjectIndex()

        for file in self.scanner.scan(project_root):

            document = self.documents.open(file)

            index.add_document(document)

            index.add_many(document.symbols)

        return index

    def add(self, symbol):

        self._symbols.append(symbol)

        self.by_id[symbol.id] = symbol

        self.by_name[symbol.name].append(symbol)

        self.by_kind[symbol.kind].append(symbol)

        self.by_file[symbol.location.file].append(symbol)

    def get(self,symbol_id,):

        return self.by_id.get(symbol_id)


    def  clear(self):
        self.by_id.clear()