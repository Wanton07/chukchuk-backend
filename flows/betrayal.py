questions = [
    "💔 What did they break — your trust, loyalty, or something even deeper?",
    "🎯 Was it just one time, or has it happened more than once?",
    "😶 Did you find out because they told you, or did you discover it yourself?",
    "🧩 What hurts more — what they did or that they kept it from you?",
    "🌪️ Has this changed how safe you feel in relationships overall?",
    "🧠 Do you keep thinking about the moment you found out?",
    "🧱 What’s harder to let go of — the past or what might come next?",
    "🌙 Do you ever secretly wonder if it was somehow your fault?",
    "🛡️ What boundary do you wish you had now to feel more protected?",
    "🌄 If healing was a picture in your mind, what would it look like?"
]

replies = [
    "Betrayal isn’t just about broken promises — it can shake your whole world.",
    "If it’s a pattern, your feelings are not overreacting — they’re trying to protect you.",
    "How you found out matters. It hurts when truth has to be uncovered, not offered.",
    "Keeping things hidden makes it hurt even more. You're allowed to feel angry and sad.",
    "It’s okay to feel unsafe now. You’re not weak — you’re healing.",
    "Your mind might keep going back to that moment. That’s normal when trust breaks.",
    "Letting go doesn’t mean forgetting. It means choosing your peace.",
    "Even if you blame yourself sometimes, this was not your fault.",
    "You deserve boundaries that make you feel respected and calm.",
    "Healing isn’t a straight road. But just wanting to heal is a powerful first step."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""