"""Base event model

Every event in forge inherits from this class
"""

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """
    Base event.

    Attributes
    ----------
    id - Unique event identifier
    timestamp - When the event occured
    name - Human-readable event name
    payload - Event-specific data.
    """

    name: str
    payload: dict = field(default_factory=dict)
    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
