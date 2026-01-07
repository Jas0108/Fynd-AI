# ✅ Fixed: How to Run Without PowerShell Activation Issues

## The Problem
PowerShell execution policy was blocking the activation script.

## The Solution
You can run everything **without activating the virtual environment** by using the full path to Python!

---

## ✅ Easy Method (No Activation Needed)

### Step 1: Install Dependencies (if not done)
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 2: Run the Server
```powershell
.venv\Scripts\python.exe run.py
```

**That's it!** The server will start running.

---

## Alternative: Use Command Prompt Instead

If PowerShell keeps giving you issues:

1. **Open Command Prompt (CMD)** instead of PowerShell
2. Navigate to your project folder:
   ```cmd
   cd C:\Users\jashi\OneDrive\Desktop\Fynd
   ```
3. **Activate virtual environment:**
   ```cmd
   .venv\Scripts\activate.bat
   ```
4. **Install dependencies:**
   ```cmd
   pip install -r requirements.txt
   ```
5. **Run server:**
   ```cmd
   python run.py
   ```

---

## Quick Commands Reference

**Without activation (easiest):**
```powershell
# Install packages
.venv\Scripts\python.exe -m pip install -r requirements.txt

# Run server
.venv\Scripts\python.exe run.py
```

**With activation (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
pip install -r requirements.txt
python run.py
```

---

## Access Your Application

Once the server is running:
- **User Dashboard:** http://localhost:8000
- **Admin Dashboard:** http://localhost:8000/admin

---

## Stop the Server

Press `Ctrl+C` in the terminal where the server is running.
