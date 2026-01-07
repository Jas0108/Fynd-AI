# Deployment Guide - FastAPI + SQLite Stack

This guide provides step-by-step instructions for deploying the AI Feedback System to production.

## Quick Deploy to Render (Recommended)

### Prerequisites
- GitHub account
- Render account (free tier works)
- OpenRouter API key

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
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave empty (or set if needed)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or paid for better performance)

4. **Add Environment Variable**
   - In the Environment section, click "Add Environment Variable"
   - Key: `OPENROUTER_API_KEY`
   - Value: Your OpenRouter API key
   - Click "Save Changes"

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete (usually 2-5 minutes)
   - Render will show you the URL once deployed

6. **Access Your Application**
   - User Dashboard: `https://your-service.onrender.com/`
   - Admin Dashboard: `https://your-service.onrender.com/admin`
   - Health Check: `https://your-service.onrender.com/health`

### Render Free Tier Notes
- Services spin down after 15 minutes of inactivity
- First request after spin-down may take 30-60 seconds
- Consider upgrading to paid plan for always-on service

## Alternative: Deploy to Vercel

Vercel is optimized for Next.js, but you can deploy FastAPI using their Python runtime.

### Steps

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Create `vercel.json`** (already included)
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "backend/main.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "backend/main.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

4. **Set Environment Variable**
   - In Vercel dashboard → Settings → Environment Variables
   - Add `OPENROUTER_API_KEY`

**Note**: Vercel's Python runtime has limitations. Render is recommended for FastAPI apps.

## Environment Variables

| Variable | Description | Where to Get |
|----------|-------------|--------------|
| `OPENROUTER_API_KEY` | OpenRouter API key for LLM features | https://openrouter.ai/keys |

## Post-Deployment Checklist

- [ ] Verify User Dashboard loads correctly
- [ ] Verify Admin Dashboard loads correctly
- [ ] Test submitting a review
- [ ] Verify AI responses are generated (or fallback if no key)
- [ ] Check that reviews persist (refresh page)
- [ ] Test admin dashboard auto-refresh
- [ ] Verify statistics display correctly
- [ ] Test filtering by rating
- [ ] Check health endpoint: `/health`

## Troubleshooting

### Issue: AI responses not working
- **Solution**: Verify `OPENROUTER_API_KEY` is set correctly in Render environment variables
- Check Render logs for API errors
- App will use fallback responses if API key is missing

### Issue: Database not persisting
- **Solution**: SQLite file (`reviews.db`) is created in the working directory
- On Render, this persists across deployments
- If data is lost, check Render logs for file system issues

### Issue: Build fails
- Check Python version (requires 3.9+)
- Verify all dependencies are in `requirements.txt`
- Check build logs for specific errors

### Issue: Service won't start
- Verify start command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- Check that `backend/main.py` exists
- Review Render logs for startup errors

### Issue: Static files not loading
- Verify `frontend/static/` directory exists
- Check that FastAPI is mounting static files correctly
- Ensure file paths in HTML are correct (`/static/styles.css`)

## Upgrading to PostgreSQL (Optional)

For production at scale, consider migrating from SQLite to PostgreSQL:

1. **Add PostgreSQL to Render**
   - Create a PostgreSQL database in Render
   - Get connection string

2. **Update `backend/database.py`**
   ```python
   # Change from:
   SQLALCHEMY_DATABASE_URL = "sqlite:///./reviews.db"
   
   # To:
   SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@host/dbname"
   ```

3. **Add PostgreSQL driver**
   - Add `psycopg2-binary` to `requirements.txt`

4. **Redeploy**

## Custom Domain (Optional)

### Render
1. Go to your service → Settings → Custom Domains
2. Add your custom domain
3. Configure DNS records as instructed by Render

## Monitoring

Consider adding:
- Error tracking (Sentry)
- Uptime monitoring (UptimeRobot, Pingdom)
- Log aggregation (if using paid Render plan)

## Database Backups

For SQLite on Render:
- The database file persists in the service's file system
- For backups, periodically download `reviews.db` via SSH or add a backup endpoint
- Consider migrating to PostgreSQL for better backup options
