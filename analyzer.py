import ast
import os

from static_extractor.extractor import extract_entities
from static_extractor.connector import extract_relation
from knowledge.builder import build_knowledge
from static_extractor.output import display_results


def analyze_python_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    entities = extract_entities(tree, file_path)
    call_graph = extract_relation(tree)

    knowledge_objects = build_knowledge(
        functions=entities["functions"],
        classes=entities["classes"],
        relationships=call_graph,
        file_path=file_path
    )

    return knowledge_objects, entities, call_graph


def analyze_path(path):
    all_knowledge = []

    if os.path.isfile(path) and path.endswith(".py"):
        ko, entities, graph = analyze_python_file(path)
        display_results(entities, graph)
        all_knowledge.extend(ko)

    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    try:
                        ko, entities, graph = analyze_python_file(file_path)
                        all_knowledge.extend(ko)
                    except Exception as e:
                        print(f"⚠️ Skipped {file_path}: {e}")

    else:
        raise ValueError("Invalid path provided")

    return all_knowledge


if __name__ == "__main__":
    user_path = input("Enter file or directory path: ").strip()
    knowledge_objects = analyze_path(user_path)

    print(f"\n✅ Analysis complete. Extracted {len(knowledge_objects)} knowledge objects.")
