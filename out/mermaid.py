def to_mermaid(call_relations):
    lines = ["graph LR"]

    for call in call_relations:
        caller = call["caller"]
        callee = call["callee"]
        lines.append(f"    {caller} --> {callee}")

    return "\n".join(lines)