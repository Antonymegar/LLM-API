from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from gemini_client import ask_gemini

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    model: str = "gemini-2.5-flash" 

@app.post("/chat")
async def chat(req: PromptRequest):
    answer = ask_gemini(req.prompt, req.model)
    return {"response": answer}
