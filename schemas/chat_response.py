from pydantic import BaseModel

class ChatResponse(BaseModel):
    intent: str
    sentiment: str
    response: str
