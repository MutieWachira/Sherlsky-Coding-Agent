"""
Base task implementation.

Every operation Sherlsky performs is 
represented as a task.
"""
from abc import ABC, abstractmethod
from enum import Enum
from uuid import uuid4

class TaskState(Enum):
    PENDING = "pending"
    READY = "ready"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

class Task(ABC):
    def __init__(self):
        self.id = str(uuid4())
        self.state = TaskState.Pending

    @abstractmethod
    def execute(self, context):
        """
        Execute this task
        """
        raise NotImplementedError()
