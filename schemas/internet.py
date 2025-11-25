from pydantic import BaseModel

class InternetStatusResponse(BaseModel):
    user_id: str
    status: str
    descricao: str
