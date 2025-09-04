import os
import requests
import random
import tweepy
from atproto import Client as BlueskyClient
from neynar import NeynarClient


# X API credentials from GitHub Secrets
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# Bluesky credentials
BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME")
BLUESKY_PASSWORD = os.getenv("BLUESKY_PASSWORD")

# Farcaster credentials
FARCASTER_API_KEY = os.getenv("FARCASTER_API_KEY")
FARCASTER_SIGNER_UUID = os.getenv("FARCASTER_SIGNER_UUID")


# Google Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

# Authenticate with X
x_client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)


# Generate post with Gemini API

# Topics for shitposting
TOPICS = {
    "MIND": [
        "physics",
        "quantum mechanics",
        "mathematics",
        "meditation"
    ],
    "SOFT_ENG": [
        "AI",
        "tech",
        "software development",
        "hacking",
        "cyber security",
        "web3"
    ],
    "MONEY": [
        "crypto",
        "HFT",
        "algo trading",
        "quant finance"
    ],
    "HARD_ENG": [
        "nanotechnology",
        "weapon technology",
        "quantum computing",
        "robotics"
    ],
    "SAMAAJ": [
        "movies",
        "dating",
        "alcohol",
        "pop culture",
        "fighting",
        "day to day activity",
        "memes"
    ]
}

TOPIC_FANBASE = {
    "TV": [
        "Dragon Ball",
        "Pokemon",
        "Naruto",
        "One Piece",
        "How I met your mother",
        "friends",
        "Star Wars",
        "Harry Potter",
        "Marvel Cinematic Universe",
        "Sherlock Holmes",
        "Disney",
        "anime",
        "DC universe",
        "Batman",
        "Studio Ghibli",
        "Lord of the Rings"
    ],
    "SPORTS": [
        "Surfing",
        "Skating",
        "Swimming",
        "Muay Thai",
        "MMA",
        "F1",
        "Football"
    ],
    "MUSIC": [
        "Eminem",
        "ACDC",
        "Billy Joel",
        "Linkin Park",
        "Snoop Dogg",
        "Enrique Iglesias",
        "Pitbull",
        "BTS",
        "Grateful Dead",
        "BLACKPINK"
    ],
    "GAMES": [
        "Minecraft",
        "RGG studio's Yakuza series",
        "Genshin Impact",
        "Pokemon",
        "Tomb Raider",
        "Sonic the hedgehog",
        "Devil May Cry",
        "Budokai Tenkaichi",
        "Call of Duty",
        "Cyberpunk 2077",
        "Grand theft Auto series",
        "Witcher",
        "Runescape",
        "Tekken"
    ]
}

# Function to generate a shitpost using Gemini
def generate_shitpost():
    topic = random.choice(list(TOPICS.keys())) 
    subtopic = random.choice(TOPICS[topic]) 
    topic1 = random.choice(list(TOPIC_FANBASE.keys())) 
    subtopic1 = random.choice(TOPIC_FANBASE[topic1]) 
    
    prompt = f""" You are a chill, playful guy, with mannerisms and speech style of Tom Ellis in lucifer active in {TOPICS} and {TOPIC_FANBASE}. Write an unhinged banger tweet about {subtopic} and/or {subtopic1} that portrays a silly thought that comes from your day to day life.

Your tweet must be:
* **Genuinely funny**, catching people by surprise.
* **concise**.
* trendy
* human humor, not AI humor
* confident
* double check the abstraction logic
* ABSOLUTELY NO "x is just like y", "x is basically y", etc. style of writing

Guidelines:
* Emojis are encouraged 🎉.
* Absolutely no hashtags.
* Keep it light: no existential dread.
* double check the abstraction logic
* ragebaiting encouraged
* unserious tonality
* no em dashes
* (And for reasons we don't question, no mentions of Roombas, and no mention of schrodinger's cat.)

Output *only* the tweet text. No explanations, no quotes, just the raw tweet."""

    
    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": GEMINI_API_KEY  # Explicitly pass API key in headers
    }
    
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

# Function to post to X
def post_to_x(text):
    if not text:
        print("No text to post to X.")
        return
    try:
        x_client.create_tweet(text=text)
        print(f"Posted to X: {text}")
    except Exception as e:
        print(f"Failed to post to X: {e}")

# Function to post to Bluesky
def post_to_bluesky(text):
    if not text:
        print("No text to post to Bluesky.")
        return
    if not BLUESKY_USERNAME or not BLUESKY_PASSWORD:
        print("Bluesky credentials not found. Skipping post.")
        return
    try:
        bluesky_client = BlueskyClient()
        bluesky_client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)
        bluesky_client.post(text=text)
        print(f"Posted to Bluesky: {text}")
    except Exception as e:
        print(f"Failed to post to Bluesky: {e}")

# Function to post to Farcaster
def post_to_farcaster(text):
    if not text:
        print("No text to post to Farcaster.")
        return
    if not FARCASTER_API_KEY or not FARCASTER_SIGNER_UUID:
        print("Farcaster credentials not found. Skipping post.")
        return
    try:
        farcaster_client = NeynarClient(api_key=FARCASTER_API_KEY)
        farcaster_client.publish_cast(signer_uuid=FARCASTER_SIGNER_UUID, text=text)
        print(f"Posted to Farcaster: {text}")
    except Exception as e:
        print(f"Failed to post to Farcaster: {e}")

# Main execution
if __name__ == "__main__":
    post_content = generate_shitpost()
    if post_content:
        post_to_x(post_content)
        post_to_bluesky(post_content)
        post_to_farcaster(post_content)
