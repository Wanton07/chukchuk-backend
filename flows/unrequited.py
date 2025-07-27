questions = [
    "💔 Did you ever tell them how you really felt?",
    "❓ Were they clear about their feelings, or did they send mixed signals?",
    "🌈 Do you imagine what it would’ve been like if things had worked out?",
    "🪞 Do you find yourself comparing to the person they chose or liked?",
    "🎭 Are you in love with them — or the idea of being with them?",
    "😔 Has this made you feel unsure or less confident about yourself?",
    "📓 Have you ever written down how you feel, even just for yourself?",
    "🔁 Are you hoping they’ll still change their mind?",
    "🗣️ What do your close friends say about all this?",
    "🌤️ What’s one kind thought you can give yourself to feel even a little better?"
]

replies = [
    "It’s brave to admit your feelings — even if they weren’t returned.",
    "Mixed signals create more pain than peace. You deserve honesty.",
    "Dreaming about 'what could’ve been' is part of letting go.",
    "Comparing yourself will only steal your peace. You are enough.",
    "Sometimes it’s the idea we hold onto, more than the person.",
    "This doesn’t make you less worthy — your heart just needed space.",
    "Journaling or writing can help release what’s been stuck inside.",
    "It’s okay to hope — just don’t lose yourself waiting.",
    "Your friends see you clearly. Sometimes they reflect what we miss.",
    "Even one soft thought for yourself is a sign of healing."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()

def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""