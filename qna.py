from gemini_client import ask


def answer_question(question: str) -> str:
    try:
        return ask(f"Answer this question accurately and concisely:\n{question}")
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"
