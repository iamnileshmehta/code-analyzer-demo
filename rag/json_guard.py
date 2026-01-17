import json
import time

class JSONValidationError(Exception):
    pass

def parse_or_retry(llm_call_fn, base_prompt, max_retries=3, delay=1):
    """
    Calls LLM, validates JSON, retries if invalid
    """

    for attempt in range(1, max_retries+1):
        response = llm_call_fn(base_prompt, attempt)

        try:
            return json.loads(response)
        except Exception as e:
            last_error = str(e)
            print(f"[JSON ERROR] Attempt {attempt}: {last_error}")
            time.sleep(delay)
            
    raise JSONValidationError(
        f"Failed to parse JSON after {max_retries} attempts. \n Last error: {last_error}"
        )