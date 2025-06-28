questions = [
    "🧭 What external factor made this relationship difficult — distance, timing, family?",
    "🕓 If circumstances had been different, do you think this would’ve worked?",
    "💬 Did you talk openly about the situation, or avoid it out of fear?",
    "📆 Was this a slow drift or a sudden ending?",
    "⏳ Are you waiting for ‘someday’ to try again?",
    "🎢 Do you feel emotionally stuck in a loop of what-ifs?",
    "🌱 What did this relationship help you discover about your needs?",
    "🧃 What were the sweetest moments that still linger in your heart?",
    "📉 What signs showed it wasn’t sustainable — even if it was beautiful?",
    "🦋 What would it look like to carry the love, but not the ache?"
]

replies = [
    "Situational pain is valid. Sometimes the world doesn’t align with the heart.",
    "You can honor both: what could’ve been and what is.",
    "Avoidance often protects the moment, but wounds the future.",
    "Slow fades hurt deeply — they confuse closure.",
    "Waiting keeps you in pause. What if clarity moved you forward?",
    "Loops are not lessons. Let’s help you step out.",
    "Even brief love can be a teacher. You’re growing from this.",
    "Sweetness doesn’t cancel out reality — it simply lives alongside it.",
    "Beauty without stability is still painful. It’s okay to let it go.",
    "You can carry the love, but leave the weight behind."
]
def get_question(step):
    return questions[step] if step < len(questions) else None