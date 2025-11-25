import streamlit as st
import requests

st.set_page_config(page_title="ClaroX Assistant", page_icon="🤖")

st.title("🤖 ClaroX – Assistente Inteligente")

st.write("Converse com o assistente da Claro em tempo real!")

# Campo de texto
user_input = st.text_input("Digite sua mensagem:")

if st.button("Enviar"):
    if not user_input.strip():
        st.warning("Digite uma mensagem.")
    else:
        payload = {
            "user_id": "12345",
            "message": user_input
        }

        try:
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json=payload
            )

            data = response.json()

            st.subheader("📌 Resultado")
            st.write("**Intenção:**", data["intent"])
            st.write("**Sentimento:**", data["sentiment"])
            st.write("**Resposta do Assistente:**")
            st.success(data["response"])

        except Exception as e:
            st.error("Erro ao conectar com o backend.")
            st.write(e)
