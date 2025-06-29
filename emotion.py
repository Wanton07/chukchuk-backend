import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def detect_emotion(message):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an emotion classifier. Return only the emotion label (like: Sadness, Anger, Shame, Fear, Love, Guilt, Relief, Hope) that best represents the user's message."},
            {"role": "user", "content": message}
        ]
    )
    emotion = response.choices[0].message.content.strip()
    return emotion