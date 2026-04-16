#!/bin/bash
# Deployment script for the data pipeline service
# Usage: ./deploy.sh [environment]

set -e

ENV=${1:-dev}
echo "Deploying to $ENV environment..."

if [ "$ENV" = "prod" ]; then
    echo "WARNING: Deploying to production!"
    read -p "Are you sure? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

# Build the Docker image
docker build -t data-pipeline:latest .

# Run database migrations (TODO: implement actual migrations)
echo "Running migrations..."
# python manage.py migrate

# Start the service
docker-compose up -d

echo "Deployment complete. Check health: curl http://localhost:${PORT:-5000}/health"
