from pathlib import Path

from app.index.models import ProjectIndex
from app.index.scanner import ProjectScanner
from app.language.manager import LanguageManager
from app.language.symbols import SymbolExtractor


class ProjectIndexer:
    """
    Creates a project-wide symbol index.
    """

    def __init__(self):
        self.scanner = ProjectScanner()
        self.languages = LanguageManager()
        self.extractor = SymbolExtractor()

    def build(self, project_root: Path):

        index = ProjectIndex()

        for file in self.scanner.scan(project_root):

            service = self.languages.registry.get_service(file.suffix)

            if service is None:
                continue

            tree = service.parse(file)

            symbols = self.extractor.extract(tree, file)

            for symbol in symbols:
                index.add(symbol)

        return index