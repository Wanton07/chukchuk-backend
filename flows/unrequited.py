questions = [
    "😔 How long have you carried feelings that weren’t returned?",
    "🎢 Have they given mixed signals or been clear about their stance?",
    "🎭 Do you ever feel like you’re performing to win their attention?",
    "🪞 How has this dynamic affected your self-esteem or confidence?",
    "🔄 Do you keep hoping something might change, or do you know deep down?",
    "🧘 What kind of love do you want — mutual, calm, and certain?",
    "🧃 Have you been romanticizing moments that were never fully real?",
    "🔒 Have you felt stuck, waiting for their emotional availability?",
    "🌅 What would it feel like to open space for someone who chooses you?",
    "📣 What do you need to hear right now to let go, even a little?"
]

replies = [
    "Longing is real pain. It deserves just as much space as any breakup.",
    "Mixed signals create confusion, not chemistry. You deserve clarity.",
    "You shouldn’t have to prove your worth to be loved.",
    "Your value doesn’t shrink because someone didn’t see it.",
    "The quiet truth you carry deserves to be honored gently.",
    "Love should feel safe and shared. Let’s start with wanting *that*.",
    "It’s okay to admit what was imagined. Closure starts with honesty.",
    "Stuckness is your cue. You don’t need permission to move forward.",
    "Being chosen — fully and freely — is worth waiting for.",
    "Sometimes, healing starts with giving yourself the goodbye they never gave."
]
def get_question(step):
    return questions[step] if step < len(questions) else None