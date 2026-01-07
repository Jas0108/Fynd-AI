# 🚀 How to Run the Project - Step by Step

## ✅ Prerequisites Check
- ✅ Python 3.12.4 installed
- ✅ Virtual environment (.venv) exists
- ✅ .env file with API key created

---

## Step 1: Activate Virtual Environment

**In PowerShell, run:**
```powershell
.venv\Scripts\Activate.ps1
```

**You should see `(.venv)` appear at the start of your command line.**

**If you get an error about execution policy, run this first:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

**Alternative (if PowerShell doesn't work):**
Open Command Prompt (CMD) and run:
```cmd
.venv\Scripts\activate.bat
```

---

## Step 2: Install Dependencies

**With virtual environment activated, run:**
```powershell
pip install -r requirements.txt
```

**Wait for it to finish** (takes 1-2 minutes). You'll see packages being installed.

**You should see:** `Successfully installed ...` at the end.

---

## Step 3: Start the Server

**With virtual environment still activated, run:**
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

**⚠️ IMPORTANT: Keep this terminal window open!** Don't close it - the server needs to keep running.

---

## Step 4: Open in Browser

1. **Open your web browser** (Chrome, Edge, Firefox, etc.)

2. **Go to one of these URLs:**

   **User Dashboard** (to submit feedback):
   ```
   http://localhost:8000
   ```
   or
   ```
   http://127.0.0.1:8000
   ```

   **Admin Dashboard** (to view all submissions):
   ```
   http://localhost:8000/admin
   ```

3. **You should see the dashboard page load!**

---

## Step 5: Test the Application

### On User Dashboard:
1. Click on stars to select a rating (1-5 stars)
2. Optionally type a review in the text box
3. Click "Submit Review" button
4. You should see an AI-generated response appear!

### On Admin Dashboard:
1. You should see your submitted review appear automatically
2. Check the statistics (total reviews, average rating)
3. Try filtering by rating using the filter buttons
4. The page auto-refreshes every 5 seconds to show new submissions

---

## 🛑 Stopping the Server

When you're done:

1. **Go back to your terminal window**
2. **Press `Ctrl+C`** to stop the server
3. **Type `deactivate`** to exit the virtual environment (optional)

---

## ❌ Troubleshooting

### Problem: "python is not recognized"
**Solution:** Python is not in your PATH. Reinstall Python and check "Add Python to PATH" during installation.

### Problem: "ModuleNotFoundError" or "No module named..."
**Solution:** 
1. Make sure virtual environment is activated (you see `(.venv)` in terminal)
2. Run: `pip install -r requirements.txt` again

### Problem: "Port 8000 already in use"
**Solution:** Another program is using port 8000. Either:
- Close the other program, OR
- Use a different port: `uvicorn backend.main:app --reload --port 8001`
- Then access at `http://localhost:8001`

### Problem: "Cannot activate virtual environment"
**Solution:** 
- Try Command Prompt (CMD) instead of PowerShell
- Run: `.venv\Scripts\activate.bat`

### Problem: API key not working / No AI responses
**Solution:**
- Make sure `.env` file is in the project root folder (`Fynd` folder)
- Make sure there are no extra spaces around the `=` sign
- Restart the server after adding/changing the key
- Check that the API key starts with `sk-or-v1-`

### Problem: Database errors
**Solution:**
- Delete `reviews.db` file if it exists
- Restart the server (it will create a new database)

---

## 📋 Quick Command Reference

```powershell
# 1. Activate virtual environment
.venv\Scripts\Activate.ps1

# 2. Install packages (only needed first time or after changes)
pip install -r requirements.txt

# 3. Start server
python run.py

# 4. Stop server (in the terminal running the server)
Ctrl+C
```

---

## 🎯 What You Should See

**When server starts successfully:**
- Terminal shows: `Uvicorn running on http://127.0.0.1:8000`
- Browser shows: Beautiful dashboard with gradient background

**When you submit a review:**
- Success message appears
- AI-generated response is shown
- Review appears in admin dashboard

---

Good luck! If you encounter any issues, check the error messages in your terminal and let me know! 🚀
