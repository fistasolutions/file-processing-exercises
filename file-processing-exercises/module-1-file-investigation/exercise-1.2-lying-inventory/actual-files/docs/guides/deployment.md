# Deployment Guide

## Prerequisites

- Docker and Docker Compose installed
- Access to the container registry
- Environment variables configured

## Steps

1. Build the Docker image: `docker build -t analytics-service .`
2. Push to registry: `docker push registry.example.com/analytics-service`
3. SSH into production server
4. Pull latest image
5. Run `docker-compose up -d`
6. Verify health: `curl http://localhost:8080/health`

## Rollback

If deployment fails:

1. Stop current containers: `docker-compose down`
2. Pull previous image tag
3. Restart: `docker-compose up -d`
