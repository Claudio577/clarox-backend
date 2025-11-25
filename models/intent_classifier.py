def classify_intent(text: str) -> str:
    text = text.lower()

    if "segunda via" in text or "fatura" in text or "boleto" in text:
        return "segunda_via"

    if "internet" in text and ("lenta" in text or "caiu" in text or "parou" in text):
        return "internet_problema"

    if "protocolo" in text or "abrir chamado" in text:
        return "abrir_protocolo"

    return "outros"
