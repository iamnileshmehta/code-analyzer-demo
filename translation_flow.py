from translator.code_translator import translate_code


def run_translation(vector_store):
    translated = translate_code(
        user_request="Translate sales invoice calculation logic",
        target_language="TypeScript",
        vector_store=vector_store
    )

    print("\n===== TRANSLATED CODE =====\n")
    print(translated)
