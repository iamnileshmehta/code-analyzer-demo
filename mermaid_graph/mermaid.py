def to_mermaid(call_graph: dict) -> str:
    """
    Convert call graph dict to Mermaid diagram.
    """
    lines = ["graph TD"]

    for caller, callees in call_graph.items():
        for callee in callees:
            lines.append(f"    {caller} --> {callee}")

    return "\n".join(lines)
