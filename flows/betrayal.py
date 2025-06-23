# flows/betrayal.py

questions = [
    "Did you find out directly from your partner, or someone else?",
    "Was it a one-time mistake or something ongoing?",
    "How did you confront or address the situation?",
    "Do you feel betrayed more by the action or the secrecy?",
    "What would you need to feel safe and trusted again?"
]

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reflection():
    return (
        "Betrayal cuts deep—it shakes the foundation of any bond 😔.\n"
        "It’s okay to feel hurt, angry, confused.\n"
        "You’re not alone—and taking time to understand your emotions is courageous 🐰.\n"
        "Healing doesn’t mean forgetting, it means reclaiming your peace."
    )