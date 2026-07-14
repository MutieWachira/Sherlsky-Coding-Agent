"""
Conversation memory

Stores recent user interactions.
"""

from datetime import datetime
from app.memory.models import MemoryItem

class ConversationMemory:
    def __init__(self):
        self.messages: list[MemoryItem] = []

    def add(self, message: str):
        self.messages.append(
            MemoryItem(
                category="conversation",
                content=message,
                timestamp=datetime.now()
            )
        )

    def recent(self, limit=10):
        return self.mesage[-limit:]