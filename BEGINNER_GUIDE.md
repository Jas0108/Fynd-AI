# Complete Beginner's Guide - Step by Step

This guide will walk you through everything from scratch. Follow each step carefully!

## Prerequisites Check

Before starting, make sure you have:
- ✅ Python installed (version 3.9 or higher)
- ✅ A code editor (VS Code recommended)
- ✅ An OpenRouter API key (get one at https://openrouter.ai/keys)

### Check if Python is installed:

**Windows PowerShell:**
```powershell
python --version
```

**Windows CMD:**
```cmd
python --version
```

If you see something like `Python 3.9.x` or higher, you're good! If not, download Python from https://www.python.org/downloads/

---

## Step 1: Open Your Project Folder

1. Open File Explorer
2. Navigate to: `C:\Users\jashi\OneDrive\Desktop\Fynd`
3. Right-click in the folder and select "Open in Terminal" or "Open PowerShell here"

---

## Step 2: Create Virtual Environment

A virtual environment keeps your project's packages separate from other Python projects.

**In PowerShell (run these commands one by one):**

```powershell
# Create virtual environment
python -m venv .venv
```

Wait for it to finish (takes 10-30 seconds).

---

## Step 3: Activate Virtual Environment

**In PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**If you get an error about execution policy, run this first:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating again:
```powershell
.venv\Scripts\Activate.ps1
```

**You should see `(.venv)` at the start of your command line** - this means it's activated!

**Alternative (if PowerShell doesn't work):**
Open Command Prompt (CMD) instead and run:
```cmd
.venv\Scripts\activate.bat
```

---

## Step 4: Install Required Packages

With the virtual environment activated, install all dependencies:

```powershell
pip install -r requirements.txt
```

This will take 1-2 minutes. You'll see lots of text scrolling - that's normal!

**Wait until you see:** `Successfully installed ...` at the end.

---

## Step 5: Set Up Your API Key

### Option A: Using .env file (Recommended - Easiest)

1. In your project folder (`Fynd`), look for `.env.example` file
2. **Copy** `.env.example` and **rename** it to `.env` (remove `.example`)
   - Right-click `.env.example` → Copy
   - Right-click → Paste
   - Rename the copy to `.env`
3. **Open** `.env` file in a text editor (Notepad, VS Code, etc.)
4. **Replace** `your_openrouter_api_key_here` with your actual API key:
   ```
   OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
   ```
5. **Save** the file (Ctrl+S)

### Option B: Set Environment Variable (Alternative)

**In PowerShell (with virtual environment activated):**
```powershell
$env:OPENROUTER_API_KEY="sk-or-v1-your-actual-key-here"
```

**Note:** This only works for the current terminal session. You'll need to set it again if you close and reopen.

---

## Step 6: Start the Server

With your virtual environment still activated, run:

```powershell
python run.py
```

**OR:**

```powershell
uvicorn backend.main:app --reload
```

**You should see output like:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**🎉 Your server is now running!**

**Keep this terminal window open** - don't close it! The server needs to keep running.

---

## Step 7: Open the Application in Browser

1. Open your web browser (Chrome, Edge, Firefox, etc.)
2. Go to one of these URLs:

   **User Dashboard (to submit feedback):**
   ```
   http://localhost:8000
   ```

   **Admin Dashboard (to view all submissions):**
   ```
   http://localhost:8000/admin
   ```

3. You should see the dashboard page load!

---

## Step 8: Test the Application

1. **On User Dashboard** (`http://localhost:8000`):
   - Click on stars to select a rating (1-5)
   - Optionally type a review
   - Click "Submit Review"
   - You should see an AI-generated response!

2. **On Admin Dashboard** (`http://localhost:8000/admin`):
   - You should see your submitted review appear
   - Check the statistics
   - Try filtering by rating

---

## Common Issues & Solutions

### Issue: "python is not recognized"
**Solution:** Python is not installed or not in PATH. Install Python and make sure to check "Add Python to PATH" during installation.

### Issue: "ModuleNotFoundError" or "No module named..."
**Solution:** 
1. Make sure virtual environment is activated (you see `(.venv)` in terminal)
2. Run: `pip install -r requirements.txt` again

### Issue: "Port 8000 already in use"
**Solution:** Another program is using port 8000. Either:
- Close the other program, OR
- Use a different port: `uvicorn backend.main:app --reload --port 8001`
- Then access at `http://localhost:8001`

### Issue: "Cannot activate virtual environment"
**Solution:** 
- Try Command Prompt (CMD) instead of PowerShell
- Run: `.venv\Scripts\activate.bat`

### Issue: API key not working
**Solution:**
- Make sure `.env` file is in the project root folder
- Make sure there are no extra spaces around the `=` sign
- Restart the server after adding/changing the key

### Issue: Database errors
**Solution:**
- Delete `reviews.db` file if it exists
- Restart the server (it will create a new database)

---

## Stopping the Server

When you're done testing:

1. Go back to your terminal window
2. Press `Ctrl+C` to stop the server
3. Type `deactivate` to exit the virtual environment (optional)

---

## Next Steps

- **Deploy to Render:** See `DEPLOYMENT.md` for production deployment
- **Customize:** Edit files in `frontend/` to change the UI
- **Add Features:** Modify `backend/main.py` to add new endpoints

---

## Quick Reference Commands

```powershell
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt

# Run server
python run.py

# Or alternatively:
uvicorn backend.main:app --reload
```

---

## Need Help?

- Check the logs in your terminal for error messages
- Make sure all steps were followed correctly
- Verify your API key is correct in `.env` file

Good luck! 🚀
