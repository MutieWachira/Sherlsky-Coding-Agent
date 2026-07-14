"""
Models used by the code indexer.
"""

from dataclasses import dataclass

@dataclass
class Symbol:
    """
    Represents  a code symbol
    
    A symbol can be a function, class, method, interface, enum, variable, etc.
    """

    name: str
    type: str
    line: int
    file: str

@dataclass
class FileIndex:
    """
    Information extracted from one file
    """

    file:str
    symbols: list[Symbol]
