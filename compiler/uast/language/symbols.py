"""
Python Symbol Extractor.

Converts a Tree-sitter AST into semantic Symbol objects.
"""

from tree_sitter import Node

from compiler.document.document import Document
from compiler.uast.language.models import (
    Symbol,
    SymbolKind,
    ImportSymbol,
    Location,
)
from compiler.parser.walker import (
    ASTWalker,
    ASTContext,
)


class SymbolExtractor:
    """
    Extract semantic symbols from a Document.
    """

    def __init__(self):
        self.walker = ASTWalker()

        self._handlers = {
            "class_definition": self._class_symbol,
            "function_definition": self._function_symbol,
            "import_statement": self._import_symbol,
        }

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def extract(
        self,
        document: Document,
    ) -> list[Symbol]:
        """
        Extract every supported symbol from a Document.
        """

        symbols: list[Symbol] = []

        for context in self.walker.walk_context(document.tree.root_node):
            symbol = self._extract_node(
                context=context,
                document=document,
            )

            if symbol is not None:
                symbols.append(symbol)

        return symbols

    # ---------------------------------------------------------
    # Dispatcher
    # ---------------------------------------------------------

    def _extract_node(
        self,
        context: ASTContext,
        document: Document,
    ):

        handler = self._handlers.get(context.node.type)

        if handler is None:
            return None

        return handler(
            context=context,
            document=document,
        )

    # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _location(
        self,
        node: Node,
        document: Document,
    ) -> Location:

        return Location(
            file=document.path,
            line=node.start_point[0] + 1,
            column=node.start_point[1] + 1,
        )

    # ---------------------------------------------------------
    # Class Extraction
    # ---------------------------------------------------------

    def _class_symbol(
        self,
        context: ASTContext,
        document: Document,
    ):

        node = context.node

        name_node = node.child_by_field_name("name")

        if name_node is None:
            return None

        return Symbol(
            name=name_node.text.decode(),
            kind=SymbolKind.CLASS,
            module=document.path.stem,
            location=self._location(
                node,
                document,
            ),
        )

    # ---------------------------------------------------------
    # Function / Method Extraction
    # ---------------------------------------------------------

    def _function_symbol(
        self,
        context: ASTContext,
        document: Document,
    ):

        node = context.node

        name_node = node.child_by_field_name("name")

        if name_node is None:
            return None

        kind, owner = self._classify_function(context)

        is_async = any(child.type == "async" for child in node.children)

        return Symbol(
            name=name_node.text.decode(),
            kind=kind,
            parent=owner,
            module=document.path.stem,
            is_async=is_async,
            location=self._location(
                node,
                document,
            ),
        )

    def _classify_function(
        self,
        context: ASTContext,
    ) -> tuple[SymbolKind, str | None]:
        """
        Determine whether the function is a
        standalone function or a class method.
        """

        for ancestor in reversed(context.ancestors):
            if ancestor.type != "class_definition":
                continue

            class_name = ancestor.child_by_field_name("name")

            owner = class_name.text.decode() if class_name else None

            return (
                SymbolKind.METHOD,
                owner,
            )

        return (
            SymbolKind.FUNCTION,
            None,
        )

    # ---------------------------------------------------------
    # Import Extraction
    # ---------------------------------------------------------

    def _import_symbol(
        self,
        context: ASTContext,
        document: Document,
    ):

        node = context.node

        module_node = next(
            (child for child in node.children if child.type == "dotted_name"),
            None,
        )

        if module_node is None:
            return None

        module_name = module_node.text.decode()

        return ImportSymbol(
            name=module_name,
            kind=SymbolKind.IMPORT,
            module=document.path.stem,
            location=self._location(
                node,
                document,
            ),
            imported_name=None,
            alias=None,
            is_from_import=False,
        )
