from app.language.manager import LanguageManager

def test_manager_parse():
    manager = LanguageManager()
    result = manager.parse("Hello.py")

    assert result["language"] == "Python"