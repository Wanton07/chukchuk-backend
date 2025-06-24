import json
import base64
import os
from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from base64 env var
creds_json = os.environ.get("GOOGLE_CREDENTIALS_B64")
if not creds_json:
    raise Exception("Missing GOOGLE_CREDENTIALS_B64 in environment variables")

creds_dict = json.loads(base64.b64decode(creds_json))
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# Sheet connection (optional fallback sheet name here)
sheet = client.open("ChukChuk Logs").sheet1