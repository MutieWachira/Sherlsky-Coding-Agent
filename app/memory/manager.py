"""
Central memory manager

Provides one interface for all memory systems.
"""

from app.memory.conversation import ConversationMemory
from app.memory.project import ProjectMemory


class MemoryManager:
    def __init__(self):
        self.conversation = ConversationMemory()
        self.project = ProjectMemory()
