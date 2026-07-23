from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama import generate

router = APIRouter()


class ChatRequest(BaseModel):
    prompt: str
    model: str


@router.post("/chat")
def chat(request: ChatRequest):
    answer = generate(request.prompt, request.model)
    return {"response": answer}
