"""
Duplicate symbol detection.
"""

from app.index.models import ProjectIndex


class DuplicateDetector:

    def find_duplicates(
        self,
        index: ProjectIndex,
    ):

        duplicates = {}

        for name, symbols in index.by_name.items():

            if len(symbols) > 1:

                duplicates[name] = symbols

        return duplicates