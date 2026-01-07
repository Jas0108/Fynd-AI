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
- 
## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Fynd
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .venv\Scripts\Activate.ps1
   # Windows CMD:
   .venv\Scripts\activate.bat
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```

## Deployment to Render 

### Steps

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Create a new Web Service on Render**
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Build Settings**
   - **Name**: `ai-feedback-system` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or paid)

4. **Add Environment Variable**
   - In the Environment section, add:
     - Key: `OPENROUTER_API_KEY`
     - Value: Your OpenRouter API key

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete

6. **Access Your Application**
   - User Dashboard: `https://your-service.onrender.com/`
   - Admin Dashboard: `https://your-service.onrender.com/admin`

## API Endpoints

### POST `/api/reviews`
Submit a new review.

**Request Body:**
```json
{
  "rating": 5,
  "review": "Great experience!"
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "id": 1,
    "rating": 5,
    "review": "Great experience!",
    "ai_response": "Thank you for your feedback...",
    "created_at": "2024-01-01T00:00:00"
  }
}
```

### GET `/api/reviews`
Get all reviews (most recent first).

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "rating": 5,
      "review": "Great experience!",
      "ai_response": "...",
      "ai_summary": "...",
      "ai_recommended_actions": "...",
      "created_at": "2024-01-01T00:00:00"
    }
  ]
}
```

### GET `/api/stats`
Get review statistics.

**Response:**
```json
{
  "success": true,
  "data": {
    "total": 10,
    "by_rating": [
      { "rating": 1, "count": 0 },
      { "rating": 2, "count": 1 },
      { "rating": 3, "count": 2 },
      { "rating": 4, "count": 3 },
      { "rating": 5, "count": 4 }
    ],
    "average_rating": 4.1
  }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

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
- Easy to migrate to PostgreSQL/MySQL if needed (just change connection string in `backend/database.py`)

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

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Yes (for AI features) |

**Note**: The app will work without the API key, but will use fallback responses instead of AI-generated content.

## Production Considerations

1. **Database**: SQLite works for small-medium scale. For larger deployments, migrate to PostgreSQL
2. **Rate Limiting**: Add rate limiting middleware to API endpoints
3. **Authentication**: Add authentication for admin dashboard
4. **CORS**: Currently allows all origins. Restrict in production
5. **Monitoring**: Add error tracking (e.g., Sentry)
6. **Backups**: Set up regular backups of `reviews.db`

## License

MIT

## Support

For issues or questions, please open an issue in the repository.
