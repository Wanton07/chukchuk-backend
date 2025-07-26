questions = [
    "💔 What was broken — trust, loyalty, promises, or something deeper?",
    "🎯 Was it a one-time incident or a pattern of betrayal?",
    "😶 Did you find out through them or on your own?",
    "🧩 What part of the betrayal hurts most — the act or the hiding?",
    "🌪️ How has this impacted your sense of safety in relationships?",
    "🧠 Do you replay the moment it happened over and over?",
    "🧱 What do you fear about letting go — the past or what comes next?",
    "🌙 Do you ever blame yourself, even secretly?",
    "🛡️ What kind of boundary or clarity would protect you now?",
    "🌄 What does healing from this betrayal look like in your life?"
]

replies = [
    "Betrayal isn’t just about broken promises — it shatters emotional reality.",
    "Patterns speak louder than apologies. You’re allowed to notice them.",
    "How you found out matters. Truth delayed still cuts.",
    "Hiding truth deepens the cut. Your pain makes complete sense.",
    "Safety can take years to rebuild — you’re not weak for needing that.",
    "Replaying is the mind's way to make sense of chaos. You’re not stuck.",
    "Letting go isn’t forgetting — it’s choosing peace over pain.",
    "Blame is a trauma echo. It belongs to them, not you.",
    "Boundaries aren’t walls — they’re bridges to self-respect.",
    "Healing isn’t linear. But it begins with saying: I didn’t deserve that."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""