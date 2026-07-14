"""
Base Provider Interface

Every AI model provider must implement this interface
"""

from abc import ABC, abstractmethod

class BaseProvider(ABC):
    """
    Abstract base class for model providers.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """"
        Generate response from a language model
        """
        pass