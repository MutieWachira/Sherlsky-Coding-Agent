"""
Base file for every Sherlsky plugin
"""

from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Every plugin must implement this interface
    """

    name = "Plugin"
    version = "1.0.0"
    author = "Sherlskyyy"

    @abstractmethod
    def initialize(self):
        """
        Called once when the plugin loads.
        """
        raise NotImplementedError()

    @abstractmethod
    def shutdown(self):
        """
        Called before the plugin unloads.
        """
        raise NotImplementedError()
