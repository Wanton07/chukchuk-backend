# flows/divorce.py

questions = [
    "How many years were you married before the divorce?",
    "Was the divorce mutual, or did one of you push for it more?",
    "Are children involved in the situation?",
    "What has been the hardest part post-divorce?",
    "Have you had support from friends or family during this time?",
]

def get_question(step):
    if step < len(questions):
        return questions[step]
    return None

def get_reflection():
    return (
        "Divorce can feel like the end of a chapter you never imagined closing 🥀.\n"
        "But it’s also the beginning of reclaiming your peace.\n"
        "Take your time, give yourself grace, and know you’re not alone 🐰."
    )