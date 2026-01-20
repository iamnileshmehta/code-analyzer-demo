from rag.llm import call_llm


def generate_code(ir_module, target_language: str) -> str:
    prompt = f"""
You are a code analyzer, translator and code modernization tool.

Translate the following intermediate representation (IR)
into clean, idiomatic {target_language} code.

Rules:
- Use best practices of {target_language}
- Use appropriate syntax and conventions
- Preserve logic and function names
- Output only code
- Explain the json structure

IR:
{ir_module}
"""

    return call_llm(prompt)
