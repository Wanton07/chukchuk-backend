from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/incoming", methods=["POST"])
def incoming_message():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "lost" in incoming_msg:
        msg.body("Hey, you're not alone. It's okay to feel this way. I'm here for you. 💛")
    elif "breakup" in incoming_msg:
        msg.body("Breakups hurt, but it’s the start of healing. Let’s talk it out. 🌱")
    elif "hi" in incoming_msg or "hello" in incoming_msg:
        msg.body("Hi, I’m ChukChuk 🤖 Your breakup buddy. Tell me how you're feeling today.")
    else:
        msg.body("I'm here to listen. Say anything you're feeling right now. 💬")

    return str(resp)

@app.route("/", methods=["GET"])
def home():
    return "ChukChuk backend is live!"

if __name__ == "__main__":
    app.run()
