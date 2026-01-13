import ast

def extract_entities(tree):
    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                imports.append(alias.name)

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports
    }

