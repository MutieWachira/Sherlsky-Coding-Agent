"""
Shared execution context

Every task can read information form the context
and write new information into it
"""


class ExecutionContext:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def contains(self, key):
        return key in self.data
