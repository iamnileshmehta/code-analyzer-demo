def build_translation_prompt(
    target_language: str,
    knowledge_objects
):
    context = "\n\n".join([
        f"Function: {ko.name}\nCode:\n{ko.code}"
        for ko in knowledge_objects
    ])

    return f"""
You are a software modernization tool.

Your task:
- Translate the following Python legacy logic into {target_language}
- Preserve business logic exactly
- Use idiomatic {target_language}
- Do NOT change behavior

Legacy code context:
{context}

Output ONLY valid {target_language} code.
"""


