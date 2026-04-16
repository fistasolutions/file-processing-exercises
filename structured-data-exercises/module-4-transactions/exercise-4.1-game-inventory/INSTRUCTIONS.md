# Exercise 4.1 -- Game Inventory Trading

**Build**: Transactions -- Implement atomic item trades between game players

## Goal

Implement a trading system for a multiplayer game where players exchange items for gold. Every trade must be atomic: either the entire trade completes (item transferred AND gold exchanged), or nothing changes. You will also implement a shop system and a batch trading endpoint that handles partial failures using savepoints.

## What You Have

- `models.py` -- Working Player and Item models with relationships. Player has a username and gold balance. Item has a name, value, and belongs to a player via foreign key.

## Your Tasks

### Step 1: Read the Models

Read `models.py` to understand the Player and Item models and their relationship. Note how items are linked to players via `player_id`.

### Step 2: Implement trade_items()

Create a new file called `trading.py`. Implement:

```python
def trade_items(session, seller_id, buyer_id, item_id, gold_amount):
```

This function must:
1. Validate the item belongs to the seller
2. Validate the buyer has enough gold
3. Transfer the item (change `item.player_id` to buyer)
4. Deduct gold from buyer, add gold to seller
5. Commit -- or rollback everything if ANY step fails
6. Return a dict: `{"success": True/False, "message": "..."}`

### Step 3: Implement buy_from_shop()

```python
def buy_from_shop(session, player_id, item_name, price):
```

This function must:
1. Validate the player has enough gold
2. Create a new Item owned by the player
3. Deduct gold from the player
4. Commit -- or rollback if gold deduction fails (no orphaned items)
5. Return the created item or None on failure

### Step 4: Implement batch_trade()

```python
def batch_trade(session, trades_list):
```

Where `trades_list` is a list of dicts: `[{"seller_id": 1, "buyer_id": 2, "item_id": 3, "gold_amount": 50}, ...]`

This function must:
1. Process each trade using a savepoint (`session.begin_nested()`)
2. If an individual trade fails, rollback only that savepoint (not the whole batch)
3. Track which trades succeeded and which failed
4. Commit all successful trades at the end
5. Return a report: `{"succeeded": [...], "failed": [...]}`

### Step 5: Write Tests

Add a test block at the bottom that:
1. Creates 3 players: "Alice" (1000 gold), "Bob" (500 gold), "Charlie" (200 gold)
2. Creates items: "Legendary Sword" (value 300, owned by Alice), "Magic Shield" (value 150, owned by Bob)
3. Executes a successful trade: Bob buys Legendary Sword from Alice for 400 gold
4. Attempts a trade where Charlie cannot afford an item (should fail cleanly, no state change)
5. Runs a batch of 3 trades where 1 is designed to fail
6. Prints final state of all players and items to verify correctness

## Expected Results

- `trading.py` with 3 transaction-safe functions
- Successful trades update both gold and item ownership atomically
- Failed trades leave the database unchanged (no partial state)
- Batch trades handle individual failures without aborting the entire batch
- Final player gold balances and item ownership are exactly correct

## Reflection

1. Why is it important to validate (check gold balance, verify item ownership) BEFORE starting the transaction, rather than relying on database constraints to catch problems?
2. In the `batch_trade` function, what is a savepoint and how does it differ from a full transaction rollback?
3. If two players try to buy the same item simultaneously, what could go wrong? How would you prevent it?
