#!/bin/bash

echo "🚀 Setting up Git repository for Flask REST API..."

# Initialize git repository (if not already done)
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Add all files
echo "📝 Adding all files to git..."
git add .

# Check if there are any changes to commit
if git diff --cached --quiet; then
    echo "✅ No changes to commit. All files are already up to date."
else
    # Commit the changes
    echo "💾 Committing changes..."
    git commit -m "Initial commit: Flask REST API with companies endpoint
    
    - Flask application with SQLAlchemy ORM
    - Companies CRUD API endpoints
    - SQLite database configuration
    - Modern Flask dependencies
    - RESTful API structure"
    
    echo "✅ Changes committed successfully!"
fi

# Check if remote origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "🌐 No remote repository configured."
    echo ""
    echo "To connect to GitHub:"
    echo "1. Create a new repository on GitHub"
    echo "2. Run: git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
    echo "3. Run: git push -u origin main"
    echo ""
    echo "Or if you want to use SSH:"
    echo "2. Run: git remote add origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git"
    echo "3. Run: git push -u origin main"
else
    echo "🌐 Remote repository found:"
    git remote get-url origin
    echo ""
    echo "To push to GitHub, run:"
    echo "git push -u origin main"
fi

echo ""
echo "📋 Current git status:"
git status --short 