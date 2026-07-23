"""
Project Scanner API

Allows clients to scan a projecct directory
"""

from fastapi import APIRouter
from compiler.scanner.scanner import ProjectScanner

router = APIRouter(
    prefix="/project",
    tags=["Project"],
)

scanner = ProjectScanner()


@router.get("/scan")
def scan(path: str):

    project = scanner.scan(path)

    return {
        "root": project.root,
        "count": len(project.files),
        "files": [
            {
                "name": f.name,
                "path": f.path,
                "extension": f.extension,
                "size": f.size,
            }
            for f in project.files
        ],
    }
