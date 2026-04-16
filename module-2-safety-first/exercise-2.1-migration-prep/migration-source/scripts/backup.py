"""Simple backup utility."""

import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_root="backups"):
    """Create a timestamped backup of a directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = os.path.join(backup_root, f"backup_{timestamp}")

    os.makedirs(backup_dir, exist_ok=True)
    shutil.copytree(source_dir, os.path.join(backup_dir, os.path.basename(source_dir)))

    print(f"Backup created: {backup_dir}")
    return backup_dir

if __name__ == "__main__":
    import sys
    source = sys.argv[1] if len(sys.argv) > 1 else "."
    create_backup(source)
