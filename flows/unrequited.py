# flows/unrequited.py

def get_question(step):
    questions = [
        "Did the other person know how you felt?",
        "Were you two ever in a romantic relationship?",
        "How long have you had these feelings?",
        "Did you express your emotions directly to them?",
        "What kind of support do you wish you had received?",
    ]
    return questions[step] if step < len(questions) else None

def get_reflection():
    return (
        "Unrequited love can feel like grieving something that never fully began 💔.\n"
        "Your feelings were valid, and your pain is real.\n"
        "This is not about being rejected—it’s about learning to value your emotions even if they weren’t returned.\n"
        "Be kind to yourself. Let’s keep working through this together, one breath at a time 🐰."
    )