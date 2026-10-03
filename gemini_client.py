import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
MODEL = "gemini-3.8-flash"
_client = None

SYSTEM = """You are EduGenie, a friendly AI tutor. In ONE conversation you handle:
- Questions: give accurate, concise answers.
- Explanations: explain concepts simply, like for a school student.
- Summaries: summarize pasted text in simple language.
- Quizzes: when asked, create 3 multiple-choice questions (A-D) and put the answers at the end under 'Answers'.
- Learning paths: give Beginner, Intermediate and Advanced levels with topics, time estimates and resources.
Detect what the student wants from their message. Keep replies clear and well organised."""


def _get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return _client


def ask(prompt: str, as_json: bool = False) -> str:
    """Single prompt -> text reply (used by the module files)."""
    config = types.GenerateContentConfig(
        response_mime_type="application/json" if as_json else "text/plain"
    )
    return _get_client().models.generate_content(
        model=MODEL, contents=prompt, config=config
    ).text.strip()


def chat(history: list, message: str) -> str:
    """Chat with memory. history = [{'role': 'user'|'model', 'text': '...'}]"""
    contents = [
        types.Content(role=h["role"], parts=[types.Part(text=h["text"])])
        for h in history
    ]
    contents.append(types.Content(role="user", parts=[types.Part(text=message)]))
    config = types.GenerateContentConfig(system_instruction=SYSTEM)
    return _get_client().models.generate_content(
        model=MODEL, contents=contents, config=config
    ).text.strip()
