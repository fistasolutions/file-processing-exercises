"""Data models for the analytics service."""

from dataclasses import dataclass
from datetime import date

@dataclass
class Customer:
    id: str
    name: str
    email: str
    plan: str
    signup_date: date
    monthly_spend: float

@dataclass
class Transaction:
    txn_id: str
    customer_id: str
    amount: float
    date: date
    type: str
    status: str
