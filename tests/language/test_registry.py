from app.language.registry import LanguageRegistry

def test_registry_returns_python():
    registry = LanguageRegistry()

    service = registry.get_service(".py")
    
    assert service.language_name == "Python"
