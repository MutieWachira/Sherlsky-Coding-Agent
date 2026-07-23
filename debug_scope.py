from pathlib import Path
from compiler.document.manager import DocumentManager
from compiler.reference.builder import ScopeBuilder, Scope


def print_scope_tree(scope: Scope, indent: int = 0) -> None:
    padding = "  " * indent
    symbol_names = [getattr(s, "name", str(s)) for s in scope.symbols]
    sym_info = f" (symbols: {symbol_names})" if symbol_names else ""
    print(f"{padding}└─ [{scope.kind.name}] {scope.name}{sym_info}")

    for child in scope.children:
        print_scope_tree(child, indent + 1)


def main():
    sample_file = Path("examples/sample.py")
    if not sample_file.exists():
        sample_file.parent.mkdir(parents=True, exist_ok=True)
        sample_file.write_text(
            "class UserService:\n"
            "    def login(self, token):\n"
            "        result = True\n"
            "        return result\n"
        )

    manager = DocumentManager()
    document = manager.open(sample_file)

    builder = ScopeBuilder()
    root_scope = builder.build(document)

    print("\n=== Scope Tree Visualizer ===")
    print_scope_tree(root_scope)


if __name__ == "__main__":
    main()