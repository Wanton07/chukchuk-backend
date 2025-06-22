from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import gspread
from datetime import datetime

# Local modules
from state import start_conversation, get_state, advance_step, reset_state
from flows import toxic

app = Flask(__name__)

# Google Sheets setup
gc = gspread.service_account(filename="/etc/secrets/credentials.json")
sheet = gc.open("ChukChuk Logs").sheet1

# Keywords to trigger Toxic flow
toxic_keywords = ['toxic', 'abuse', 'gaslight', 'manipulated', 'unsafe', 'hurt me']

def detect_toxic_keywords(message):
    return any(kw in message.lower() for kw in toxic_keywords)

@app.route("/incoming", methods=["POST"])
def incoming_message():
    from_number = request.values.get('From', '')
    incoming_msg = request.values.get('Body', '').lower()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    resp = MessagingResponse()

    # ESCALATION CHECK
    if any(phrase in incoming_msg for phrase in ['want to die', 'end it all', 'kill myself']):
        resp.message("You’re feeling something very heavy right now 🐰. Please consider speaking to someone trained to help:\n📞 iCall Helpline (9152987821)\nYou are not alone.")
        return str(resp)

    # STATE CHECK
    state = get_state(from_number)

    # START TOXIC FLOW
    if state is None and detect_toxic_keywords(incoming_msg):
        start_conversation(from_number, "toxic")
        first_q = toxic.get_question(0)
        reply = (
            "It sounds like you went through something hard. I’m here with care 🐰.\n"
            "Would it feel okay if I asked a few questions to understand better?\n\n" + first_q
        )
        resp.message(reply)
        return str(resp)

    # CONTINUE TOXIC FLOW
    if state and state["type"] == "toxic":
        advance_step(from_number, incoming_msg)
        current_step = get_state(from_number)["step"]

        next_q = toxic.get_question(current_step)
        if next_q:
            resp.message(next_q)
        else:
            resp.message(toxic.get_reflection())
            reset_state(from_number)

        # ✅ Log to Google Sheet
        sheet.append_row([timestamp, from_number, "toxic", f"Step {current_step}", incoming_msg])
        return str(resp)

    # DEFAULT FALLBACK
    resp.message("Hi, I’m ChukChuk 🐰 your breakup buddy. Just tell me how you're feeling.")
    return str(resp)