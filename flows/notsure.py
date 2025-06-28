questions = [
    "🤔 What emotions are clashing the most — guilt, fear, hope, or confusion?",
    "🔄 Are your thoughts about breaking up constant or only in certain moments?",
    "🎭 Are you showing up as your true self in this relationship?",
    "🧘 How does your body react when you imagine staying vs. leaving?",
    "🧩 What do you get from this relationship — comfort, chaos, duty, joy?",
    "🪞 Are you in love with the person or the potential of who they could become?",
    "⚖️ If nothing changed in 6 months, would you feel more stuck or more settled?",
    "📣 If your best friend described this exact relationship, what would you tell them?",
    "🔍 What fears are keeping you from exploring the truth fully?",
    "🌱 What would clarity feel like in your body — light, grounded, certain?"
]

replies = [
    "Confusion is part of clarity. You’re not wrong for feeling both love and doubt.",
    "Patterns matter. If these thoughts keep returning, they’re telling you something.",
    "Hiding parts of yourself can drain you slowly. You deserve to be whole.",
    "The body knows. Notice — do you tense up or relax when you imagine freedom?",
    "It’s okay to name both the good and the hard. You’re seeing the full picture.",
    "Potential is not a promise. You deserve someone who already shows up.",
    "Time is a teacher. Would staying be healing or just delaying?",
    "You already give great advice — now offer it to yourself.",
    "Fear doesn’t mean wrong — but it can be a signal to slow down and ask more.",
    "Clarity is not a sudden light — it’s a steady unfolding. You’re already on the way."
]
def get_question(step):
    return questions[step] if step < len(questions) else None