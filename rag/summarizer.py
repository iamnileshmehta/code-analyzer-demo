from rag.llm import call_llm

def summarize_function(code: str, name: str) -> str:
    """
    Summarizes what the function does based strictly on its code.
    """

    prompt = f"""
You are analyzing a Python function.

Function name: {name}

Code:
{code}

Task:
- Describe what this function does in 1–2 sentences.
- Do NOT assume anything not present in the code.
- Do NOT suggest improvements.
- Do NOT mention variable names unless relevant.
"""

    # call LLM here (OpenAI / Gemini / Claude)
    summary = call_llm(prompt)

    return summary.strip()
