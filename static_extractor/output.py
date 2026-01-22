from mermaid_graph.mermaid import to_mermaid


def display_results(entities, relationships):
    print("\n📌 FUNCTIONS:")
    for f in entities["functions"]:
        print(f" - {f}\n")

    print("\n📌 CLASSES:")
    for c in entities["classes"]:
        print(f" - {c}\n")

    print("\n📌 IMPORTS:")
    for i in entities["imports"]:
        print(f" - {i}")

    print("\n📌 FUNCTION CALL RELATIONSHIPS:")
    for func, calls in relationships.items():
        print(f" {func} → {calls}\n")

    mermaid_graph = to_mermaid(relationships)
    with open("callgraph.md", "w") as f:
        f.write(mermaid_graph)

    print("\n📊 Mermaid call graph written to callgraph.md")