import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="ClaroX Dashboard", page_icon="📊", layout="wide")

st.title("📊 Dashboard – ClaroX Assistente Inteligente")

LOG_FILE = "data/logs.json"

# Carregar logs
try:
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
except:
    logs = []

if not logs:
    st.warning("Nenhum atendimento registrado ainda.")
else:
    df = pd.DataFrame(logs)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de atendimentos", len(df))

    with col2:
        st.metric("Intenções únicas detectadas", df["intent"].nunique())

    with col3:
        st.metric("Sentimento mais comum", df["sentiment"].mode()[0])

    st.subheader("📌 Distribuição de Intenções")
    st.bar_chart(df["intent"].value_counts())

    st.subheader("😊 Distribuição de Sentimentos")
    st.bar_chart(df["sentiment"].value_counts())

    st.subheader("🕒 Atendimentos ao longo do tempo")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")
    df["count"] = 1
    st.line_chart(df.set_index("timestamp")["count"])

    st.subheader("📝 Últimos atendimentos")
    st.dataframe(df[["timestamp", "user_id", "intent", "sentiment", "message"]].tail(10))
