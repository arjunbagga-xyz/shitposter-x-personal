# Shitposter-Socials

Shitposter-Socials is a bot that generates and posts humorous, insightful content on X (formerly Twitter), Bluesky, and Farcaster using Google's Gemini API. It selects trending topics and crafts posts in a unique style.

## Features
- Generates posts based on trending topics using Gemini API
- Automatically posts to X, Bluesky, and Farcaster at scheduled intervals
- Runs via a cron job or GitHub Actions

## Setup
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/shitposter-x.git
cd shitposter-x
```

### 2. Install Dependencies
Ensure you have Python 3.13 installed, then run:
```sh
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory and add the following. If you are running this via GitHub Actions, you should set these as repository secrets.
```
# X Credentials
API_KEY=your_x_api_key
API_SECRET=your_x_api_secret
ACCESS_TOKEN=your_x_access_token
ACCESS_TOKEN_SECRET=your_x_access_token_secret

# Gemini API Key
GEMINI_API_KEY=your_google_gemini_api_key

# Bluesky Credentials
BLUESKY_USERNAME=your_bluesky_username
BLUESKY_PASSWORD=your_bluesky_password

# Farcaster Credentials
FARCASTER_API_KEY=your_neynar_api_key
FARCASTER_SIGNER_UUID=your_farcaster_signer_uuid
```

### 4. Schedule the Bot with a Cron Job
Use `crontab -e` to edit your crontab and add the following line to run the bot every hour:
```
0 * * * * /usr/bin/python3 /path/to/shitposter-socials/post_to_socials.py
```
Replace `/path/to/shitposter-socials/` with the actual path to your script.

Alternatively, you can rely on the GitHub Actions workflow in this repository, which will run at the schedule defined in `.github/workflows/post.yml`.

## Usage
Run the script manually with:
```sh
python post_to_socials.py
```

## License
MIT License. Feel free to modify and share!
