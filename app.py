from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import gspread
import json
import os
from datetime import datetime

app = Flask(__name__)

# Google Sheets Auth – load from Render Secret File
gc = gspread.service_account(filename="/etc/secrets/credentials.json")
sheet = gc.open("ChukChuk Logs").sheet1

@app.route("/incoming", methods=["POST"])
def incoming_message():
    incoming_msg = request.values.get('Body', '').lower()
    from_number = request.values.get('From', '')

    if "lost" in incoming_msg:
        reply = "Hey, you're not alone. It’s okay to feel this way. I’m right here with you 🐰💛"
    elif "breakup" in incoming_msg:
        reply = "Breakups are painful. But healing is possible. I'm your breakup buddy 🐰 and I’m here to help."
    elif "hi" in incoming_msg or "hello" in incoming_msg:
        reply = "Hi, I’m ChukChuk 🐰 Your breakup buddy. Tell me how you're feeling today."
    else:
        reply = "I’m listening, always. Just let it out 🐰💬"

    # Respond to WhatsApp
    resp = MessagingResponse()
    resp.message(reply)

    # Log to Google Sheet
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, from_number, incoming_msg, reply])

    return str(resp)