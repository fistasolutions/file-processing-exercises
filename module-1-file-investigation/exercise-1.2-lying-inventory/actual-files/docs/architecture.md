# Architecture Overview

## Components

```
Client → Flask API → PostgreSQL
                  → Redis (cache)
```

## Data Flow

1. Client sends request to Flask API
2. API checks Redis cache for recent queries
3. On cache miss, queries PostgreSQL
4. Results cached in Redis with 5-minute TTL
5. Response returned to client

## File Structure

- `src/` - Application source code
- `data/` - Sample data and fixtures
- `config/` - Configuration files
- `docs/` - Documentation
