import subprocess

def call_llm(prompt: str, model: str = "llama3.1:8b") -> str:
    """
    Calls a local Ollama model to generate text from a prompt.
    """
    try:
        # Ollama CLI: use 'run' instead of 'generate'
        result = subprocess.run(
            ["ollama", "run", model, "--prompt", prompt],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"[LLM ERROR]: {e.stderr}"
