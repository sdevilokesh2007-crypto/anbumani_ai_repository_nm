from gemini_client import ask


def summarize_text(text: str) -> str:
    try:
        return ask(f"Summarize the following text in simple language:\n\n{text}")
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"
