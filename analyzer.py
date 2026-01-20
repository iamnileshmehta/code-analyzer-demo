import ast
import sys
import os

from static_extractor.extractor import extract_entities
from static_extractor.connector import extract_relation
from static_extractor.output import display_results
from mermaid_graph.mermaid import to_mermaid

from knowledge.builder import build_knowledge

from rag.embedder import embed_text
from rag.summarizer import summarize_function
from rag.vector_store import VectorStore

from translator.code_translator import translate_code


# Initialize vector store once (global / app-level)
vector_store = VectorStore(dim=384)


def analyze_code(file_path):
    with open(file_path, "r") as f:
        source_code = f.read()
        tree = ast.parse(source_code)

    # 1️⃣ Extract entities
    entities = extract_entities(tree, file_path)
    functions = entities["functions"]
    classes = entities["classes"]

    # 2️⃣ Extract relationships
    call_graph = extract_relation(tree)

    # 3️⃣ Build knowledge layer
    knowledge_objects = build_knowledge(
        functions=functions,
        classes=classes,
        relationships=call_graph,
        file_path=file_path
    )

    # 4️⃣ Summarize + Embed (RAG indexing)
    for ko in knowledge_objects:
        if ko.type == "function":
            ko.summary = summarize_function(ko.code, ko.name)

            # Build embedding text (VERY IMPORTANT)
            embedding_text = f"""
            Function Name: {ko.name}
            Summary: {ko.summary}
            Code:
            {ko.code}
            """

            vector = embed_text(embedding_text)
            vector_store.add(vector, ko)

    # 5️⃣ Display analysis results
    display_results(entities, call_graph)

    return vector_store


if __name__ == "__main__":

    vector_store = analyze_code("sample.py")

    # 🔹 Example translation request (can be CLI / API later)
    translated_code = translate_code(
        user_request="Translate area calculation logic",
        target_language="TypeScript",
        vector_store=vector_store
    )

    print("\n===== TRANSLATED CODE =====\n")
    print(translated_code)
