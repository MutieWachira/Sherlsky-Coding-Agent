"""Tool Registry

This module stores every tool Sherlsky can use

As the project grows, new tools can be registered here.
"""

from app.tools.files import (
    ReadFileTool,
    ListDirectoryTool,
)

TOOLS = {
    "read_file": ReadFileTool(),
    # "scan_project": ScanProjectTool(),
    "list_directory": ListDirectoryTool(),
}
