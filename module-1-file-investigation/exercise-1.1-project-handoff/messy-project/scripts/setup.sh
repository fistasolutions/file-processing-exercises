#!/bin/bash
# Initial setup script for new developers
# Usage: ./setup.sh

set -e

echo "Setting up development environment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment config
if [ ! -f config/dev.env ]; then
    cp config/prod.env.example config/dev.env
    echo "Created config/dev.env - update with your local settings"
fi

# Initialize database
python -c "from src.app import app; print('App initialized successfully')"

echo "Setup complete! Run: flask run"
