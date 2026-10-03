import json
import re
from gemini_client import ask


def clean_json_block(text: str) -> str:
    """Remove ```json code fences if the model adds them."""
    return re.sub(r"```(?:json)?\n?(.*?)```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    prompt = f"""You are a quiz generator.
From the following topic or passage, create 3 multiple-choice questions.
Each question must have: "question", "options" (list of 4 strings), and
"answer" (must exactly match one of the options).
Return only valid JSON: [{{"question": "...", "options": ["..."], "answer": "..."}}]

Topic/Passage:
{text}"""
    return json.loads(clean_json_block(ask(prompt, as_json=True)))
