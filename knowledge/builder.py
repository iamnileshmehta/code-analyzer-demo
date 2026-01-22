from knowledge.schema import KnowledgeObject

def build_knowledge(functions, classes, relationships, file_path):
    knowledge = []

    for func in functions:
        ko = KnowledgeObject(
            id=f"{file_path}::{func['name']}",
            type="function",
            name=func['name'],
            file_path=file_path,
            code=func['code'],
            calls=relationships.get(func['name'], []),
            imports=func.get('imports', []),
            summary=func.get('summary')
        )
        knowledge.append(ko)

    return knowledge