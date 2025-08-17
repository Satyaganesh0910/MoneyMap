#!/usr/bin/env python3
"""
MoneyMap GitHub Setup Helper Script
This script helps you set up your MoneyMap project on GitHub and deploy it publicly.
"""

import os
import subprocess
import sys

def print_banner():
    print("=" * 60)
    print("💰 MoneyMap - GitHub Setup & Deployment Helper 💰")
    print("=" * 60)
    print()

def check_git_status():
    """Check if git repository is properly initialized"""
    try:
        result = subprocess.run(['git', 'status'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Git repository is initialized")
            return True
        else:
            print("❌ Git repository not found")
            return False
    except FileNotFoundError:
        print("❌ Git is not installed. Please install Git first.")
        return False

def get_github_username():
    """Get GitHub username from user"""
    print("🔧 Step 1: GitHub Repository Setup")
    print("-" * 40)
    username = input("Enter your GitHub username: ").strip()
    return username

def create_github_commands(username):
    """Generate the commands needed to set up GitHub"""
    commands = f"""
# Step 2: Create GitHub Repository
# Go to https://github.com/new
# Repository name: MoneyMap
# Description: A beautiful family finance tracker with modern design
# Visibility: Public
# Don't initialize with README (we'll push our existing code)

# Step 3: Connect to GitHub (run these commands):
git remote add origin https://github.com/{username}/MoneyMap.git
git branch -M main
git push -u origin main

# Step 4: Deploy on Streamlit Cloud
# Go to https://share.streamlit.io
# Sign in with GitHub
# Click "New app"
# Repository: {username}/MoneyMap
# Branch: main
# Main file path: app.py
# App URL: moneymap-app (or choose your preferred name)
# Click "Deploy"

# Your app will be live at: https://moneymap-app.streamlit.app
"""
    return commands

def main():
    print_banner()
    
    # Check git status
    if not check_git_status():
        print("\nPlease run these commands first:")
        print("git init")
        print("git add .")
        print("git commit -m 'Initial MoneyMap release'")
        return
    
    # Get GitHub username
    username = get_github_username()
    
    # Generate commands
    commands = create_github_commands(username)
    
    print("\n📋 Complete Setup Instructions:")
    print("=" * 50)
    print(commands)
    
    print("\n🚀 Quick Start Commands:")
    print("-" * 30)
    print(f"git remote add origin https://github.com/{username}/MoneyMap.git")
    print("git branch -M main")
    print("git push -u origin main")
    
    print("\n💡 Tips:")
    print("- Make sure you've created the GitHub repository first")
    print("- The repository should be public for free Streamlit deployment")
    print("- After pushing to GitHub, deploy on Streamlit Cloud for public access")
    
    print("\n🎉 Once deployed, your MoneyMap will be available to everyone!")
    print("Share your public link: https://moneymap-app.streamlit.app")

if __name__ == "__main__":
    main()
