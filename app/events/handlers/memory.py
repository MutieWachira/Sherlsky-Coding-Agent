"""
Memory event handler
"""

class MemoryHandler:
    """
    Stores selected events in memory.
    
    for now, this implementation is simple.
    later it can filter or summarize events.
    """
    def __init__(self):
        self.events = []

    def handle( self, event):
        self.events.append(event)