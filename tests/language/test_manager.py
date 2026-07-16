from pathlib import Path

from app.language.manager import LanguageManager


def test_manager_parse():

    manager = LanguageManager()

    file_path = Path("examples/sample.py")

    service = manager.service_for(file_path)

    tree = service.parse(file_path)

    assert tree is not None
    assert tree.root_node.type == "module"