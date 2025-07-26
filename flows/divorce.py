questions = [
    "⚖️ What has changed emotionally or practically that led to this point?",
    "🛠️ Did you both try healing efforts — counseling, conversations, time apart?",
    "💬 What’s left unsaid between you two that still feels heavy?",
    "👨‍👩‍👧 If there are kids involved, how has their presence shaped your choices?",
    "🔄 Is this decision coming from exhaustion, clarity, or survival?",
    "🌪️ Are you afraid of starting over, or losing identity tied to this relationship?",
    "🧍‍♀️ Do you feel more alone *with* them or *without* them?",
    "📚 What lessons do you think this relationship taught you?",
    "🚪What do you wish someone told you at the start of this marriage?",
    "🌅 What kind of peace are you hoping for after this chapter?"
]

replies = [
    "Divorce isn’t failure — it’s often a final chapter after long battles.",
    "Trying shows you cared. Whether or not it worked, your effort matters.",
    "Unspoken words carry weight. Sometimes just naming them brings relief.",
    "Parenting adds complex layers. You’re allowed to want clarity for yourself too.",
    "Clarity is gold. Exhaustion shows the cost you’ve paid to get here.",
    "Grief and fear often come before growth. It’s okay to not feel ready.",
    "Loneliness can exist even in company. You’re learning to honor that truth.",
    "Lessons don’t erase pain, but they add meaning to it.",
    "Reflection shows growth. Your younger self did the best they could.",
    "You deserve calm, ease, and soft mornings. That’s not too much to ask."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""