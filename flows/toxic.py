questions = [
    "💣 Have there been moments when fear or anxiety felt normal in this relationship?",
    "🧍 Do you often feel isolated or unsupported, even when they’re physically present?",
    "🪤 Have you ever felt manipulated or made to doubt your reality (gaslighting)?",
    "🚨 Do you walk on eggshells or filter your truth to avoid their reactions?",
    "🧨 Have threats, name-calling, or control over your choices been present?",
    "🫥 Have you lost parts of your personality or confidence over time?",
    "🌀 Do apologies feel sincere or part of a repeated cycle?",
    "📉 Is your self-worth mostly impacted *because* of this relationship?",
    "🧭 If a loved one were in this relationship, what would you tell them?",
    "🌱 What does emotional safety look and feel like to you?"
]

replies = [
    "Noticing fear patterns is a big deal. Safety is a basic need, not a bonus.",
    "Emotional loneliness in a relationship can be louder than physical distance.",
    "Trusting your perception again is part of healing. You're not crazy — you're careful.",
    "Filtering yourself is a survival response. But long-term, it exhausts your truth.",
    "Toxic behaviors are not 'just fights' — they're data. You deserve peace.",
    "Feeling lost or small isn’t your fault. It’s okay to start reclaiming yourself.",
    "When words don’t match actions, patterns speak. You’re learning to see it clearly.",
    "Your worth is not up for negotiation. Let’s rebuild that from within.",
    "You often know the truth when imagining it happening to someone you love.",
    "Safety is the soil where love grows. Let’s start from there."
]
def get_question(step):
    return questions[step] if step < len(questions) else None