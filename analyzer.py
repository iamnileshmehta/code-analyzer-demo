import ast
from extractor import extract_entities
from output import display_results
from connnector import extract_relation


def analyze_code(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    entities = extract_entities(tree)
    relations = extract_relation(tree)

    display_results(entities, relations)

if __name__ == "__main__":
    analyze_code("sample.py")
