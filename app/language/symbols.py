"""
Python Symbol Extractor.

Converts a Tree-sitter AST into semantic Symbol objects.
"""

from pathlib import Path

from tree_sitter import Node

from app.language.models import (
    Symbol,
    SymbolKind,
    ImportSymbol,
    Location,
)
from app.language.parser.walker import (
    ASTWalker,
    ASTContext,
)


class SymbolExtractor:
    """
    Extract semantic symbols from a Tree-sitter AST.
    """

    def __init__(self):
        self.walker = ASTWalker()

        self._handlers = {
            "class_definition": self._class_symbol,
            "function_definition": self._function_symbol,
            "import_statement": self._import_symbol,
        }

    def extract(self, tree, file_path):
        """
        Extract every supported symbol.
        """

        symbols = []

        for context in self.walker.walk(tree.root_node):

            symbol = self._extract_node(
                context,
                file_path,
            )

            if symbol is not None:
                symbols.append(symbol)

        return symbols

    def _extract_node(
        self,
        context: ASTContext,
        file_path,
    ):
        """
        Dispatch a node to the correct extractor.
        """

        handler = self._handlers.get(context.node.type)

        if handler is None:
            return None

        return handler(
            context,
            file_path,
        )

    def _location(
        self,
        node: Node,
        file_path,
    ):
        """
        Create a Location object.
        """

        return Location(
            file=file_path,
            line=node.start_point[0] + 1,
            column=node.start_point[1] + 1,
        )

    # ---------------------------------------------------------
    # Class Extraction
    # ---------------------------------------------------------

    def _class_symbol(
        self,
        context: ASTContext,
        file_path,
    ):
        """
        Extract a class definition.
        """

        node = context.node

        name_node = node.child_by_field_name("name")

        if name_node is None:
            return None

        return Symbol(
            name=name_node.text.decode(),
            kind=SymbolKind.CLASS,
            module=Path(file_path).stem,
            location=self._location(
                node,
                file_path,
            ),
        )

    # ---------------------------------------------------------
    # Function / Method Extraction
    # ---------------------------------------------------------

    def _function_symbol(
        self,
        context: ASTContext,
        file_path,
    ):
        """
        Extract a function or class method.
        """

        node = context.node

        name_node = node.child_by_field_name("name")

        if name_node is None:
            return None

        kind, owner = self._classify_function(
            context
        )

        is_async = any(
            child.type == "async"
            for child in node.children
        )

        return Symbol(
            name=name_node.text.decode(),
            kind=kind,
            parent=owner,
            module=Path(file_path).stem,
            is_async=is_async,
            location=self._location(
                node,
                file_path,
            ),
        )

    def _classify_function(
        self,
        context: ASTContext,
    ):
        """
        Determine whether a function is
        a standalone function or a class method.

        Returns
        -------
        tuple[SymbolKind, str | None]
        """

        for ancestor in reversed(
            context.ancestors
        ):

            if ancestor.type != "class_definition":
                continue

            class_name = ancestor.child_by_field_name(
                "name"
            )

            owner = (
                class_name.text.decode()
                if class_name is not None
                else None
            )

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
        file_path,
    ):
        """
        Extract a standard Python import statement.

        Supported:

            import requests
            import pathlib

        Future versions will support:

            import requests as req

            from pathlib import Path
        """

        node = context.node

        module_node = next(

            (
                child
                for child in node.children
                if child.type == "dotted_name"
            ),

            None,

        )

        if module_node is None:
            return None

        module_name = module_node.text.decode()

        return ImportSymbol(

            name=module_name,

            kind=SymbolKind.IMPORT,

            module=Path(file_path).stem,

            location=self._location(
                node,
                file_path,
            ),

            imported_name=None,

            alias=None,

            is_from_import=False,

        )