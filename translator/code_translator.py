from rag.retriever import retrieve_relevant_code
from translator.prompt_builder import build_translation_prompt
from rag.llm import call_llm

def translate_code(
    user_request: str,
    target_language: str,
    vector_store
):
    relevant_kos = retrieve_relevant_code(
        user_request,
        vector_store,
        top_k=5
    )

    prompt = build_translation_prompt(
        target_language,
        relevant_kos
    )

    return call_llm(prompt)
