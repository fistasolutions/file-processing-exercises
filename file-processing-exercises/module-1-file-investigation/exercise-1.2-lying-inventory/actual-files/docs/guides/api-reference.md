# API Reference

## Endpoints

### GET /api/customers
Returns a paginated list of customers.

Query parameters:
- `page` (int, default: 1)
- `limit` (int, default: 20)
- `plan` (string, optional): Filter by plan type

### GET /api/customers/:id
Returns a single customer by ID.

### GET /api/transactions
Returns transaction history.

Query parameters:
- `customer_id` (string, optional): Filter by customer
- `start_date` (string, optional): YYYY-MM-DD format
- `end_date` (string, optional): YYYY-MM-DD format
- `status` (string, optional): completed|failed|pending

### GET /api/products
Returns all products.

Query parameters:
- `active` (boolean, optional): Filter by active status
