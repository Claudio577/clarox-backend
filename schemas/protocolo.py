from pydantic import BaseModel

class ProtocoloResponse(BaseModel):
    id: str
    user_id: str
    status: str
