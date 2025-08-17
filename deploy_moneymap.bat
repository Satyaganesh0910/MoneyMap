@echo off
echo ============================================================
echo 💰 MoneyMap - Quick Deployment Script 💰
echo ============================================================
echo.

echo 🔧 Step 1: Checking Git status...
git status
if %errorlevel% neq 0 (
    echo ❌ Git repository not found. Please run this script from the MoneyMap directory.
    pause
    exit /b 1
)

echo.
echo ✅ Git repository is ready!
echo.

echo 📋 Step 2: GitHub Repository Setup
echo ----------------------------------------
echo Please follow these steps:
echo 1. Go to https://github.com/new
echo 2. Repository name: MoneyMap
echo 3. Description: A beautiful family finance tracker with modern design
echo 4. Visibility: Public
echo 5. Don't initialize with README
echo 6. Click "Create repository"
echo.

set /p username="Enter your GitHub username: "

echo.
echo 🚀 Step 3: Connecting to GitHub...
git remote add origin https://github.com/%username%/MoneyMap.git
git branch -M main
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ Successfully pushed to GitHub!
    echo.
    echo 🌐 Step 4: Deploy on Streamlit Cloud
    echo ----------------------------------------
    echo 1. Go to https://share.streamlit.io
    echo 2. Sign in with GitHub
    echo 3. Click "New app"
    echo 4. Repository: %username%/MoneyMap
    echo 5. Branch: main
    echo 6. Main file path: app.py
    echo 7. App URL: moneymap-app
    echo 8. Click "Deploy"
    echo.
    echo 🎉 Your MoneyMap will be live at: https://moneymap-app.streamlit.app
    echo.
    echo 💡 Share this link with everyone to use your beautiful MoneyMap app!
) else (
    echo ❌ Error pushing to GitHub. Please check your repository URL.
)

echo.
pause
