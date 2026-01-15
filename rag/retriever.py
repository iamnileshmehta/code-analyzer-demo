from rag.embedder import embed_text

def retrieve_relevant_code(query, vector_store, top_k=3):
    query_vec = embed_text(query)
    return vector_store.search(query_vec, top_k)


