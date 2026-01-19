import ast

def get_docstring(node):
    return ast.get_docstring(node)

def extract_entities(tree, file_path):
    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
        "name": node.name,
        "code": ast.unparse(node),
        "docstring": get_docstring(node),
        "line": node.lineno,
        "file": file_path
    })

        elif isinstance(node, ast.ClassDef):
            classes.append({
        "name": node.name,
        "docstring": get_docstring(node),
        "line": node.lineno,
        "file": file_path
    })

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                imports.append(alias.name)

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports
    }

