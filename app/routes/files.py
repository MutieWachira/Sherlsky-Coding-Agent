"""
Read-only File API

These endpoints expose safe file-system operations
"""

from fastapi import APIRouter
from app.tools.files import (
    read_file, list_directory,
    )

router = APIRouter(prefix="/files", tags=(["Files"]))

@router.get("/read")
def read(path: str):
    """
    Read a text file
    Example:
    /files/read?path=README.md
    """
    return {
        "content": read_file(path)
    }
    
@router.get("/list")
def list_files(path: str):
    """
    List files inside a directory

    Example: /files/list?path=.
    """

    return{
        "files": list_directory(path)
    }