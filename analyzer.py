import ast
import sys
import os

from extractor import extract_entities
from connector import extract_relation
from output import display_results

from knowledge.builder import build_knowledge

from rag.embedder import embed_text
from rag.summarizer import summarize_function
from rag.vector_store import VectorStore

from translator.code_translator import translate_code


# Initialize vector store once
vector_store = VectorStore(dim=384)


def analyze_code(file_path: str):
    """
    End-to-end analysis pipeline:
    - Parse code
    - Extract entities & relationships
    - Build knowledge objects
    - Summarize & embed
    - Store in vector DB
    """

    # 1️⃣ Parse source code
    with open(file_path, "r", encoding="utf-8") as f:
        source_code = f.read()

    tree = ast.parse(source_code)

    # 2️⃣ Extract structure
    entities = extract_entities(tree, file_path)
    relations = extract_relation(tree)

    functions = entities.get("functions", [])
    classes = entities.get("classes", [])
    call_graph = relations.get("call_graph", {})

    # 3️⃣ Build knowledge layer
    knowledge_objects = build_knowledge(
        functions=functions,
        classes=classes,
        relationships=call_graph,
        file_path=file_path
    )

    # 4️⃣ Summarize + embed knowledge
    for ko in knowledge_objects:
        if ko.type == "function":
            ko.summary = summarize_function(ko.code, ko.name)

        text_for_embedding = f"""
        Name: {ko.name}
        Type: {ko.type}
        Summary: {ko.summary}
        Code:
        {ko.code}
        """

        embedding = embed_text(text_for_embedding)
        vector_store.add(embedding, ko)

    # 5️⃣ Display extracted results (human-readable)
    display_results(entities, relations)

    return vector_store


def get_python_files(path):
    if os.path.isfile(path) and path.endswith(".py"):
        return [path]

    py_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(root, file))
    return py_files


def run_demo_queries(vector_store):
    print("\n🔍 RAG Test Query:")
    results = vector_store.search(
        embed_text("How is bullish signal calculated?"),
        top_k=5
    )

    for r in results:
        print(" -", r.name)

    print("\n🌐 Code Translation:")
    translated = translate_code(
        user_request="Translate technical signal logic",
        target_language="TypeScript",
        vector_store=vector_store
    )

    print(translated)



if __name__ == "__main__":
    import sys
    analyze_code("sample.py")








    # target_path = sys.argv[1]
    # py_files = get_python_files(target_path)

    # for file in py_files:
    #     print(f"Analyzing: {file}")
    #     analyze_code(file)

