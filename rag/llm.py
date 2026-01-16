import subprocess

def call_llm(prompt: str, model: str = "qwen2.5:3b") -> str:
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



