# Dave's Random Notes

## Redis caching
Tried adding caching to the user endpoint. Works locally but need to figure out
cache invalidation when users are created/deleted. Left the redis dependency in
requirements.txt but it's not actually used in the code yet.

## Database thoughts
SQLite works for dev but we need PostgreSQL for production. The psycopg2 dependency
is in requirements.txt. Haven't written the migration scripts yet.

## That weird bug on Feb 15
Users endpoint was returning 500 for page > 1. Fixed it by changing the pagination
logic in users.py. The old version is in old_version_app.py.bak (I think? or maybe
that's even older).

## Deploy process
1. SSH into server
2. Pull latest from git
3. Run deploy.sh
4. Check /health
There's probably a better way to do this.

## Secrets
Dev secrets are in config/dev.env (NOT committed to git... I hope)
Production secrets are in the cloud provider's secret manager
The API key for the external data service is... somewhere. Check Slack?
