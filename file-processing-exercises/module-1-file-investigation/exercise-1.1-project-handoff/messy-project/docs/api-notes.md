# API Notes

## Endpoints (as of March 2024)

### GET /health
Returns service health status. No auth required.

### GET /api/users
List all users. Requires Bearer token. Supports pagination via `page` and `limit` query params.

### POST /api/users
Create a new user. Requires `name` and `email` in JSON body.

### POST /api/process
Submit data for pipeline processing. Currently returns placeholder response.
**NOTE**: This endpoint is not fully implemented. Dave was working on it before he left.

## Authentication

All endpoints except /health require an API key in the Authorization header:
```
Authorization: Bearer <api-key>
```

The API key is stored in the environment variable `API_KEY`.

## Known Issues
- Process endpoint returns placeholder data
- No rate limiting implemented
- User deletion has no cascade handling
- Tests may be outdated after March refactor
