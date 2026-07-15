"""
Execution result models
"""

from dataclasses import dataclass
from enum import Enum

class ResultStatus(Enum):
    SUCCESS = "success"
    FAILED = "failed" 
    SKIPPED = "skipped"

@dataclass
class TaskResult:
    task_id: int
    task_name: str
    status: ResultStatus
    output: str
