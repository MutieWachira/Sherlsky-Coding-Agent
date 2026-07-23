from pathlib import Path


class ModuleResolver:
    """
    Resolves imported module names to files
    inside the current project.
    """

    def resolve(
        self,
        project_root: Path,
        module_name: str,
    ):

        candidate = project_root / f"{module_name}.py"

        if candidate.exists():
            return candidate

        return None
