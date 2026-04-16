"""
Banking Module -- Account Operations
WARNING: This file contains 5 transaction safety holes. Do NOT use for real money.
"""

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    owner_name = Column(String(100), nullable=False)
    balance = Column(Float, nullable=False, default=0.0)

    def __repr__(self):
        return f"<Account: {self.owner_name} (${self.balance:.2f})>"


def get_engine():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()


def transfer(session, from_id, to_id, amount):
    """Transfer money between two accounts.

    BUG: Commits the debit BEFORE adding the credit.
    If the credit step fails, the debit is already committed
    and money vanishes from the system.
    """
    from_account = session.query(Account).filter(Account.id == from_id).first()
    to_account = session.query(Account).filter(Account.id == to_id).first()

    if not from_account or not to_account:
        return {"success": False, "message": "Account not found"}

    if from_account.balance < amount:
        return {"success": False, "message": "Insufficient funds"}

    # Debit from source
    from_account.balance -= amount
    session.commit()  # BUG: commits debit before credit

    # Credit to destination
    to_account.balance += amount
    session.commit()

    return {"success": True, "message": f"Transferred ${amount:.2f}"}


def withdraw(session, account_id, amount):
    """Withdraw money from an account.

    BUG: No check for sufficient balance.
    Allows withdrawals that make the balance negative.
    """
    account = session.query(Account).filter(Account.id == account_id).first()
    if not account:
        return {"success": False, "message": "Account not found"}

    # BUG: no balance check -- allows negative balances
    account.balance -= amount
    session.commit()
    return {"success": True, "message": f"Withdrew ${amount:.2f}", "new_balance": account.balance}


def batch_deposit(session, deposits):
    """Process a list of deposits: [{"account_id": 1, "amount": 100}, ...]

    BUG: Catches exceptions but does not rollback.
    After an exception, the session is in an inconsistent state.
    Subsequent operations on this session will behave unpredictably.
    """
    results = []
    for deposit in deposits:
        try:
            account = session.query(Account).filter(Account.id == deposit["account_id"]).first()
            if not account:
                raise ValueError(f"Account {deposit['account_id']} not found")
            account.balance += deposit["amount"]
            session.commit()
            results.append({"account_id": deposit["account_id"], "status": "success"})
        except Exception as e:
            # BUG: catches exception but does NOT rollback
            # The session is now in a dirty state
            results.append({"account_id": deposit["account_id"], "status": f"failed: {e}"})
    return results


def close_account(session, account_id, transfer_to_id=None):
    """Close an account.

    BUG: Deletes the account without transferring the remaining balance.
    Any money in the account is simply lost.
    """
    account = session.query(Account).filter(Account.id == account_id).first()
    if not account:
        return {"success": False, "message": "Account not found"}

    # BUG: deletes account without transferring remaining balance
    session.delete(account)
    session.commit()
    return {"success": True, "message": f"Account {account_id} closed"}


def apply_interest(session, interest_rate):
    """Apply interest to all accounts.

    BUG: No transaction wrapping -- each account is updated independently.
    If the operation fails mid-batch, some accounts get interest and others do not.
    """
    accounts = session.query(Account).all()
    for account in accounts:
        # BUG: each update is committed independently
        interest = account.balance * interest_rate
        account.balance += interest
        session.commit()

    return {"success": True, "message": f"Applied {interest_rate*100:.1f}% interest to {len(accounts)} accounts"}
