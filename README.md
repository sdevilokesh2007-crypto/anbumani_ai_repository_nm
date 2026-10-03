# EduGenie: Gemini Powered Learning Assistant

AI learning assistant built with **FastAPI**, **HTML/CSS/JS**, and the **Google Gemini API**.

## Features
- Q&A (`/qa`), concept explanation (`/explain`), summarizer (`/summarize`)
- Quiz generator with answer checking (`/quiz`)
- Beginner-to-advanced learning paths (`/learn/recommendations`)

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env      # then paste your key from https://aistudio.google.com/api-keys
uvicorn main:app --reload
```
Open http://127.0.0.1:8000

## Structure
```
main.py  qna.py  explanation_module.py  quiz_module.py
summary_module.py  learning_path.py  gemini_client.py
templates/index.html  static/style.css  requirements.txt
```
