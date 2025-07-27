questions = [
    "🤔 Are your feelings all mixed up — like guilt, hope, fear, or confusion?",
    "🔄 Do you keep thinking about ending things, or does it come and go?",
    "🎭 Do you feel like you’re fully yourself when you’re with them?",
    "🧘 When you picture staying vs. leaving, how does your body feel?",
    "🎢 Does this relationship feel calm, joyful, or more like a rollercoaster?",
    "🪞 Are you in love with them — or with who you hope they’ll become?",
    "⏳ If things stayed the same for 6 more months, how would that feel?",
    "👯 If your best friend was in your shoes, what would you tell them?",
    "🫣 Are there any fears stopping you from seeing things clearly?",
    "🌤️ If you had clarity, how would your heart or body feel?"
]

replies = [
    "Mixed feelings are human. You’re not broken — you’re just figuring things out.",
    "If the thought keeps coming back, it’s worth listening to.",
    "You deserve a relationship where you can be your full, honest self.",
    "Your body often knows what your mind is still unsure about. Trust it.",
    "Love isn’t supposed to feel like a constant up-and-down. You deserve steady care.",
    "Hoping someone changes is hard. You deserve someone who’s already showing up.",
    "The future matters. Ask yourself if this is peace or just habit.",
    "The advice you’d give your friend is often the truth you need too.",
    "Fear can protect, but it can also block the truth. You're allowed to look deeper.",
    "Clarity might come slowly — but the fact you’re seeking it means you’re on the way."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""