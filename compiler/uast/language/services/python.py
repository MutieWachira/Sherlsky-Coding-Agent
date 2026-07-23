"""
Python language service.
"""

from pathlib import Path

from compiler.uast.language.base import LanguageService
from compiler.parser.adapter import TreeSitterAdapter


class PythonService(LanguageService):
    """
    Python language implementation.
    """

    language_name = "Python"

    supported_extensions = [".py"]

    def __init__(self):
        self.parser = TreeSitterAdapter("python")

    def parse(self, file: Path):
        """
        Parse a Python source file using Tree-sitter.
        """
        return self.parser.parse(file)

    def find_symbols(self, file: Path):
        """
        Symbol extraction is handled by SymbolExtractor.
        """
        raise NotImplementedError("Use SymbolExtractor instead.")
