"""
Memory models for Sherlsky

Each memory entry represents one piece of information that the agent
may reuse later.
"""

from dataclasses import dataclass
from datetime import datetime

@dataclass
class MemoryItem:
    """
    One memory record.
    """
    category: str
    content: str
    timestamp: datetime