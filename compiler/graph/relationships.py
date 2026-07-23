"""
Relationship types used by the Knowledge Graph.

Using an Enum instead of raw strings prevents typos,
improves autocomplete, and makes future expansion easy.
"""

from enum import Enum


class RelationshipType(Enum):
    DEFINES = "defines"

    IMPORTS = "imports"

    OWNS = "owns"

    CALLS = "calls"

    REFERENCES = "references"

    INHERITS = "inherits"

    IMPLEMENTS = "implements"

    DECORATED_BY = "decorated_by"

    RETURNS = "returns"

    USES = "uses"

    IMPORTS_MODULE = "imports_module"
