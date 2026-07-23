"""
Planning models

These dataclasses describe tasks and execution plans.
"""

from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(Enum):
    """Represents the current state of a task"""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    """
    One step in an execution plan
    """

    id: int
    title: str
    tool: str | None = None
    status: TaskStatus = TaskStatus.PENDING


@dataclass
class ExecutionPlan:
    """
    Ordered collection of tasks.
    """

    goal: str
    tasks: list[Task] = field(default_factory=list)
