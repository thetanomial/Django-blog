#!/bin/bash

echo "🚀 Starting Deployment..."

# Navigate to the project directory
cd /var/www/Django-blog || exit

# Check if the local branch is up-to-date with the remote master branch
echo "🔍 Checking if local branch is up-to-date with remote master..."

# Fetch the latest updates from remote
git fetch origin

# Get the current local branch
current_branch=$(git rev-parse --abbrev-ref HEAD)

# Check for differences between the local and remote branch
local_commit=$(git rev-parse $current_branch)
remote_commit=$(git rev-parse origin/master)

if [ "$local_commit" != "$remote_commit" ]; then
    echo "📥 Pulling latest code from master branch..."
    git pull origin master  # Change 'master' if you're using a different branch
else
    echo "✅ Already up-to-date with remote master."
fi

# Activate the virtual environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Collect static files
echo "🖼️ Collecting static files..."
python manage.py collectstatic --noinput

# Restart Gunicorn and Nginx
echo "🔄 Restarting Gunicorn and Nginx..."
sudo systemctl restart gunicorn
sudo systemctl restart nginx

echo "✅ Deployment Complete!"
