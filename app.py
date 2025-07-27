from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
from datetime import datetime
from supabase import create_client
import traceback

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

def handle_feedback_reply(user_input):
    input_lower = user_input.lower().strip()

    if input_lower == "a":
        return "🐰 I’m really glad you feel lighter. Take your time and I’ll be here if you need to talk again. 💙", "lighter", False
    elif input_lower == "b":
        return "🐰 I understand. Sometimes clarity takes more than one conversation. Would you like to try another path or take a break?", "confused", False
    elif input_lower == "c":
        return "🐰 Thank you for sharing. I’ve noted that you may want to talk to someone real. Sending you a virtual hug. 🤗", "escalate", True
    else:
        return None, None, None

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_path = os.getenv("GOOGLE_CREDS_JSON_PATH")
if not creds_path:
    raise EnvironmentError("⚠️ GOOGLE_CREDS_JSON_PATH not found in environment variables.")

with open(creds_path, "r") as f:
    creds_dict = json.load(f)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open("ChukChuk Session Logs").sheet1

# Supabase initialization
SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip()
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY", "").strip()
SUPABASE_TABLE = os.getenv("SUPABASE_TABLE_NAME")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

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

    response_text, mood, escalate = handle_feedback_reply(user_message)
    if response_text:
        state = get_state(user_id) or {}
        # Append feedback to Google Sheet for now
        sheet.append_row([
            user_id,
            "feedback",
            mood,
            "ESCALATE" if escalate else "",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ])
        try:
            supabase.table("user_testing_feedback").insert({
                "tester_name": user_id,
                "flow_picked": flows.get(state.get("type", ""), ["unknown"])[0],
                "stuck_at_step": None,
                "feedback_choice": mood,
                "drop_off_point": False,
                "final_mood_emoji": "",
                "comments": "",
                "created_at": datetime.now().isoformat()
            }).execute()
        except Exception as e:
            traceback.print_exc()
            print("❌ Supabase feedback logging failed:", e)
        response.message(response_text)
        return str(response)

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

    if user_message.lower() == "delete today":
        today = datetime.now().strftime("%Y-%m-%d")
        records = sheet.get_all_records()
        deleted = False
        for idx, row in enumerate(records, start=2):  # skip header
            if row.get("user_id") == user_id and row.get("timestamp") == today:
                sheet.delete_row(idx)
                deleted = True
                break
        if deleted:
            response.message("🗑️ Today's session logs have been deleted. The rest of your reflections are still safe.")
        else:
            response.message("📅 No logs found for today under your ID.")
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
        # Simple invalid input fallback filter
        if len(user_message.strip()) <= 2 and user_message.lower() not in ["yes", "no", "maybe", "idk", "ok"]:
            response.message("🐰 Hmm, I didn’t quite catch that. Want to continue or choose another path? Just reply again.")
            return str(response)
        flow_module = flows[state["type"]][1]
        reply = flow_module.replies[state["step"]] if state["step"] < len(flow_module.replies) else None

        if reply:
            response.message(reply)

        advance_step(user_id, user_message)
        next_question = flow_module.get_question(state["step"])

        if next_question:
            response.message(next_question)
        else:
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

        # Log full session to Supabase and Google Sheets as backup
        try:
            # Log to Supabase
            supabase.table(SUPABASE_TABLE).insert({
                "user_id": user_id,
                "type": full_session["type"],
                "emotion": full_session["emotion"],
                "responses": "\n".join(full_session["responses"]),
                "journal": full_session["journal"],
                "summary": summary,
                "tone": full_session["tone"],
                "created_at": datetime.now().isoformat()
            }).execute()
        except Exception as e:
            traceback.print_exc()
            print("❌ Supabase logging failed:", e)

        # Also log to Google Sheets as backup
        sheet.append_row([
            user_id,
            full_session["type"],
            full_session["emotion"],
            "\n".join(full_session["responses"]),
            full_session["journal"],
            summary,
            full_session["tone"],
            datetime.now().strftime("%Y-%m-%d")
        ])
        reset_state(user_id)
        return str(response)

    # Fallback
    reset_state(user_id)
    response.message("🐰 I'm here with you. Just say 'hi' or pick a breakup type again.")
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)