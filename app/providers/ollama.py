"""
Ollama provider implementation.
"""

import requests

from app.providers.base import BaseProvider

class OllamaProvider(BaseProvider):
    """
    Communicates with a local ollama model.
    """
    def __init__(
            self,
            model: str,
            host: str = "http://localhost:11434"
    ):
        self.model=model
        self.host = host

    def generate(self, prompt:str) -> str:
        response = requests.post(f"{self.host}/api/generate",
                                 json={
                                     "model: self.model,"
                                     "prompt": prompt,
                                     "stream": False,
                                 },
                                 timeout=120,
                                 )
        response.raise_for_status()

        return response.json()
    ["response"]