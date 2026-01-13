def print_tree(person, level=0):
    indent = "│   " * level
    print(f"{indent}├── {person}")

    for child in person.children:
        print_tree(child, level + 1)

