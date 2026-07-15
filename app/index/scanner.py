"""
Project scanner.

Finds source files inside a project.
"""

from pathlib import Path


class ProjectScanner:
    """
    Scans a project directory for supported files.
    """

    SUPPORTED_EXTENSIONS = {
        ".py",
    }

    def scan(self, root: Path):
        """
        Yield every supported source file.
        """

        for file in root.rglob("*"):

            if (
                file.is_file()
                and file.suffix in self.SUPPORTED_EXTENSIONS
            ):
                yield file