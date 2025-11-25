negative_words = ["ruim", "péssimo", "horrível", "droga", "lento", "caiu", "raiva"]
positive_words = ["bom", "ótimo", "perfeito", "maravilha"]

def analyze_sentiment(text: str) -> str:
    text = text.lower()

    if any(w in text for w in negative_words):
        return "negativo"

    if any(w in text for w in positive_words):
        return "positivo"

    return "neutro"
