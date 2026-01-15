import ast

from extractor import extract_entities
from output import display_results
from connnector import extract_relation

from translator.code_translator import translate_code

from knowledge.builder import build_knowledge

from rag.retriever import retrieve_relevant_code
from rag.summarizer import summarize_function
from rag.embedder import embed_text
from rag.vector_store import VectorStore

vector_store = VectorStore(dim=384)  # Assuming embedding dimension is 384


def analyze_code(file_path):
    with open(file_path, "r") as f:
        source_code = f.read()
        tree = ast.parse(source_code)

    entities = extract_entities(tree, source_code)
    relations = extract_relation(tree)

    functions = entities.get("functions", [])
    classes = entities.get("classes", [])
    call_graph = relations.get("call_graph", {})


    # Build knowledge objects
    knowledge_objects = build_knowledge(
    functions=functions,
    classes=classes,
    relationships=call_graph,
    file_path=file_path
)
    
    # Embed knowledge objects and store in vector store
    for ko in knowledge_objects:
        text = f"{ko.name}\n{ko.summary}\n{ko.code}"
        embedding = embed_text(text)
        vector_store.add(embedding, ko)
    
    
    # Add summaries to knowledge objects
    for ko in knowledge_objects:
        if ko.type == "function":
            ko.summary = summarize_function(ko.code, ko.name)


    # Display results
    display_results(entities, relations)

    results = retrieve_relevant_code(
    "How is bullish signal calculated?",
    vector_store
)

    for r in results:
        print(r.name)


    translated = translate_code(
        user_request="Translate technical signal logic",
        target_language="TypeScript",
        vector_store=vector_store
    )

    print(translated)

if __name__ == "__main__":
    analyze_code("sample.py")
