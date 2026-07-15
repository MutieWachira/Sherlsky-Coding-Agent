"""
Sherlsky Event Bus

Responsible for publishing events to interesetd subscribers
"""
from collections import defaultdict
from app.events.event import Event

class EventBus:
    """
    Lightweight synchronous event bus
    
    later we can change this with an asynchronous implementation without
    changing the rest of the application
    """
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_name: str, handler,):
        """
        Register a handler for an event
        """
        self._subscribers[event_name].append(handler)

    def publish(self, event: Event,):
        """
        Publish an event to all subscribers.
        """
        handlers = self._subscribers.get(event.name, [])

        for handler  in handlers:
            handler(event)