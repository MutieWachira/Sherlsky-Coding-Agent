"""
Language manager

finds the correct language service for a file
"""

from pathlib import Path
from app.language.registry import LanguageRegistry

class LanguageManager:
    def __init__(self):
        self.registry = LanguageRegistry()

    def parse (self, filename):
        path = Path(filename)

        service = self.registry.get_service(path.suffix)

        if service is None:
            raise ValueError(f"No Language service for {path.suffix}")
        return service.parse(path)