from fastapi import FastAPI
from pydantic import BaseModel

from models.intent_classifier import classify_intent
from models.sentiment_analyzer import analyze_sentiment
from models.llm import generate_ai_response

from services.fatura import gerar_segunda_via
from services.internet_status import verificar_internet
from services.protocolo import abrir_protocolo

app = FastAPI(title="ClaroX API")

from schemas.messages import ChatMessage

@app.post("/chat")
async def chat_endpoint(payload: ChatMessage):
    user_msg = payload.message

    # 1. Detectar intenção
    intent = classify_intent(user_msg)

    # 2. Sentimento
    sentiment = analyze_sentiment(user_msg)

    # 3. Executar ação
    if intent == "segunda_via":
        data = gerar_segunda_via(payload.user_id)
        ai_text = f"Aqui está sua segunda via da fatura: {data['link']}"

    elif intent == "internet_problema":
        status = verificar_internet(payload.user_id)
        ai_text = f"Status da sua internet: {status['descricao']}"

    elif intent == "abrir_protocolo":
        protocolo = abrir_protocolo(payload.user_id)
        ai_text = f"Protocolo aberto com sucesso: #{protocolo['id']}"

    else:
        ai_text = generate_ai_response(user_msg, intent, sentiment)

    return {
        "intent": intent,
        "sentiment": sentiment,
        "response": ai_text
    }
