# Quick Start Guide

Get the AI Feedback System running in 3 minutes!

## Step 1: Install Dependencies

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# macOS/Linux:
source .venv/bin/activate

# Install packages
pip install -r requirements.txt
```

## Step 2: Set API Key (Optional)

The app works without an API key (uses fallback responses), but for AI features:

```bash
# Windows PowerShell:
$env:OPENROUTER_API_KEY="your_key_here"

# macOS/Linux:
export OPENROUTER_API_KEY="your_key_here"
```

Or create `.env` file:
```env
OPENROUTER_API_KEY=your_key_here
```

## Step 3: Run Server

```bash
python run.py
```

Or:
```bash
uvicorn backend.main:app --reload
```

## Step 4: Open in Browser

- **User Dashboard**: http://localhost:8000
- **Admin Dashboard**: http://localhost:8000/admin

## That's It! 🎉

Try submitting a review on the user dashboard, then check the admin dashboard to see it appear.

## Troubleshooting

**Port already in use?**
```bash
uvicorn backend.main:app --reload --port 8001
```

**Module not found?**
- Make sure you activated the virtual environment
- Run `pip install -r requirements.txt` again

**Database errors?**
- Delete `reviews.db` and restart the server (it will recreate)

## Next: Deploy to Render

See `DEPLOYMENT.md` for full deployment instructions!
