import ast

def extract_entities(tree, source_code):
    functions = []
    classes = []
    imports = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
    "name": node.name,
    "code": ast.get_source_segment(source_code, node),
    "imports": []
})

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

