from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

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

from flows import toxic, bigone, divorce, unrequited, betrayal, situational, ghosted, notsure, test

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
    "9": ("Test Flow 🧪", test)
}

@app.route("/incoming", methods=["POST"])
def incoming():
    user_id = request.form.get("From")
    user_message = request.form.get("Body", "").strip()

    response = MessagingResponse()

    if user_message.lower() == "privacy":
        response.message(
            "🔐 *Your Privacy Matters*\n\n"
            "Everything you share with ChukChuk stays between us.\n"
            "We don’t store personal identifiers, and your reflections are never used to train any model.\n"
            "Type `delete` anytime to clear your session.\n\n"
            "Your journey, your control. 🧘‍♂️"
        )
        return str(response)

    if user_message.lower() == "delete":
        reset_state(user_id)
        response.message("🧹 Your session has been cleared.\nYou can start again anytime by choosing a breakup type.")
        return str(response)

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
                "8️⃣ Not sure 🤔\n"
                "9️⃣ Test Flow 🧪 (for development only)\n\n"
                "Reply with a number to begin."
            )
            response.message(menu)
        return str(response)

    # If user already in conversation
    if state["type"] == "9":
        max_steps = 3
    else:
        max_steps = 10

    if state["step"] < max_steps:
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

    # Journal response (after last question in flow)
    if state["journal"] == "":
        set_journal(user_id, user_message)

        summary_prompt = f"""Summarize this journal with 3 calming points and identify the emotional tone (e.g., hopeful, regretful, confused, angry, peaceful). 
1. Validate the feelings.
2. Reflect one key theme.
3. Offer a non-judgmental insight.
4. Tone (one word): ?

Journal:
{user_message}"""

        try:
            completion = openai.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": summary_prompt}]
            )
            summary = completion.choices[0].message.content.strip()
            lines = summary.splitlines()
            tone_line = next((line for line in lines if "Tone" in line), "")
            tone = tone_line.split(":")[-1].strip() if ":" in tone_line else "Unknown"
            summary = "\n".join([line for line in lines if "Tone" not in line]).strip()
            # Store the tone in the session for logging
            full_session = get_full_session(user_id)
            full_session["tone"] = tone
            # Gen Z tone customization
            if tone.lower() in ["confused", "anxious", "overwhelmed", "stressed", "lost", "numb"]:
                summary = summary.replace(
                    "🐰 Here's a soft reflection:",
                    "🐰 Real talk time: Let’s unpack this 💬"
                )
            response.message(f"🐰 Here's a soft reflection:\n\n{summary}")
        except Exception as e:
            summary = "🐰 I read that. Just a small glitch while summarizing, but I’ve noted what you wrote 🧠"
            tone = "Unknown"
            # Still try to log the tone as "Unknown"
            full_session = get_full_session(user_id)
            full_session["tone"] = tone
            response.message(summary)

        # Log full session
        # Use the tone from full_session, not the local variable
        sheet.append_row([
            user_id,
            full_session["type"],
            full_session["emotion"],
            "\n".join(full_session["responses"]),
            full_session["journal"],
            summary,
            full_session["tone"]
        ])
        reset_state(user_id)
        return str(response)

    # Fallback
    reset_state(user_id)
    response.message("🐰 I'm here with you. Just say 'hi' or pick a breakup type again.")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)