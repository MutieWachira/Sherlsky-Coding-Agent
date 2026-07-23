"""
Incoming request

Every user interaction becomes a Requset object
"""

from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime


@dataclass
class Request:
    prompt: str

    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)
    project_path: str | None = None
    session_id: str | None = None
