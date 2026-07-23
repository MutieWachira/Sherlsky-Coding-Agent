"""
Logging event handler
"""

from app.utils.logger import logger


def log_event(event):
    """Log every published event"""
    logger.info(
        "[%s] %s",
        event.name,
        event.payload,
    )
