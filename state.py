user_states = {}

def start_conversation(user_id, flow_type):
    user_states[user_id] = {
        "type": flow_type,
        "step": 0,
        "responses": []
    }

def get_state(user_id):
    return user_states.get(user_id, None)

def advance_step(user_id, response):
    if user_id in user_states:
        user_states[user_id]["responses"].append(response)
        user_states[user_id]["step"] += 1

def reset_state(user_id):
    if user_id in user_states:
        del user_states[user_id]