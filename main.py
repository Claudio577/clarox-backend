from fastapi import FastAPI

from schemas.messages import ChatMessage
from schemas.chat_response import ChatResponse
from schemas.fatura import FaturaResponse
from schemas.internet import InternetStatusResponse
from schemas.protocolo import ProtocoloResponse
from services.logging_service import save_log

from models.intent_classifier import classify_intent
from models.sentiment_analyzer import analyze_sentiment
from models.llm import generate_ai_response

from services.fatura import gerar_segunda_via
from services.internet_status import verificar_internet
from services.protocolo import abrir_protocolo

app = FastAPI(title="ClaroX API")

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatMessage):
    user_msg = payload.message

    # 1. Detecção de intenção
    intent = classify_intent(user_msg)

    # 2. Sentimento
    sentiment = analyze_sentiment(user_msg)

    # 3. Ação baseada na intenção
    if intent == "segunda_via":
        data = gerar_segunda_via(payload.user_id)
        ai_text = f"Aqui está sua segunda via da fatura: {data['link']}"

    elif intent == "internet_problema":
        status = verificar_internet(payload.user_id)
        ai_text = f"Status da sua internet: {status['descricao']}"

    elif intent == "abrir_protocolo":
        protocolo = abrir_protocolo(payload.user_id)
        ai_text = f"Protocolo #{protocolo['id']} aberto com sucesso!"

    else:
        ai_text = generate_ai_response(user_msg, intent, sentiment)

    # 4. Registrar log (AGORA está no lugar certo!)
    save_log(payload.user_id, intent, sentiment, user_msg)

    # 5. Retorno padronizado
    return ChatResponse(
        intent=intent,
        sentiment=sentiment,
        response=ai_text
    )
