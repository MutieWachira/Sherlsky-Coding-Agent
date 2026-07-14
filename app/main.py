from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.routes.files import router as file_router
from app.routes.project import router as project_router

app = FastAPI(title="Sherlskyy")

app.include_router(chat_router)
app.include_router(file_router)
app.include_router(project_router)

@app.get("/")
def root():
    return {
        "status": "running",
        "agent": "Sherlskyy",
        "version": "0.1"
    }