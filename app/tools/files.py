"""
File System Tools

This module contains safe, read-only operations that allow
Forge to inspect a project without modifying it.

Security Principles
-------------------
- Read-only operations.
- No file writes.
- No file deletion.
- No directory creation.
- No shell execution.

All write operations will be implemented as separate tools
that require explicit user approval.
"""

from pathlib import Path

from app.execution.context import ExecutionContext
from app.tools.base import Tool


class ReadFileTool(Tool):
    """
    Reads the contents of a text file.

    This tool is intentionally read-only.
    """

    name = "read_file"

    def execute(
        self,
        context: ExecutionContext,
        path: str,
    ) -> str:
        """
        Read a UTF-8 encoded text file.

        Parameters
        ----------
        context : ExecutionContext
            Shared execution context.

        path : str
            Absolute or relative file path.

        Returns
        -------
        str
            File contents.

        Raises
        ------
        FileNotFoundError
            If the file does not exist.

        ValueError
            If the path is not a file.
        """

        file = Path(path)

        if not file.exists():
            raise FileNotFoundError(
                f"File does not exist: {path}"
            )

        if not file.is_file():
            raise ValueError(
                f"Not a file: {path}"
            )

        content = file.read_text(
            encoding="utf-8"
        )

        # Store useful information for later tasks
        context.set("last_file", str(file))
        context.set("last_file_content", content)

        return content


class ListDirectoryTool(Tool):
    """
    Lists files inside a directory.

    Hidden and generated folders are ignored.
    """

    name = "list_directory"

    IGNORED = {
        ".git",
        ".venv",
        "__pycache__",
        "node_modules",
        ".next",
        "dist",
        "build",
    }

    def execute(
        self,
        context: ExecutionContext,
        path: str,
    ) -> list[str]:
        """
        List files and folders.

        Parameters
        ----------
        context : ExecutionContext
            Shared execution context.

        path : str
            Directory to inspect.

        Returns
        -------
        list[str]
            Sorted directory contents.
        """

        directory = Path(path)

        if not directory.exists():
            raise FileNotFoundError(path)

        if not directory.is_dir():
            raise ValueError(
                f"Not a directory: {path}"
            )

        items = [
            item.name
            for item in directory.iterdir()
            if item.name not in self.IGNORED
        ]

        items.sort()

        context.set("last_directory", str(directory))
        context.set("directory_listing", items)

        return items