from gemini_client import ask


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured learning path with Beginner, Intermediate and Advanced levels.
For each level give key topics, estimated time, and resources (videos, articles, books)."""
    try:
        return ask(prompt)
    except Exception as e:
        return f"❌ Error occurred: {e}"
