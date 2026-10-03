from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations
from gemini_client import chat

app = FastAPI(title="EduGenie")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class TopicIn(BaseModel):
    topic: str


class TextIn(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/qa")
def qa(question: str = Query(...)):
    return {"answer": answer_question(question)}


@app.post("/explain")
def explain(data: TopicIn):
    return {"topic": data.topic, "explanation": explain_topic(data.topic)}


@app.post("/summarize")
def summarize(data: TextIn):
    return {"summary": summarize_text(data.text)}


@app.post("/quiz")
def quiz(data: TextIn):
    try:
        return {"quiz": generate_quiz(data.text)}
    except Exception as e:
        return JSONResponse({"error": f"Quiz error: {e}"}, status_code=500)


@app.get("/learn/recommendations")
def recommendations(topic: str = Query(...)):
    return {"topic": topic, "recommendation": get_learning_recommendations(topic)}


class ChatIn(BaseModel):
    message: str
    history: list = []


@app.post("/chat")
def chat_api(data: ChatIn):
    try:
        return {"reply": chat(data.history, data.message)}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
