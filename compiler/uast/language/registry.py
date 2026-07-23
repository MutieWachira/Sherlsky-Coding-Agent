"""
Language registry
"""

from compiler.uast.language.services.python import PythonService


class LanguageRegistry:
    def __init__(self):
        self._services = [PythonService()]

    def get_service(self, extension):
        for service in self._services:
            if extension in service.supported_extensions:
                return service
        return None
