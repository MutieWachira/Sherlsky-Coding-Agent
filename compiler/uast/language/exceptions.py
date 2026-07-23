"""
Language Service exceptions.
"""


class LanguageServiceError(Exception):
    """Base language service error."""


class UnsupportedLanguage(LanguageServiceError):
    """Raised when no language service exists."""


class ParseError(LanguageServiceError):
    """Raised when parsing fails."""
