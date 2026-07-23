"""
Sherlsky Agent

The agent coordinates communication between the LLM
and the available tools.

The LLM never acceses the operating system directly.
Every interaction goes through this class.
"""

from app.services.ollama import generate


class Agent:
    """
    Main AI Agent
    """

    def __init__(self, model: str):
        self.model = model

    def ask(self, prompt: str) -> str:
        """
        Send a prompt to the LLM

        parameters
        --------------
        prompt : str

        Returns
        ---------------
        str"""

        return generate(
            prompt=prompt,
            model=self.model,
        )
