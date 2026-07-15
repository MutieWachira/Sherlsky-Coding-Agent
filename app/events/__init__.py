from app.events.bus import EventBus
from app.events.handlers.logging import log_event
from app.events.handlers.memory import MemoryHandler

bus = EventBus()

memory = MemoryHandler()

bus.subscribe(
    "ToolsCompleted",
    log_event,
)

bus.subscribe(
    "ToolCompleted",
    memory.handle
)