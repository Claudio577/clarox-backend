import json
from datetime import datetime

LOG_FILE = "data/logs.json"

def save_log(user_id: str, intent: str, sentiment: str, message: str):
    entry = {
        "user_id": user_id,
        "intent": intent,
        "sentiment": sentiment,
        "message": message,
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
