import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_emotion(message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": (
                    "You are an emotion classifier. Return only one emotion label "
                    "that best represents the user's message. Use this set: "
                    "Sadness, Anger, Shame, Fear, Love, Guilt, Relief, Hope, "
                    "Confusion, Anxiety, Loneliness, Frustration, Grief, Regret, "
                    "Empowerment, Vulnerability, Numbness. "
                    "Reply only with the label — no explanations. "
                    "If unsure, pick the most dominant emotion, not 'Confusion'. "
                    "The user may reply in English, Hindi or Hinglish. If in Hindi or Hinglish, translate first."
                )},
                {"role": "user", "content": message}
            ]
        )
        emotion = response.choices[0].message.content.strip().capitalize()
        return emotion
    except Exception as e:
        return "Unknown"