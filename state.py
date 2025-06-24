import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("chukchuk-logger.json", scope)
client = gspread.authorize(creds)

sheet = client.open("ChukChuk Logs").sheet1  # <-- Your target Google Sheet name