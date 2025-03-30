import os
import requests
import random
import tweepy


# X API credentials from GitHub Secrets
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

# Authenticate with X (OAuth 1.0a)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Generate post with Gemini API

# Topics for shitposting
TOPICS = [
    "physics",
    "AI",
    "quantum mechanics",
    "biotechnology",
    "crypto",
    "cybersecurity",
    "hacking",
    "LLM",
    "finance",
    "maths",
    "motorcycles",
    "US stocks",
    "Indian stocks",
    "beer",
    "wine",
    "tech"
]

# Function to generate a shitpost using Gemini
def generate_shitpost():
    topic = random.choice(TOPICS)  # Randomly select a topic
    
    prompt = (
        f"Analyse the posts on X related to {topic}, select the funniest trend with the most engagement, "
        f"and write an X post in the style of https://x.com/ArjunBagga_xyz. "
        f"Make it insightful and humorous. Your response should be just the post, nothing else (under 200 characters and no hashtags)."
    )
    
    headers = {"Content-Type": "application/json"}
    
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
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

# Post to X
post = generate_post()
api.update_status(post)
print(f"Posted to X: {post}")
