import ast


class CallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = {}

    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.calls[self.current_function] = []
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.calls[self.current_function].append(node.func.id)
        self.generic_visit(node)

def extract_relation(tree):
    visitor = CallVisitor()
    visitor.visit(tree)
    return visitor.calls