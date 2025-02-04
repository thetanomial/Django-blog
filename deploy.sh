#!/bin/bash

echo "🚀 Starting Deployment..."

# Navigate to the project directory
cd /var/www/Django-blog || exit

# Pull the latest changes from Git
echo "📥 Pulling latest code from Git..."
git pull origin main  # Change 'main' to your actual branch

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
