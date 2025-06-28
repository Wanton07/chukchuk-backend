questions = [
    "👻 Did the silence feel sudden or was it slowly growing?",
    "🧠 Are you stuck asking why, without any real answer?",
    "💬 Did you try reaching out after being ghosted? What happened?",
    "📉 How has this experience affected your self-worth?",
    "🔎 Are you blaming yourself for their silence?",
    "🌪️ Does the lack of closure keep pulling you back emotionally?",
    "🛑 What would you say to them now if they actually listened?",
    "📱 Does seeing their profile or presence online trigger you?",
    "🧭 What does closure look like when the other person won’t offer it?",
    "🌤️ What small truth helps you breathe a little easier right now?"
]

replies = [
    "Ghosting feels like emotional theft. You deserved better communication.",
    "The brain craves reasons. But silence doesn’t mean it was your fault.",
    "Reaching out shows your heart — their response shows their character.",
    "Your value isn’t tied to someone else’s absence.",
    "You’re not the reason they vanished. That’s their unfinished work.",
    "Closure isn’t something they give — it’s something you build.",
    "Even imagined conversations help heal. Speak your truth.",
    "Triggers are data, not weakness. Let’s use them gently.",
    "You don’t need their words to move on. Your own voice is enough.",
    "You’re healing in silence what they didn’t even face. That’s power."
]
def get_question(step):
    return questions[step] if step < len(questions) else None