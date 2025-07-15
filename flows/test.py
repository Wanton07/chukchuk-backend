def get_question(step):
    questions = [
        "🧪 This is just a test. What emotion are you simulating?",
        "🔁 Do you feel stuck in a loop around this issue?",
        "💬 What's one thought you're testing journaling for?"
    ]
    if step < len(questions):
        return questions[step]
    return get_feedback_prompt()

def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""