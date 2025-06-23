# flows/notsure.py

def get_question(step):
    questions = [
        "🤔 Do you feel something is wrong but can’t explain what?",
        "🌀 Are you thinking of breaking up but still unsure if it’s the right step?",
        "⚖️ Do you often wonder if it’s worth saving or walking away?",
        "😟 Are you afraid of regretting the decision either way?"
    ]
    return questions[step] if step < len(questions) else None