from pathlib import Path

from app.language.services.python import PythonService

def test_python_service_parse():
    service = PythonService()
    result = service.parse(Path("main.py"))
    assert result["language"] == "Python"
    assert result["status"] == "parsed"