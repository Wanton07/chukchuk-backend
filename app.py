from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
import gspread

from state import start_conversation, get_state, advance_step, reset_state
from flows import toxic, bigone, divorce, unrequited, betrayal, situational, ghosted, notsure

app = Flask(__name__)

# Google Sheets
gc = gspread.service_account(filename="/etc/secrets/credentials.json")
workbook = gc.open("ChukChuk Logs")
session_sheet = workbook.worksheet("Session Logs")

flow_map = {
    "1": ("Toxic or Abusive", toxic),
    "2": ("Big Emotional Breakup", bigone),
    "3": ("Separation or Divorce", divorce),
    "4": ("Unrequited Love", unrequited),
    "5": ("Betrayal or Cheating", betrayal),
    "6": ("Situational Breakup", situational),
    "7": ("Ghosted or No Closure", ghosted),
    "8": ("Not Sure", notsure)
}

def log_row(timestamp, from_number, session_id, flow_type, step, question, answer):
    session_sheet.append_row([
        timestamp, from_number, session_id, flow_type, step, question, answer
    ])

@app.route("/incoming", methods=["POST"])
def incoming_message():
    from_number = request.values.get('From', '')
    incoming_msg = request.values.get('Body', '').strip().lower()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    resp = MessagingResponse()

    # 🆘 Escalation check
    if any(x in incoming_msg for x in ["want to die", "kill myself", "end it all"]):
        resp.message("You’re feeling something very heavy right now 🐰.\nPlease consider speaking to someone trained to help:\n📞 iCall Helpline (9152987821)\nYou are not alone.")
        return str(resp)

    # 🧠 Get user state
    state = get_state(from_number)

    # 🌱 If no flow started yet
    if state is None:
        if incoming_msg in flow_map:
            flow_type, flow = flow_map[incoming_msg]
            start_conversation(from_number, incoming_msg)
            question = flow.get_question(0)
            resp.message(
                f"Okay, we’ll take it slow 🐰\nLet’s start your **{flow_type}** flow.\n\n{question}"
            )
            return str(resp)
        else:
            # 🐣 Greeting menu
            greeting = (
                "Hi there, I’m ChukChuk 🐰 — your breakup buddy.\n"
                "Whatever you're feeling, I’m here to help.\n\n"
                "**What kind of breakup are you going through?**\n\n"
                "1️⃣ Toxic or abusive 💔\n"
                "2️⃣ A big emotional breakup 💞\n"
                "3️⃣ Separation or divorce ⚖️\n"
                "4️⃣ Unrequited love 😢\n"
                "5️⃣ Betrayal or cheating 😔\n"
                "6️⃣ Situational breakup (LDR, timing) 🌍\n"
                "7️⃣ Ghosted or no closure 👻\n"
                "8️⃣ Not sure 🤔\n\n"
                "_Reply with a number to begin._"
            )
            resp.message(greeting)
            return str(resp)

    # 🔁 Continue CBT Flow
    flow_id = state["type"]
    flow_type, flow = flow_map[flow_id]
    step = state["step"]

    # Log previous response
    question = flow.get_question(step - 1)
    log_row(timestamp, from_number, f"{from_number}-{flow_type}", flow_type, step, question, incoming_msg)

    # Advance and reply
    advance_step(from_number, incoming_msg)
    new_step = get_state(from_number)["step"]
    next_q = flow.get_question(new_step)

    if next_q:
        resp.message(next_q)
    else:
        resp.message(flow.get_reflection())
        reset_state(from_number)

    return str(resp)