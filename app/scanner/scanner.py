"""Sherlsky project scanner

scan an entire project recursively.

The scanner builds metadata about every source file without
loading file contents into memory.
"""

from pathlib import Path

from app.scanner.models import (
    FileInfo,
    ProjectInfo,
)

from app.scanner.ignore import(
    IGNORED_DIRECTORIES,
    IGNORED_EXTENSIONS,
)

class ProjectScanner:
    """
    Scans a project directory.
    """

    def scan(self, root: str) -> ProjectInfo:

        project_root = Path(root).resolve()

        if not project_root.exists():
            raise FileNotFoundError(
                f"Project does not exist: {project_root}"
            )

        if not project_root.is_dir():
            raise NotADirectoryError(
                f"{project_root} is not a directory."
            )

        files = []

        for file in project_root.rglob("*"):

            print(file)

            if not file.is_file():
                continue

            # Ignore generated folders
            if any(
                part in IGNORED_DIRECTORIES
                for part in file.parts
            ):
                continue

            # Ignore binary files
            if file.suffix in IGNORED_EXTENSIONS:
                continue

            files.append(
                FileInfo(
                    name=file.name,
                    path=str(file),
                    extension=file.suffix,
                    size=file.stat().st_size,
                )
            )

        # ✅ Return AFTER scanning every file
        return ProjectInfo(
            root=str(project_root),
            files=files,
        )