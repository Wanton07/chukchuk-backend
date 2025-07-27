questions = [
    "💣 Do you ever feel scared or nervous when you're around them?",
    "🧍 Do you sometimes feel lonely, even when they’re sitting right next to you?",
    "🪤 Have they made you second-guess your own thoughts or memories?",
    "🚨 Do you stop yourself from being honest just to avoid upsetting them?",
    "🧨 Have they ever said hurtful things or tried to control you?",
    "🫥 Do you feel like you’ve lost your confidence or parts of who you are?",
    "🌀 When they say sorry, does it feel real — or do the same things keep happening?",
    "📉 Has this relationship made you feel small or not good enough?",
    "🧭 If someone you loved was going through this, what would you want to tell them?",
    "🌱 In your heart, what would feeling truly safe and respected in love look like?"
]

replies = [
    "Feeling unsafe around someone isn’t love — it’s a sign something’s off.",
    "Being alone together can feel worse than being alone — your feelings matter.",
    "Doubting yourself over time takes a toll. You deserve to trust your truth.",
    "Hiding your feelings to avoid conflict is exhausting — you shouldn’t have to.",
    "No one should try to control or belittle you. That’s not love, that’s harm.",
    "Losing parts of yourself is a sign it’s not healthy. You can begin to reclaim who you are.",
    "Real apologies lead to change. Without that, they’re just words.",
    "You are enough, and always have been — this pain doesn’t define you.",
    "What you’d say to someone else in this situation might be what you need to hear too.",
    "Love should feel safe, calm, and kind — that’s what you deserve."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()

def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""