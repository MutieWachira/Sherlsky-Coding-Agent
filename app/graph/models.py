"""
Knowledge Graph Models.
"""

from dataclasses import dataclass
from uuid import uuid4

from app.graph.relationships import RelationshipType
from app.language.models import Symbol


@dataclass(slots=True)
class GraphNode:
    """
    A node inside the Knowledge Graph.
    """

    id: str

    symbol: Symbol


@dataclass(slots=True)
class Relationship:
    """
    Directed edge.
    """

    id: str

    source: str

    target: str

    relation: RelationshipType

    @staticmethod
    def create(
        source: str,
        target: str,
        relation: RelationshipType,
    ):
        return Relationship(
            id=str(uuid4()),
            source=source,
            target=target,
            relation=relation,
        )