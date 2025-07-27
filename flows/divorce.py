questions = [
    "⚖️ Did things feel off for a while before the separation?",
    "🛠️ Did you both try to fix things before parting ways?",
    "💬 Are there still things left unsaid that feel heavy inside you?",
    "👨‍👩‍👧 Are you worried about how this is affecting your kids or family?",
    "🔄 Do you feel more tired, clear, or just emotionally drained?",
    "🌪️ Are you scared about starting over or losing your sense of identity?",
    "🧍‍♀️ Do you feel more alone with them or without them?",
    "📚 What lessons did this relationship teach you about love or life?",
    "🚪 If you could talk to your younger self at the start of this, what would you say?",
    "🌅 What kind of peace are you hoping to feel after this chapter?"
]

replies = [
    "Divorce isn’t failure — sometimes it’s choosing peace over constant pain.",
    "Trying shows you cared. Whether or not it worked, that effort matters.",
    "Even if words were never said out loud, your feelings still matter deeply.",
    "It’s okay to care about others and still want healing for yourself.",
    "Feeling drained doesn’t mean you’re broken — it means you’ve carried a lot.",
    "Starting over is scary, but it can also be the start of something lighter.",
    "Loneliness inside a relationship can feel worse than being alone — you’re allowed to notice that.",
    "Hard times can still teach soft lessons. Your pain holds meaning.",
    "You’ve grown. And your past self did what they knew with what they had.",
    "Peace might feel far now, but every little step toward calm is still progress."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""