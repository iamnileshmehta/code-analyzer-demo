from rag.embedder import embed_text
from rag.summarizer import summarize_function
from rag.vector_store import VectorStore

MAX_LINES = 500  # VERY IMPORTANT

vector_store = VectorStore(dim=384)


def index_knowledge_objects(knowledge_objects):
    for ko in knowledge_objects:

        if ko.type != "function":
            continue

        if len(ko.code.splitlines()) > MAX_LINES:
            continue  # skip huge ERPNext functions

        try:
            summary = summarize_function(ko.code, ko.name)

            embedding_text = f"""
            Function: {ko.name}
            Summary: {summary}
            File: {ko.file_path}
            """

            vector = embed_text(embedding_text)
            vector_store.add(vector, ko)

        except Exception as e:
            print(f"⚠️ RAG skip {ko.name}: {e}")

    return vector_store
