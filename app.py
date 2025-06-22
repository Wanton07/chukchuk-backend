from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
import gspread
from datetime import datetime
import uuid

# Local modules
from state import start_conversation, get_state, advance_step, reset_state
from flows import toxic

app = Flask(__name__)

# Google Sheets setup
gc = gspread.service_account(filename="/etc/secrets/credentials.json")
workbook = gc.open("ChukChuk Logs")
session_sheet = workbook.worksheet("Session Logs")

# Toxic keywords to trigger the flow
toxic_keywords = ['toxic', 'abuse', 'gaslight', 'manipulated', 'unsafe', 'hurt me']

def detect_toxic_keywords(message):
    return any(kw in message.lower() for kw in toxic_keywords)

@app.route("/incoming", methods=["POST"])
def incoming_message():
    from_number = request.values.get('From', '')
    incoming_msg = request.values.get('Body', '').lower()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    resp = MessagingResponse()

    # Fetch session state
    state = get_state(from_number)
    session_id = f"{from_number}-pending-sess"

    # ✅ Log all incoming messages, even from unknown users
    session_sheet.append_row([
        timestamp,
        from_number,
        session_id,
        "unknown",
        "0",
        "initial",
        incoming_msg
    ])

    # Emergency escalation check
    if any(phrase in incoming_msg for phrase in ['want to die', 'end it all', 'kill myself']):
        resp.message("You’re feeling something very heavy right now 🐰. Please consider speaking to someone trained to help:\n📞 iCall Helpline (9152987821)\nYou are not alone.")
        return str(resp)

    # Start toxic flow if keywords match and no session exists
    if state is None and detect_toxic_keywords(incoming_msg):
        start_conversation(from_number, "toxic")
        first_q = toxic.get_question(0)
        reply = (
            "It sounds like you went through something hard. I’m here with care 🐰.\n"
            "Would it feel okay if I asked a few questions to understand better?\n\n" + first_q
        )
        resp.message(reply)
        return str(resp)

    # Continue toxic flow if session is ongoing
    if state and state["type"] == "toxic":
        advance_step(from_number, incoming_msg)
        current_step = get_state(from_number)["step"]

        next_q = toxic.get_question(current_step)
        if next_q:
            resp.message(next_q)
        else:
            resp.message(toxic.get_reflection())
            reset_state(from_number)

        session_id = f"{from_number}-{state['type']}-sess"
        question_asked = toxic.get_question(current_step - 1)

        session_sheet.append_row([
            timestamp,
            from_number,
            session_id,
            state["type"],
            current_step,
            question_asked,
            incoming_msg
        ])
        return str(resp)

    # Default fallback
    resp.message("Hi, I’m ChukChuk 🐰 your breakup buddy. Just tell me how you're feeling.")
    return str(resp)