import subprocess

def call_llm(prompt: str, attempt: int=1, model: str = "qwen2.5:3b") -> str:

    """
    Calls Ollama / LLM
    """
    strict_prefix = ""
    if attempt > 1:
        strict_prefix = (
            "CRITICAL:\n"
            "- Output VALID JSON ONLY\n"
            "- No explanations\n"
            "- No markdown\n"
            "- No text outside JSON\n\n"
        )

    full_prompt = strict_prefix + prompt
    
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore"   # 🔑 CRITICAL FIX
        )

        if result.returncode != 0:
            return f"[LLM ERROR]: {result.stderr.strip()}"

        return result.stdout.strip()

    except Exception as e:
        return f"[LLM ERROR]: {str(e)}"



