from pydantic import BaseModel

class FaturaResponse(BaseModel):
    user_id: str
    link: str
