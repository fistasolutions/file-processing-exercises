"""Helper utilities for the inventory system."""

import os
import json


def format_currency(amount):
    """Format a number as currency string."""
    return f"${amount:,.2f}"


def validate_quantity(quantity):
    """Ensure quantity is a positive integer."""
    if not isinstance(quantity, int) or quantity < 0:
        raise ValueError(f"Quantity must be a non-negative integer, got {quantity}")
    return quantity


def validate_price(price):
    """Ensure price is a positive number."""
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError(f"Price must be a non-negative number, got {price}")
    return round(float(price), 2)


def backup_file(filepath):
    """Create a backup copy of a file."""
    if os.path.exists(filepath):
        backup_path = filepath + ".bak"
        with open(filepath, "r") as src:
            with open(backup_path, "w") as dst:
                dst.write(src.read())
        return backup_path
    return None


def load_config():
    """Load app configuration — reads from config.json in project root."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    with open(config_path, "r") as f:
        return json.load(f)
