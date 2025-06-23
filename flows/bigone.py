# flows/bigone.py

questions = [
    "How long was the relationship before it ended?",
    "Was this your first serious relationship?",
    "Were you blindsided by the breakup or did you see it coming?",
    "Do you still find yourself thinking about this person often?",
    "What part of the relationship do you miss most?",
]

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reflection():
    return (
        "Big breakups leave deep marks 💔. It’s valid to still feel the ache.\n"
        "Healing is a process — and you’re taking a brave step today 🐰.\n"
        "Let’s take this one day at a time. You're not alone."
    )