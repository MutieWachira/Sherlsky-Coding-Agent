"""
Tests for the ProviderManger
"""

from unittest.mock import MagicMock
from app.providers.manager import ProviderManager


def test_generate_returns_provider_response():
    """
    ProviderManager should return the response from the active provider
    """

    manager = ProviderManager()
    manager.provider = MagicMock()

    manager.provider.generate.return_value = "Hello Sherlsky"
    response = manager.generate("Hi")
    assert response == "Hello Sherlsky"

    manager.provider.generate.assert_called_once_with("Hi")
