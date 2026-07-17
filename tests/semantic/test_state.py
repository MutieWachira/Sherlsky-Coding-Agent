from pathlib import Path

from app.language.models import Symbol, SymbolKind, Location
from app.semantic.state import SemanticState


def test_add_symbol():
    analysis = SemanticAnalysis()

    state = SemanticState()

    context = SemanticContext(
        analysis=analysis,
        state=state,
        document=None,
    )

    state.add_symbol(context, symbol)

    assert len(analysis.symbols) == 1