# flows/situational.py

def get_question(step):
    questions = [
        "🧳 Are you parting ways due to life circumstances like moving, career, or family pressure?",
        "💔 Do you both still care but feel it's not practical anymore?",
        "🔁 Have you tried to make it work but keep ending up in the same place?",
        "🎯 Do you both want different things in life right now?"
    ]
    return questions[step] if step < len(questions) else None