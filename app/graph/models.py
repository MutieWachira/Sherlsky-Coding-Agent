"""
Knowledge Graph Models.
"""

from dataclasses import dataclass

from app.graph.relationships import RelationshipType
from app.language.models import Symbol


@dataclass(slots=True)
class GraphNode:
    """
    A node inside the Knowledge Graph.
    """

    symbol: Symbol

    @property
    def id(self) -> str:
        return self.symbol.id


@dataclass(slots=True)
class Relationship:
    """
    Directed edge between two graph nodes.
    """

    source: str
    target: str
    relation: RelationshipType

    @property
    def id(self) -> str:
        """
        Deterministic edge ID.

        Example:
        examples/sample.py:3:UserService:owns:examples/sample.py:6:login
        """
        return (
            f"{self.source}:"
            f"{self.relation.value}:"
            f"{self.target}"
        )

    @staticmethod
    def create(
        source: str,
        target: str,
        relation: RelationshipType,
    ) -> "Relationship":
        return Relationship(
            source=source,
            target=target,
            relation=relation,
        )