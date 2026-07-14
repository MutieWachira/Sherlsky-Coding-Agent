"""Tool Registry

This module stores every tool Sherlsky can use

As the project grows, new tools can be registered here.
"""

from app.tools.files import (
    read_file,
    list_directory,
)

TOOLS={ 
    "read_file": read_file,
    "list_directory": list_directory,
}
