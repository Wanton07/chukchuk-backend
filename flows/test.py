def get_question(step):
    questions = [
        "🧪 This is just a test. What emotion are you simulating?",
        "🔁 Do you feel stuck in a loop around this issue?",
        "💬 What's one thought you're testing journaling for?"
    ]
    if step < len(questions):
        return questions[step]
    return "JOURNAL"