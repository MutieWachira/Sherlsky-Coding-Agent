"""
Base class for all Sherlsky tools
"""

from abc import ABC, abstractMethod
from app.execution.context import ExecutionContext


class Tool(ABC):
    name = "tool"

    @abstractMethod
    def execute(
        self,
        context: ExecutionContext,
        **kwargs,
    ):
        """
        Execute this tool
        """
        raise NotImplementedError
