"""
Semantic Analysis Result.

Everything discovered during semantic analysis
is stored here.
"""

from dataclasses import dataclass, field

from app.language.models import Symbol
from app.reference.models import Reference
from app.reference.scope import Scope


@dataclass(slots=True)
class SemanticAnalysis:
    """
    Complete semantic information for one document.
    """
    def add_symbol(self, symbol):

        self.symbols.append(symbol)

    def add_scope(self, scope):

        self.scopes.append(scope)

    def add_reference(self, reference):

        self.references.append(reference)

    def add_call(self, call):

        self.calls.append(call)

    def add_diagnostic(self, diagnostic):

        self.diagnostics.append(diagnostic)