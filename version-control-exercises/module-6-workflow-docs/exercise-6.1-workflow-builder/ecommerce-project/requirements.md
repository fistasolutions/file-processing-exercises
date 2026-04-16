# ShopSimple — Feature Requirements

## Core Features (MVP — Weeks 1-6)

### Product Catalog
- Display a list of products with name, price, image, and description
- Filter products by category (electronics, clothing, books, home)
- Sort products by price (low-high, high-low) and name
- Product detail page with full description

### Shopping Cart
- Add items to cart from product list or detail page
- Update quantities in cart
- Remove items from cart
- Show cart total with item count in navigation
- Persist cart in browser local storage

### Checkout
- Collect shipping information (name, address, email)
- Display order summary before payment
- Stripe sandbox payment integration
- Order confirmation page with order number

### User Accounts
- Registration with email and password
- Login / logout
- Order history page
- Saved shipping addresses

## Nice-to-Have Features (Weeks 7-8)

- Product search by keyword
- Product reviews and ratings
- Inventory tracking (show "out of stock")
- Email confirmation on order
- Admin dashboard for adding products

## Non-Functional Requirements

- Page load time under 2 seconds
- Mobile-responsive design
- Accessible (WCAG 2.1 AA)
- All AI-generated code must be disclosed in PR descriptions
