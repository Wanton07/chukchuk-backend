questions = [
    "🌍 Was it distance, timing, family — or something else that pulled you apart?",
    "🔄 Do you think it could have worked if life had been different?",
    "💬 Did you talk honestly about what was happening, or keep things inside?",
    "📆 Did it end suddenly or drift apart over time?",
    "⏳ Are you still hoping that someday you’ll be back together?",
    "🎢 Are you stuck replaying ‘what ifs’ in your mind?",
    "🌱 What did this relationship teach you about what you really need?",
    "💖 What’s one memory that still brings you warmth?",
    "🚧 Were there signs it wasn’t working, even if it felt special?",
    "🕊️ What would it feel like to let go without letting go of the love?"
]

replies = [
    "Life gets in the way sometimes — and that doesn’t make your love any less real.",
    "It’s okay to grieve the version of this story that never got written.",
    "Holding it in can feel easier, but you deserve open, honest conversations.",
    "Slow endings can leave big feelings. Closure takes time.",
    "Hoping is human — but clarity helps you move forward.",
    "‘What ifs’ keep you stuck. Let’s help you find the ‘what now.’",
    "Even a short chapter can teach big things about your heart.",
    "It’s okay to treasure the sweet parts while letting go of the ache.",
    "Just because it felt magical doesn’t mean it could last — and that’s okay.",
    "You can carry love forward, even without carrying the pain with it."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


# Feedback prompt function
def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""