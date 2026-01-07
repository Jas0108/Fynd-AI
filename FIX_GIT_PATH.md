# Fix Git Not Recognized Error

Git is installed but not in your PATH. Here are solutions:

## Solution 1: Restart Your Computer (Recommended)

The easiest fix:
1. **Save all your work**
2. **Restart your computer**
3. **Open a new terminal** after restart
4. **Try:** `git --version`

This will refresh all environment variables.

---

## Solution 2: Refresh PATH in Current Session

**In PowerShell, run:**
```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
git --version
```

**In Command Prompt (CMD), run:**
```cmd
refreshenv
```
(If you have Chocolatey installed)

Or manually:
```cmd
set PATH=%PATH%;C:\Program Files\Git\cmd
git --version
```

---

## Solution 3: Use Git Bash Instead

Git Bash should work immediately:

1. **Search for "Git Bash"** in Windows Start menu
2. **Open Git Bash**
3. **Navigate to your project:**
   ```bash
   cd /c/Users/jashi/OneDrive/Desktop/Fynd
   ```
4. **Git will work here!**

---

## Solution 4: Use Full Path (Temporary Workaround)

You can use Git with the full path:

**In PowerShell:**
```powershell
& "C:\Program Files\Git\cmd\git.exe" --version
& "C:\Program Files\Git\cmd\git.exe" init
& "C:\Program Files\Git\cmd\git.exe" add .
```

**In CMD:**
```cmd
"C:\Program Files\Git\cmd\git.exe" --version
"C:\Program Files\Git\cmd\git.exe" init
"C:\Program Files\Git\cmd\git.exe" add .
```

---

## Solution 5: Manually Add to PATH

1. **Search "Environment Variables"** in Windows
2. **Click "Edit the system environment variables"**
3. **Click "Environment Variables" button**
4. **Under "System variables", find "Path"**
5. **Click "Edit"**
6. **Click "New"**
7. **Add:** `C:\Program Files\Git\cmd`
8. **Click "OK" on all windows**
9. **Close and reopen terminal**

---

## Quick Test

After trying any solution, test with:
```powershell
git --version
```

You should see: `git version 2.52.0.windows.1`

---

## Recommended: Use Git Bash

For now, the easiest solution is to **use Git Bash** - it works immediately and you don't need to fix PATH!
