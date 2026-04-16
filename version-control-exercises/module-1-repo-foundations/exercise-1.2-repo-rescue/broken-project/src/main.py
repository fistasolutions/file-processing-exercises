"""Broken Project — A simple inventory management script with issues."""

import json
import os
from datetime import datetime


def load_inventory(filepath="inventory.json"):
    """Load inventory from JSON file."""
    if not os.path.exists(filepath):
        return {"items": [], "last_updated": None}
    with open(filepath, "r") as f:
        return json.load(f)


def save_inventory(inventory, filepath="inventory.json"):
    """Save inventory to JSON file."""
    inventory["last_updated"] = datetime.now().isoformat()
    with open(filepath, "w") as f:
        json.dump(inventory, f, indent=2)


def add_item(inventory, name, quantity, price):
    """Add an item to inventory."""
    item = {
        "name": name,
        "quantity": quantity,
        "price": price,
        "added": datetime.now().isoformat()
    }
    inventory["items"].append(item)
    return inventory


def remove_item(inventory, name):
    """Remove an item by name."""
    inventory["items"] = [i for i in inventory["items"] if i["name"] != name]
    return inventory


def get_total_value(inventory):
    """Calculate total inventory value."""
    total = 0
    for item in inventory["items"]:
        total += item["quantity"] * item["price"]
    return round(total, 2)


def list_items(inventory):
    """Print all inventory items."""
    if not inventory["items"]:
        print("Inventory is empty.")
        return
    print(f"{'Name':<20} {'Qty':>5} {'Price':>8} {'Value':>10}")
    print("-" * 45)
    for item in inventory["items"]:
        value = item["quantity"] * item["price"]
        print(f"{item['name']:<20} {item['quantity']:>5} ${item['price']:>7.2f} ${value:>9.2f}")
    print("-" * 45)
    print(f"{'Total':>35} ${get_total_value(inventory):>9.2f}")


if __name__ == "__main__":
    inv = load_inventory()
    list_items(inv)
