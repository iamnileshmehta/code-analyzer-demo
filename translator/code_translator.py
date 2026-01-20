
from rag.retriever import retrieve_relevant_code
from knowledge.builder import build_knowledge
from translator.ir_builder import build_ir
from translator.prompt_builder import generate_code
from rag.llm import call_llm
from rag.embedder import embed_text

def translate_code(
    user_request: str,
    target_language: str,
    vector_store,
    call_graph=None
):
    query_vec = embed_text(user_request)
    relevant_kos = vector_store.search(query_vec, top_k=5)


    ir_module = build_ir(knowledge_objects=relevant_kos,
        call_graph=call_graph
        )
    prompt = generate_code(ir_module, target_language)

    return prompt
