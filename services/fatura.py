def gerar_segunda_via(user_id: str):
    return {
        "user_id": user_id,
        "link": f"https://claro.com/fatura/{user_id}"
    }
