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
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Authenticate with X (OAuth 1.0a)
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Check which API version is being used
print(api.auth.access_token)  # Should not be None

client = tweepy.Client(
    bearer_token=os.getenv("BEARER_TOKEN"),
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
        "mathematics"
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
# Function to generate a shitpost using Gemini
def generate_shitpost():
    topic = random.choice(list(TOPICS.keys())) 
    subtopic = random.choice(TOPICS[topic]) 
    topic1 = random.choice(list(TOPIC_FANBASE.keys())) 
    subtopic1 = random.choice(TOPIC_FANBASE[topic1]) 
    
    prompt = f"""write an unhinged banger one-two liner tweet about {subtopic} mixed with hummor or anecdote from {subtopic1}. a hot take with a call to action.

Your tweet must be:
* **Genuinely funny**, catching people by surprise.
* **Subtly philosophical**, offering a tiny, blink-and-you'll-miss-it insight.
* An **"insider's joke" that outsiders may or may not appreciate** and find amusing.
* A blend of **passion and sarcasm**.
* **offensive**.
* **concise**.

Guidelines:
* Emojis are encouraged 🎉.
* Absolutely no hashtags.
* Keep it light: no existential dread.
* type like a comedian.
* unserious tonality
* no em dashes
* Funny one liners welcome.
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
post = generate_shitpost()
client.create_tweet(text=post)
print(f"Posted to X: {post}")
