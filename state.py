user_states = {}

def start_conversation(user_id, flow_type):
    user_states[user_id] = {
        "type": flow_type,
        "step": 0,
        "responses": [],
        "emotion": None,
        "journal": "",
        "lang": "english",
        "privacy_shown": False
    }

def get_state(user_id):
    return user_states.get(user_id)

def advance_step(user_id, response):
    if user_id in user_states:
        user_states[user_id]["responses"].append(response)
        user_states[user_id]["step"] += 1

def reset_state(user_id):
    if user_id in user_states:
        del user_states[user_id]

def set_emotion(user_id, emotion):
    if user_id in user_states:
        user_states[user_id]["emotion"] = emotion

def set_journal(user_id, journal_text):
    if user_id in user_states:
        user_states[user_id]["journal"] = journal_text

def get_full_session(user_id):
    return user_states.get(user_id, {})

def set_language(user_id, lang):
    if user_id in user_states:
        user_states[user_id]["lang"] = lang


# Set the privacy_shown flag to True for a user
def set_privacy_shown(user_id):
    if user_id in user_states:
        user_states[user_id]["privacy_shown"] = True

# Get the privacy_shown status for a user
def has_shown_privacy(user_id):
    return user_states.get(user_id, {}).get("privacy_shown", False)