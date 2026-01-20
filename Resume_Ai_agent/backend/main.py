from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import agent  # your existing agent import

app = FastAPI()

# Allow CORS
origins = [
    "http://127.0.0.1:5500",  # your frontend if using Live Server
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InterviewRequest(BaseModel):
    resume_text: str
    role: str

@app.post("/interview")
async def interview(request: InterviewRequest):
    prompt = f"Resume: {request.resume_text}\nJob Role: {request.role}\nConduct an interview."
    result = await agent.run(prompt)  # note the 'await'
    output_text = result.output
    return {"response": output_text}
