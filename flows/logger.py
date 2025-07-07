

import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
SUPABASE_TABLE_NAME = os.getenv("SUPABASE_TABLE_NAME", "chukchuk_logs")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

def log_to_supabase(data: dict):
    try:
        print("[Supabase] Logging data:", data)
        response = supabase.table(SUPABASE_TABLE_NAME).insert(data).execute()
        print("[Supabase] Insert response:", response)
    except Exception as e:
        print("❌ Supabase logging failed:", str(e))