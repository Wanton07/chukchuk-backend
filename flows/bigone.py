questions = [
    "💔 This seems like a really big decision. What made you feel it's time to reflect on this relationship?",
    "🧱 What kind of emotional foundation has this relationship been built on — love, fear, obligation?",
    "📊 Over time, what has increased and what has decreased — trust, respect, closeness?",
    "⛅ Do you often feel more peaceful or more anxious when thinking of them?",
    "🪞 In this relationship, do you feel seen and accepted for who you truly are?",
    "🎭 Are there parts of yourself you’ve hidden just to keep the peace or avoid conflict?",
    "🔁 Are there any repetitive patterns (fights, silences, doubts) that have worn you down?",
    "🧩 When you imagine life without this relationship, what feelings come up first?",
    "📉 If nothing changed in this relationship for the next 2 years, how would that impact you?",
    "🔓 What does freedom or growth look like for you on the other side of this clarity?"
]

replies = [
    "You’re taking a strong first step by pausing to reflect. Let’s look at what’s underneath.",
    "Naming the emotional base can help you understand why it feels so heavy. You're doing deep work.",
    "Patterns matter. Seeing what’s grown or faded helps make things more real — and less confusing.",
    "Your nervous system often knows first. Let’s listen to it gently, without judgment.",
    "Being seen is a need, not a luxury. Let’s explore what’s been missing.",
    "You shouldn’t have to shrink to fit. Let's name what you've been holding back.",
    "You deserve relationships that evolve, not repeat. Let’s break down these cycles.",
    "Those first feelings are important data. You don't need to act — just notice for now.",
    "Time helps measure clarity. Imagining the future helps your inner voice speak up.",
    "That vision of freedom is powerful. Let’s walk toward it step by step, with care."
]

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reply(step):
    if step < len(replies):
        return replies[step]
    return "Thank you for sharing. This is the end of this reflection path. I'm here if you want to explore more."