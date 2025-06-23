# flows/ghosted.py

def get_question(step):
    questions = [
        "👻 Did they suddenly stop responding without explanation?",
        "🤯 Have you felt confused or anxious about the silence?",
        "😶‍🌫️ Was everything fine before they disappeared?",
        "📱 Do you keep checking your phone or social media for a sign from them?"
    ]
    return questions[step] if step < len(questions) else None