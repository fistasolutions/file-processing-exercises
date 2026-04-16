"""Utility functions for configuration loading and input validation."""

import os
import json
import yaml

def load_config(env="dev"):
    """Load configuration from the config directory."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", f"{env}.env")
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config

def validate_input(data, required=None):
    """Validate that required fields are present in the input data."""
    if not data or not isinstance(data, dict):
        return False
    if required:
        for field in required:
            if field not in data or not data[field]:
                return False
    return True

def parse_csv_line(line, delimiter=","):
    """Parse a single CSV line, handling quoted fields."""
    fields = []
    current = ""
    in_quotes = False
    for char in line:
        if char == '"':
            in_quotes = not in_quotes
        elif char == delimiter and not in_quotes:
            fields.append(current.strip())
            current = ""
        else:
            current += char
    fields.append(current.strip())
    return fields

def format_size(size_bytes):
    """Format file size in human-readable format."""
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"
