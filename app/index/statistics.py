"""
Project statistics.
"""

from app.index.models import ProjectIndex


class IndexStatistics:
    def summary(
        self,
        index: ProjectIndex,
    ):

        return {
            "symbols": len(index.all()),
            "classes": len(index.classes()),
            "functions": len(index.functions()),
            "methods": len(index.methods()),
            "imports": len(index.imports()),
        }
