# Shitposter-X

Shitposter-X is a bot that generates and posts humorous, insightful tweets on X (formerly Twitter) using Google's Gemini API. It selects trending topics and crafts posts in a unique style.

## Features
- Generates tweets based on trending topics using Gemini API
- Automatically posts to X at scheduled intervals
- Runs via a cron job

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
Create a `.env` file in the root directory and add:
```
API_KEY=your_x_api_key
API_SECRET=your_x_api_secret
ACCESS_TOKEN=your_x_access_token
ACCESS_TOKEN_SECRET=your_x_access_token_secret
GEMINI_API_KEY=your_google_gemini_api_key
```

### 4. Schedule the Bot with a Cron Job
Use `crontab -e` to edit your crontab and add the following line to run the bot every hour:
```
0 * * * * /usr/bin/python3 /path/to/shitposter-x/post_to_x.py
```
Replace `/path/to/shitposter-x/` with the actual path to your script.

## Usage
Run the script manually with:
```sh
python post_to_x.py
```

## License
MIT License. Feel free to modify and share!

