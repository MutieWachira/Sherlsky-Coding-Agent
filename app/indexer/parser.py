"""
Parser interface.

This will later use Tree-sitter ro parse code.
"""

class Parser:
    """
    Base parser.
    
    Each programming language will have its own implementation
    """

    def parse(self, path: str):
        raise NotImplementedError()