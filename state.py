user_states = {}

def start_conversation(user_id, flow_type):
    user_states[user_id] = {
        "type": flow_type,
        "step": 0,
        "responses": [],
        "emotion": None,
        "journal": "",
        "lang": "english"
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