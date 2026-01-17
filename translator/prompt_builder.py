def build_translation_prompt(target_language, relevant_kos):
    return f"""
You are an enterprise code modernization engine.

Rules:
- Translate Python functions into {target_language}
- Preserve logic EXACTLY
- Do not refactor or optimize
- Do not change function signatures
- Output VALID JSON ONLY
- No markdown
- No extra text

JSON schema:
{{
  "language": "{target_language}",
  "functions": [
    {{
      "name": "string",
      "signature": "string",
      "code": "string",
      "explanation": "string"
    }}
  ]
}}

Functions to translate:
{relevant_kos}
"""
