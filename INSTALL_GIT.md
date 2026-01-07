# How to Install Git on Windows

## Quick Install (Recommended)

### Option 1: Download Git for Windows

1. **Go to:** https://git-scm.com/download/win
2. **Download** the installer (it will auto-detect 64-bit or 32-bit)
3. **Run the installer** (Git-2.x.x-64-bit.exe)
4. **During installation:**
   - Click "Next" through the setup wizard
   - **Important:** On "Select Components" page, make sure "Git Bash Here" and "Git GUI Here" are checked
   - On "Choosing the default editor", choose your preferred editor (or leave as "Nano editor")
   - On "Adjusting your PATH environment", select:
     - **"Git from the command line and also from 3rd-party software"** (Recommended)
   - Click "Next" through remaining steps
   - Click "Install"
5. **Wait for installation** to complete
6. **Click "Finish"**

### Option 2: Install via Winget (Windows Package Manager)

If you have Windows 10/11 with winget:

```powershell
winget install --id Git.Git -e --source winget
```

### Option 3: Install via Chocolatey

If you have Chocolatey installed:

```powershell
choco install git
```

---

## Verify Installation

After installation, **close and reopen** your terminal/command prompt, then run:

```powershell
git --version
```

You should see something like: `git version 2.xx.x`

---

## After Installing Git

Once Git is installed, you can proceed with pushing to GitHub:

```powershell
# Initialize git repository
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit"

# Add GitHub repository (replace with your actual repo URL)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git branch -M main
git push -u origin main
```

---

## Troubleshooting

**If Git still not recognized after installation:**
1. **Close and reopen** your terminal/command prompt
2. **Restart your computer** (sometimes needed for PATH to update)
3. **Check PATH manually:**
   - Search "Environment Variables" in Windows
   - Check if Git is in your PATH
   - Git is usually installed at: `C:\Program Files\Git\cmd\`

**If you get authentication errors when pushing:**
- GitHub now requires a Personal Access Token instead of password
- See: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

---

## Quick Reference

**Download Git:** https://git-scm.com/download/win

**Installation takes:** 2-5 minutes

**After installation:** Restart terminal, then run `git --version` to verify
