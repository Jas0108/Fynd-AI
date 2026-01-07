# AI Feedback System - Two-Dashboard Web Application

A minimal, production-ready web application with two dashboards: a public-facing user dashboard for submitting feedback and an admin dashboard for viewing and analyzing submissions.

## Features

### User Dashboard 
- Star rating selection (1-5)
- Optional review text input (up to 5000 characters)
- AI-generated personalized response
- Success/error state handling
- Automatic submission storage

### Admin Dashboard 
- Real-time statistics (total reviews, average rating, rating breakdown)
- Auto-refresh capability (every 5 seconds)
- Live-updating list of all submissions
- Filter by rating
- AI-generated summaries and recommended actions for each review
  

## Technical Stack

- **Backend**: FastAPI (Python)
- **Database**: SQLite (via SQLAlchemy)
- **Frontend**: Plain HTML + JavaScript (no frameworks)
- **AI Integration**: OpenRouter (server-side only)
- **Deployment**: Render

## Architecture

### Server-Side LLM Processing
All LLM calls are made server-side only (in FastAPI endpoints) to ensure:
- API key security
- Rate limiting control
- Cost management
- Better error handling

### Data Persistence
- Uses SQLite database (`reviews.db`) created automatically on first run
- Database file persists across server restarts

### Error Handling
The system handles:
- Empty reviews (optional field)
- Long reviews (truncated to 5000 characters)
- LLM API failures (fallback responses)
- Network errors
- Invalid input validation

## Project Structure

```
├── backend/
│   ├── main.py           # FastAPI app and routes
│   ├── database.py       # SQLite database setup
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas for validation
│   └── ai.py             # OpenRouter integration
├── frontend/
│   ├── user.html         # User dashboard HTML
│   ├── admin.html        # Admin dashboard HTML
│   └── static/
│       ├── styles.css    # Shared styles
│       ├── user.js       # User dashboard logic
│       └── admin.js      # Admin dashboard logic
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # This file
```

## Environment Variables

| Variable | Description | 
|----------|-------------|
| `OPENROUTER_API_KEY` | OpenRouter API key | 

