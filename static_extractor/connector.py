import ast
from collections import defaultdict


class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        # function_name -> set(called_functions)
        self.call_graph = defaultdict(set)

        # Track current scope
        self.current_function = None
        self.current_class = None

    # ---------- Function & Class Tracking ----------

    def visit_ClassDef(self, node):
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        if self.current_class:
            self.current_function = f"{self.current_class}.{node.name}"
        else:
            self.current_function = node.name

        # Ensure function exists in graph
        self.call_graph[self.current_function]

        self.generic_visit(node)
        self.current_function = None

    # ---------- Call Extraction ----------

    def visit_Call(self, node):
        if not self.current_function:
            return  # Ignore calls outside functions

        called_name = self._resolve_call_name(node.func)
        if called_name:
            self.call_graph[self.current_function].add(called_name)

        self.generic_visit(node)

    # ---------- Helpers ----------

    def _resolve_call_name(self, node):
        """
        Resolve function names from different call types:
        - foo()
        - obj.foo()
        - Class.foo()
        """
        if isinstance(node, ast.Name):
            return node.id

        if isinstance(node, ast.Attribute):
            value = node.value
            if isinstance(value, ast.Name):
                return f"{value.id}.{node.attr}"
            return node.attr  # fallback

        return None


# ---------- Public API ----------

def extract_relation(tree):
    visitor = CallGraphVisitor()
    visitor.visit(tree)

    # Convert sets → lists for JSON compatibility
    call_graph = {
        func: sorted(list(calls))
        for func, calls in visitor.call_graph.items()
    }

    return {
        "call_graph": call_graph
    }


