from pydantic import BaseModel

class InterviewRequest(BaseModel):
    resume_text: str
    role: str
    answer: str | None = None
