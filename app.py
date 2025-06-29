from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from datetime import datetime

from state import (
    start_conversation,
    get_state,
    advance_step,
    reset_state,
    set_emotion,
    set_journal,
    get_full_session
)
from emotion import detect_emotion

from flows import toxic, bigone, divorce, unrequited, betrayal, situational, ghosted, notsure

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_dict = json.loads(os.getenv("GOOGLE_CREDS_JSON"))
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("ChukChuk Session Logs").sheet1

app = Flask(__name__)

flows = {
    "1": ("Toxic or abusive 💔", toxic),
    "2": ("A big emotional breakup 💞", bigone),
    "3": ("Separation or divorce ⚖️", divorce),
    "4": ("Unrequited love 😢", unrequited),
    "5": ("Betrayal or cheating 😔", betrayal),
    "6": ("Situational breakup 🌍", situational),
    "7": ("Ghosted or no closure 👻", ghosted),
    "8": ("Not sure 🤔", notsure),
}

@app.route("/incoming", methods=["POST"])
def incoming():
    user_id = request.form.get("From")
    user_message = request.form.get("Body", "").strip()
    response = MessagingResponse()
    state = get_state(user_id)

    if not state:
        if user_message in flows:
            flow_title, flow_module = flows[user_message]
            start_conversation(user_id, user_message)
            emotion = detect_emotion(user_message)
            set_emotion(user_id, emotion)
            question = flow_module.get_question(0)
            response.message(f"Okay, we’ll take it slow 🐰\nLet’s start your *{flow_title}* flow.\n\n{question}")
        else:
            menu = (
                "Hi there, I’m ChukChuk 🐰 — your breakup buddy.\n"
                "Whatever you're feeling, I’m here to help.\n\n"
                "*What kind of breakup are you going through?*\n\n"
                "1️⃣ Toxic or abusive 💔\n"
                "2️⃣ A big emotional breakup 💞\n"
                "3️⃣ Separation or divorce ⚖️\n"
                "4️⃣ Unrequited love 😢\n"
                "5️⃣ Betrayal or cheating 😔\n"
                "6️⃣ Situational breakup 🌍\n"
                "7️⃣ Ghosted or no closure 👻\n"
                "8️⃣ Not sure 🤔\n\n"
                "Reply with a number to begin."
            )
            response.message(menu)
        return str(response)

    # If user already in conversation
    if state["step"] < 10:
        advance_step(user_id, user_message)
        next_question = flows[state["type"]][1].get_question(state["step"])

        if next_question:
            response.message(next_question)
        else:
            # After 10 steps, prompt for journal
            response.message(
                "🐰 You’ve completed this clarity path.\nIf you’d like, write a few lines about how you're feeling now. I’ll reflect it back gently."
            )
        return str(response)

    # Journal response (after 10 questions)
    if state["journal"] == "":
        set_journal(user_id, user_message)

        summary_prompt = f"""Summarize this journal with 3 calming points:\n1. Validate the feelings.\n2. Reflect one key theme.\n3. Offer a non-judgmental insight.\n\nJournal:\n{user_message}"""
        summary = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": summary_prompt}]
        ).choices[0].message.content.strip()

        response.message(f"🐰 Here's a soft reflection:\n\n{summary}")

        # Log full session
        full_session = get_full_session(user_id)
        sheet.append_row([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp
            user_id,                                       # Twilio ID
            request.form.get("WaId", ""),                  # Phone number
            full_session["type"],                          # Clarity path type
            full_session["emotion"],                       # Detected emotion
            "\n".join(full_session["responses"]),          # Collected responses
            full_session["journal"],                       # Journal text
            summary                                        # GPT summary
        ])
        reset_state(user_id)
        return str(response)

    # Fallback
    response.message("🐰 I'm here with you. Just say 'hi' or pick a breakup type again.")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)