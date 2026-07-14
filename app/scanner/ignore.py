"""
Directories that Sherlsky should ignore while scanning

 these folders are usually generated automatically and contain thousands of files 
 that do not help the AI understand the project
"""

IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".next",
    "dist",
    "build",
    ".idea",
    ".vscode",
}

IGNORED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".svg",
    ".ico",
    ".pdf",
    ".zip",
    ".gz",
    ".mp4",
}
