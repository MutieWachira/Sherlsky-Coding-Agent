"""
Project Memory

Stores discovered information about the active codebase
"""


class ProjectMemory:
    def __init__(self):
        self.data = {}

    def store(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)
