import os
import requests
import random

# Load environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
X_BEARER_TOKEN = os.getenv("API_KEY")  # Using API Key as Bearer Token

# X (Twitter) API endpoint
X_POST_URL = "https://api.twitter.com/2/tweets"

# Gemini API Endpoint
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

# Predefined shitposting prompts
PROMPTS = [
    "Generate a conspiracy theory that makes absolutely no sense but sounds convincing.",
    "Write a cursed motivational quote that feels both inspiring and deeply unsettling.",
    "Create a fake 'life hack' that is completely impractical but sounds genius.",
    "Invent a new slang term and explain it as if it's already widely known.",
    "Generate a tweet that sounds like it was written by an AI going through an existential crisis.",
    "Write an overly dramatic tweet about a very minor inconvenience."
]

# Function to generate a shitpost using Gemini
def generate_shitpost():
    prompt = random.choice(PROMPTS)  # Randomly pick a prompt
    
    headers = {
        "Content-Type": "application/json"
    }
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        try:
            return data["candidates"][0]["content"]["parts"][0]["text"].strip()
        except (KeyError, IndexError):
            print("Error: Unexpected Gemini API response format.")
            return None
    else:
        print(f"Gemini API Error: {response.text}")
        return None

# Function to post a tweet
def post_to_x():
    shitpost = generate_shitpost()
    if not shitpost:
        print("Failed to generate a tweet.")
        return
    
    headers = {
        "Authorization": f"Bearer {X_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {"text": shitpost}
    
    response = requests.post(X_POST_URL, headers=headers, json=payload)
    
    if response.status_code == 201:
        print(f"Posted: {shitpost}")
    else:
        print(f"Failed to post: {response.text}")

if __name__ == "__main__":
    post_to_x()
