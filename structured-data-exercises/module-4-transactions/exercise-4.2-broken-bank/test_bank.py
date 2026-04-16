"""
Test suite for Banking Module.
Run: python test_bank.py

When all 5 transaction safety holes in broken_bank.py are fixed, all tests pass.
"""

import sys


def setup_accounts(session):
    """Create standard test accounts."""
    from broken_bank import Account
    alice = Account(owner_name="Alice", balance=1000.0)
    bob = Account(owner_name="Bob", balance=500.0)
    charlie = Account(owner_name="Charlie", balance=200.0)
    session.add_all([alice, bob, charlie])
    session.commit()
    return alice.id, bob.id, charlie.id


def run_tests():
    errors = []
    passed = 0

    # ── Test 1: Transfer is atomic ────────────────────────────────────
    print("Test 1: transfer() should be atomic (both accounts change or neither)...")
    try:
        from broken_bank import get_engine, get_session, transfer, withdraw, Account

        engine = get_engine()
        session = get_session(engine)
        alice_id, bob_id, charlie_id = setup_accounts(session)

        # Get initial balances
        alice_before = session.get(Account, alice_id).balance
        bob_before = session.get(Account, bob_id).balance

        # Successful transfer
        result = transfer(session, alice_id, bob_id, 200.0)
        assert result["success"] is True, f"Transfer should succeed: {result['message']}"

        alice_after = session.get(Account, alice_id).balance
        bob_after = session.get(Account, bob_id).balance

        assert alice_after == alice_before - 200.0, f"Alice should have {alice_before - 200.0}, has {alice_after}"
        assert bob_after == bob_before + 200.0, f"Bob should have {bob_before + 200.0}, has {bob_after}"

        # Total money in system should be preserved
        total_before = alice_before + bob_before
        total_after = alice_after + bob_after
        assert abs(total_before - total_after) < 0.01, f"Money not conserved: {total_before} vs {total_after}"

        print("  PASSED: Transfer is atomic and preserves total money")
        passed += 1
        session.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 1: {e}")

    # ── Test 2: Withdraw rejects insufficient funds ───────────────────
    print("Test 2: withdraw() should reject insufficient funds...")
    try:
        engine = get_engine()
        session = get_session(engine)
        alice_id, bob_id, charlie_id = setup_accounts(session)

        # Charlie has $200, try to withdraw $500
        result = withdraw(session, charlie_id, 500.0)

        charlie = session.get(Account, charlie_id)
        assert charlie.balance >= 0, f"Balance went negative: ${charlie.balance:.2f}"
        assert result["success"] is False, "Withdraw of more than balance should fail"
        assert charlie.balance == 200.0, f"Balance should be unchanged at $200, got ${charlie.balance:.2f}"
        print("  PASSED: Insufficient withdrawal rejected, balance unchanged")
        passed += 1
        session.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 2: {e}")

    # ── Test 3: Batch deposit rolls back on failure ───────────────────
    print("Test 3: batch_deposit() should rollback failed deposits cleanly...")
    try:
        from broken_bank import batch_deposit

        engine = get_engine()
        session = get_session(engine)
        alice_id, bob_id, charlie_id = setup_accounts(session)

        alice_before = session.get(Account, alice_id).balance

        deposits = [
            {"account_id": alice_id, "amount": 100.0},
            {"account_id": 9999, "amount": 50.0},  # Non-existent account -- should fail
            {"account_id": bob_id, "amount": 75.0},
        ]

        results = batch_deposit(session, deposits)

        # After the batch, verify the session is still usable
        # (not in a corrupted state from un-rolled-back failure)
        try:
            alice_after = session.get(Account, alice_id).balance
            # Alice's deposit should have succeeded
            assert alice_after == alice_before + 100.0, \
                f"Alice should have ${alice_before + 100.0:.2f}, has ${alice_after:.2f}"
            print("  PASSED: Batch deposit handles failures without corrupting session")
            passed += 1
        except Exception as inner_e:
            print(f"  FAILED: Session corrupted after failed deposit -- {inner_e}")
            errors.append(f"Test 3: Session corrupted -- {inner_e}")

        session.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 3: {e}")

    # ── Test 4: Close account transfers remaining balance ─────────────
    print("Test 4: close_account() should transfer remaining balance...")
    try:
        from broken_bank import close_account

        engine = get_engine()
        session = get_session(engine)
        alice_id, bob_id, charlie_id = setup_accounts(session)

        alice_balance = session.get(Account, alice_id).balance
        bob_before = session.get(Account, bob_id).balance

        # Close Alice's account, transfer to Bob
        result = close_account(session, alice_id, transfer_to_id=bob_id)

        # Verify Alice's account is gone
        alice = session.get(Account, alice_id)
        assert alice is None, "Alice's account should be deleted"

        # Verify Bob received Alice's balance
        bob_after = session.get(Account, bob_id).balance
        expected = bob_before + alice_balance
        assert abs(bob_after - expected) < 0.01, \
            f"Bob should have ${expected:.2f} (his ${bob_before:.2f} + Alice's ${alice_balance:.2f}), has ${bob_after:.2f}"

        print("  PASSED: Account closed with balance transfer")
        passed += 1
        session.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 4: {e}")

    # ── Test 5: Interest applied atomically ───────────────────────────
    print("Test 5: apply_interest() should be atomic (all accounts or none)...")
    try:
        from broken_bank import apply_interest

        engine = get_engine()
        session = get_session(engine)
        alice_id, bob_id, charlie_id = setup_accounts(session)

        # Get balances before interest
        balances_before = {}
        for acc_id in [alice_id, bob_id, charlie_id]:
            acc = session.get(Account, acc_id)
            balances_before[acc_id] = acc.balance

        # Apply 10% interest
        result = apply_interest(session, 0.10)
        assert result["success"] is True

        # All accounts should have exactly 10% more
        for acc_id in [alice_id, bob_id, charlie_id]:
            acc = session.get(Account, acc_id)
            expected = balances_before[acc_id] * 1.10
            assert abs(acc.balance - expected) < 0.01, \
                f"Account {acc_id}: expected ${expected:.2f}, got ${acc.balance:.2f}"

        print("  PASSED: Interest applied correctly to all accounts")
        passed += 1
        session.close()
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 5: {e}")

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/5 tests passed")
    if errors:
        print(f"\nFailed tests:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll tests passed! All 5 transaction safety holes are fixed.")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
