import uuid

def abrir_protocolo(user_id: str):
    protocolo_id = str(uuid.uuid4())[:8]
    return {
        "id": protocolo_id,
        "status": "aberto",
        "user_id": user_id
    }
