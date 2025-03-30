# Shitposter-X

A fully automated shitposting bot for X (formerly Twitter), powered by Gemini AI and GitHub Actions. Generates and posts insightful, humorous tweets based on trending topics.

## Features
- Fetches trending topics on X
- Uses Gemini AI to generate witty and engaging posts
- Posts automatically via the X API
- Runs on GitHub Actions for hands-free operation

## Setup
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/shitposter-x.git
cd shitposter-x
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed. Then run:
```sh
pip install -r requirements.txt
```

### 3. Set Up X API Credentials
You need a developer account on X (Twitter). Once you have it, set up the following environment variables:
```sh
export API_KEY="your_api_key"
export API_SECRET="your_api_secret"
export ACCESS_TOKEN="your_access_token"
export ACCESS_TOKEN_SECRET="your_access_token_secret"
export GEMINI_API_KEY="your_gemini_api_key"
```
Or create a `.env` file:
```
API_KEY=your_api_key
API_SECRET=your_api_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
GEMINI_API_KEY=your_gemini_api_key
```

### 4. Running Locally
```sh
python post_to_x.py
```

## Deployment
### GitHub Actions
This bot is configured to run on a schedule using GitHub Actions.
1. Go to **Settings > Secrets and variables > Actions** on your GitHub repo.
2. Add the environment variables from step 3.
3. Enable GitHub Actions in **Settings > Actions**.

### Docker (Optional)
```sh
docker build -t shitposter-x .
docker run -e API_KEY=your_api_key -e API_SECRET=your_api_secret -e ACCESS_TOKEN=your_access_token -e ACCESS_TOKEN_SECRET=your_access_token_secret -e GEMINI_API_KEY=your_gemini_api_key shitposter-x
```

## Troubleshooting
- **403 Forbidden (Error 453)**: Your app may not have "Write" permissions. Check [X Developer Portal](https://developer.x.com/en/portal/dashboard) and apply for **Elevated Access**.
- **401 Unauthorized**: Invalid API keys. Double-check your credentials.
- **Gemini API Errors**: Ensure your API key is correct and you haven't hit your usage limits.

## License
MIT License. Use at your own risk. Don't get canceled.

---

Built by Arjun Bagga. Enjoy the chaos. 🚀

