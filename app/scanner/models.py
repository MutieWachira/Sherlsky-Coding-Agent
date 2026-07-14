"""
Project Scanner Models

These classes represent information about files and projects.

Keepings models separate makes the scanner easier to maintain and prepare us  for future database support

"""

from dataclasses import dataclass

@dataclass
class FileInfo:
    """
    represents one file inside a project
    """
    name: str
    path: str
    extension: str
    size: int


@dataclass 
class ProjectInfo:
    """
    Represents an entire scanned project
    """
    root: str
    files: list[FileInfo]