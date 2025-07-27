questions = [
    "👻 Did they disappear all of a sudden, or did things fade slowly?",
    "🧠 Are you stuck wondering why they went silent?",
    "💬 Did you try to reach out after they ghosted you? What happened?",
    "📉 Has this made you feel like you're not good enough?",
    "🔎 Are you blaming yourself for something you don’t understand?",
    "🌪️ Does the lack of answers make it harder to let go?",
    "🛑 If you could say something to them now, what would it be?",
    "📱 Does seeing them online or on social media bother you?",
    "🧭 What would closure look like, even if they never give it?",
    "🌤️ What’s one small truth or thought that gives you a little peace?"
]

replies = [
    "Ghosting feels like someone left the room without saying goodbye — it’s painful and unfair.",
    "It’s okay to want answers, even if none come. You’re not wrong for wondering.",
    "Reaching out was brave. If they didn’t respond, that’s about them — not you.",
    "This doesn’t define your worth. Someone’s silence can’t decide your value.",
    "You didn’t cause their silence. Sometimes people run from their own discomfort.",
    "Letting go without answers is hard, but you still deserve peace.",
    "Even if they’ll never hear it, saying it out loud can help you let go.",
    "Seeing them online can reopen wounds. It’s okay to mute or take space.",
    "Closure isn’t something they give. It’s something you create within yourself.",
    "You’re moving forward, even in silence. That takes quiet strength."
]
def get_question(step):
    return questions[step] if step < len(questions) else get_feedback_prompt()


def get_feedback_prompt():
    return """🐰 Before we say goodbye for now, how did this conversation feel for you?

A. I feel lighter 🙏  
B. I still feel confused 🌀  
C. I want to talk to a human 💬

Just reply with A, B, or C."""