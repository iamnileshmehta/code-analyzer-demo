import ast


# ---------- Utilities ----------

def get_docstring(node):
    return ast.get_docstring(node)


def get_source_code(node):
    """
    Safely extract source code from AST node.
    """
    try:
        return ast.unparse(node)
    except Exception:
        return None


# ---------- AST Visitor ----------

class EntityExtractor(ast.NodeVisitor):
    def __init__(self, file_path):
        self.file_path = file_path

        self.functions = []
        self.classes = []
        self.imports = []

        self.current_class = None

    # ---------- Class ----------

    def visit_ClassDef(self, node):
        class_data = {
            "name": node.name,
            "docstring": get_docstring(node),
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", None),
            "file": self.file_path,
            "methods": []
        }

        self.classes.append(class_data)

        self.current_class = class_data
        self.generic_visit(node)
        self.current_class = None

    # ---------- Function / Method ----------

    def visit_FunctionDef(self, node):
        func_data = {
            "name": node.name,
            "qualified_name": (
                f"{self.current_class['name']}.{node.name}"
                if self.current_class else node.name
            ),
            "type": "method" if self.current_class else "function",
            "args": [arg.arg for arg in node.args.args],
            "decorators": [get_source_code(d) for d in node.decorator_list],
            "docstring": get_docstring(node),
            "code": get_source_code(node),
            "line_start": node.lineno,
            "line_end": getattr(node, "end_lineno", None),
            "file": self.file_path
        }

        if self.current_class:
            self.current_class["methods"].append(func_data)
        else:
            self.functions.append(func_data)

        self.generic_visit(node)

    # ---------- Imports ----------

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append({
                "module": alias.name,
                "alias": alias.asname,
                "type": "import"
            })

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.imports.append({
                "module": node.module,
                "name": alias.name,
                "alias": alias.asname,
                "type": "from_import"
            })


# ---------- Public API ----------

def extract_entities(tree, file_path):
    extractor = EntityExtractor(file_path)
    extractor.visit(tree)

    return {
        "functions": extractor.functions,
        "classes": extractor.classes,
        "imports": extractor.imports
    }
