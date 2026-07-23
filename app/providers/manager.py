"""
Provider manager

Responsible for selecting the active AI provider
"""

from app.providers.ollama import OllamaProvider


class ProviderManager:
    def __init__(self):
        self.provider = OllamaProvider(model="qwen2.5-coder:7b")

    def generate(self, prompt: str):
        return self.provider.generate(prompt)
