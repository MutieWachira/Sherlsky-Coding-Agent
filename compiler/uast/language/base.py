"""
Base interface for all language services

"""

from abc import ABC, abstractmethod
from pathlib import Path


class LanguageService(ABC):
    """
    Every language implementation must inherit this class.
    """

    language_name = "Unknown"
    supported_extensions = []

    @abstractmethod
    def parse(self, file: Path):
        """
        Parse a source file.
        """
        raise NotImplementedError()

    @abstractmethod
    def find_symbols(self, file: Path):
        """
        Return symbols from a file.
        """
        raise NotImplementedError()
