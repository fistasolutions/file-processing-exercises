# Exercise 4.2 -- Broken Bank

**Debug**: Transactions -- Find and fix 5 transaction safety holes in banking operations

## Goal

Find and fix 5 transaction safety holes in a banking module. Each function "works" in the happy path but has a specific flaw that would corrupt data under failure conditions. The test suite intentionally triggers failures to expose these holes.

## What You Have

- `broken_bank.py` -- Account model and 5 banking functions (transfer, withdraw, batch_deposit, close_account, apply_interest), each with a transaction safety hole.
- `test_bank.py` -- A test suite that validates atomicity by checking account balances after intentional failures.

## Your Tasks

### Step 1: Read the Banking Code

Read `broken_bank.py` and understand what each function is supposed to do. Think adversarially: "What if this line throws an exception? What state would the database be in?"

### Step 2: Run the Tests

Run `python test_bank.py` and observe which tests fail. The tests are designed to trigger the exact failure conditions that expose each safety hole.

### Step 3: Fix Each Safety Hole

The five holes are:

1. **transfer()** -- Commits the debit before adding the credit. If the credit step fails, money vanishes.
2. **withdraw()** -- No check for sufficient balance. Allows withdrawals that drive the balance negative.
3. **batch_deposit()** -- Catches exceptions but does not rollback. Failed deposits leave the session in a corrupted state.
4. **close_account()** -- Deletes the account but does not transfer the remaining balance first. Money vanishes.
5. **apply_interest()** -- No transaction wrapping. Multiple accounts are updated independently, so a failure mid-batch leaves some accounts with interest and others without.

### Step 4: Verify Atomicity

After fixing all bugs, re-run the test suite. The tests verify that:
- Failed transfers leave both accounts unchanged
- Withdrawals respect balance limits
- Failed batch deposits do not corrupt other deposits
- Account closures transfer remaining funds
- Interest is applied to all accounts or none

### Step 5: Write Production Impact

For each bug, write one sentence: "In production, this bug would cause..."

## Expected Results

- All tests in `test_bank.py` pass
- `transfer()` is fully atomic: both accounts change or neither does
- `withdraw()` rejects insufficient funds
- `batch_deposit()` rolls back on failure
- `close_account()` transfers remaining balance before deleting
- `apply_interest()` wraps all updates in a single transaction

## Reflection

1. Bug #1 (partial commit) is the most dangerous. Why is committing after each step worse than committing once at the end?
2. For Bug #2 (no balance check), should you check in Python or use a database CHECK constraint? What are the tradeoffs?
3. If you could add ONE automated check to prevent all five bug categories, what would it be?
