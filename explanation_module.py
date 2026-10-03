from gemini_client import ask


def explain_topic(topic: str) -> str:
    try:
        return ask(f"Explain the concept of '{topic}' in a simple and clear way "
                   "for a school student, in under 150 words.")
    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"
