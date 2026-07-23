from pathlib import Path

from compiler.parser.adapter import TreeSitterAdapter
from compiler.parser.walker import ASTWalker

parser = TreeSitterAdapter("python")

tree = parser.parse(Path("examples/sample.py"))

walker = ASTWalker()

parent_map = walker.build_parent_map(tree.root_node)

for node in walker.walk(tree.root_node):
    if node.type == "function_definition":
        name = node.child_by_field_name("name")

        print(f"\nFunction: {name.text.decode()}")

        current = parent_map.get(id(node))

        while current:
            print(" ->", current.type)
            current = parent_map.get(id(current))

    for node in walker.walk(tree.root_node):
        if node.type == "function_definition":
            print(node)
            print(id(node))

            print(parent_map.get(id(node)))
