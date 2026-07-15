"""
Planner

Creates an execution plan form a user goal

This first implementation uses simple keyword rules.
Later it will use an LLM to generate plans dynamically.
"""

from app.planner.models import ExecutionPlan, Task

class Planner:
    """
    Responsible for generating execution plans.
    """
    def create_plan(self, goal: str) -> ExecutionPlan:
        """
        convert a natural language goal into a sequence of executable tasks
        """
        tasks = [
            Task(
                id=1,
                title="Scan project",
                tool="project_scan",
            ),
            Task(
                id=2,
                title="Search relevant files",
                tool="symbol_search",
            ),
            Task(
                id=3,
                title="Read selected files",
                tool="read_file",
            ),
            Task(
                id=4,
                title="Analyze findings",
                tool=None,
            ),
        ]
        return ExecutionPlan(
            goal=goal,
            tasks=tasks,
        )