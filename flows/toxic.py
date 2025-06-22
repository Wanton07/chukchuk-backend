# flows/toxic.py

questions = [
    "Did you often feel unheard, disrespected, or afraid in the relationship?",
    "Can you recall one moment where you felt you lost your voice or freedom?",
    "What thought about yourself stuck with you because of how they treated you?",
    "If that thought were a friend talking to you, would you believe them?",
    "What boundary would make you feel more protected going forward?"
]

reflection_text = (
    "You’ve just made space for your voice — and I’m honored to be here with you 🐰.\n"
    "What you described shows strength. You’re starting to challenge the painful beliefs someone tried to plant in you.\n"
    "Boundaries are not walls, they’re bridges to safety."
)

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reflection():
    return reflection_text