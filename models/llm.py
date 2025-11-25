def generate_ai_response(user_msg: str, intent: str, sentiment: str) -> str:
    return (
        f"Entendi sua mensagem: '{user_msg}'. "
        f"Intenção detectada: {intent}. "
        f"Sentimento: {sentiment}. "
        "Como posso ajudar mais?"
    )
