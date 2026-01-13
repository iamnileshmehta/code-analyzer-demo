def display_results(entities, relationships):
    print("\n📌 FUNCTIONS:")
    for f in entities["functions"]:
        print(f" - {f}")

    print("\n📌 CLASSES:")
    for c in entities["classes"]:
        print(f" - {c}")

    print("\n📌 IMPORTS:")
    for i in entities["imports"]:
        print(f" - {i}")

    print("\n📌 FUNCTION CALL RELATIONSHIPS:")
    for func, calls in relationships.items():
        print(f" {func} → {calls}")
