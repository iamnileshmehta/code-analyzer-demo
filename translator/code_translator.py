
from rag.retriever import retrieve_relevant_code
from translator.prompt_builder import build_translation_prompt
from rag.llm import call_llm
from rag.embedder import embed_text

def translate_code(
    user_request: str,
    target_language: str,
    vector_store
):
    query_vec = embed_text(user_request)
    relevant_kos = vector_store.search(query_vec, top_k=5)


    prompt = build_translation_prompt(
        target_language,
        relevant_kos
    )

    result = parse_or_retry(
        llm_call_fn=call_llm,
        base_prompt=prompt,
        max_retries=3
    )

    return result
