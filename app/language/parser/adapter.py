"""
Tree-sitter adapter.

This is the ONLY place in Forge that directly interacts with
Tree-sitter. Keeping it isolated means we can swap parsers
in the future without affecting the rest of the application.
"""

from pathlib import Path

from tree_sitter import Parser
from tree_sitter_language_pack import get_language


class TreeSitterAdapter:
    """
    Wraps Tree-sitter behind a simple interface.
    """

    def __init__(self, language_name: str):
        """
        Create a parser for the specified language.

        Example:
            TreeSitterAdapter("python")
        """

        self.language_name = language_name

        self.parser = Parser()

        language = get_language(language_name)

        self.parser.language = language

    def parse(self, file: Path):
        """
        Parse a source code file.

        Returns
        -------
        tree_sitter.Tree
        """

        source = file.read_text(
            encoding="utf-8"
        )

        tree = self.parser.parse(
            bytes(source, "utf-8")
        )

        return tree