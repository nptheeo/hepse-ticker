# Deploy Flask App to Railway

## Files Generated:
1. `requirements.txt` - Python dependencies
2. `Procfile` - Railway deployment configuration
3. `api_server_railway.py` - Updated Flask app with Railway configuration

## Deployment Steps:

### Option 1: Deploy from GitHub (Recommended)
1. Replace your `api_server.py` with `api_server_railway.py` (or copy the changes)
2. Push all files to GitHub repository
3. Go to https://railway.app/ and sign in
4. Click "New Project" → "Deploy from GitHub"
5. Select your repository
6. Railway will auto-detect and deploy
7. Go to Settings → Networking → Generate Domain

### Option 2: Deploy via Railway CLI
1. Install CLI: `npm install -g @railway/cli`
2. Login: `railway login`
3. Initialize: `railway init`
4. Deploy: `railway up`

## Important Notes:
- Make sure `sharesansar_scraper.py` is in the same directory
- Railway uses the PORT environment variable automatically
- Your app will be accessible at: `https://your-app.railway.app`
