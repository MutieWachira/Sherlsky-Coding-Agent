from pathlib import Path

from app.language.registry import LanguageRegistry


class LanguageManager:
    """
    High-level interface for language services.
    """

    def __init__(self):
        self.registry = LanguageRegistry()

    def service_for(self, file_path: Path):
        """
        Return the language service responsible for a file.
        """
        service = self.registry.get_service(file_path.suffix)

        if service is None:
            raise ValueError(
                f"No language service registered for '{file_path.suffix}'"
            )

        return service

    def parse(self, file_path: Path):
        """
        Convenience method for parsing a file.
        """
        service = self.service_for(file_path)
        return service.parse(file_path)