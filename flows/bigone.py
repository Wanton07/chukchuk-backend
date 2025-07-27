questions = [
    "💔 What feeling has been the hardest to carry since the breakup?",
    "📸 Do your good memories with them make it harder to let go?",
    "🗣️ Did you get a chance to have one last honest conversation?",
    "🔁 Do you keep replaying things in your head, wondering what went wrong?",
    "⚖️ Do your feelings go back and forth between missing them and feeling hurt?",
    "✍️ Have you written them a message, even if you never sent it?",
    "🛌 Have you been sleeping okay or has your routine been off?",
    "🔮 Is it hard to picture a happy future without them in it?",
    "💬 What’s one thing you wish they truly understood about you?",
    "🌱 Is there even one small part of you that feels like it’s starting to heal?"
]

replies = [
    "That heavy feeling deserves care — you don’t have to carry it alone.",
    "Good memories can feel like anchors. You're not wrong for missing the good times.",
    "Closure can help, but sometimes we carry words we never got to say. It’s okay.",
    "It’s natural to rewind everything in your mind — you’re just trying to understand.",
    "Mixed emotions are normal. You’re healing, even if it doesn’t feel like it yet.",
    "Writing things out can be healing, even if no one else reads it.",
    "Breakups can shake your routine. Be gentle with yourself right now.",
    "It’s okay if the future feels blurry. You’re still finding your new path.",
    "Wanting to be understood is human. You deserve to be seen deeply.",
    "Noticing even a tiny shift toward healing is a big deal. You’re getting there."
]

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reply(step):
    if step < len(replies):
        return replies[step]
    return get_feedback_prompt()

def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""