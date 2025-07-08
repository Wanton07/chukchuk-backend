# Required Supabase table: chukchuk_logs
# Columns:
# - session_id: text
# - user_message: text
# - reply: text
# - timestamp: timestamp or text

import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME = os.getenv("SUPABASE_TABLE_NAME", "chukchuk_logs")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def log_to_supabase(data: dict):
    try:
        mapped_data = {
            "user_id": data.get("user_number"),
            "type": "whatsapp",
            "emotion": data.get("emotion_detected"),
            "responses": data.get("response"),
            "journal": data.get("journal"),
            "summary": data.get("summary"),
            "tone": data.get("tone"),
            "created_at": data.get("timestamp")
        }

        print("[Supabase] Logging data:", mapped_data)
        response = supabase.table(SUPABASE_TABLE_NAME).insert(mapped_data).execute()
        print("[Supabase] Insert response:", response)
    except Exception as e:
        print("❌ Supabase logging failed:", str(e))