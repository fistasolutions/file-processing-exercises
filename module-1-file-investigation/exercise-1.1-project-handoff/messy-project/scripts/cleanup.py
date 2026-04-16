"""Cleanup script to remove temporary and stale files."""

import os
import shutil
from datetime import datetime, timedelta

CLEANUP_EXTENSIONS = {".tmp", ".bak", ".pyc", ".log"}
MAX_AGE_DAYS = 30

def cleanup_directory(root_dir, dry_run=True):
    """Remove old temporary files from the project directory."""
    removed = []
    cutoff = datetime.now() - timedelta(days=MAX_AGE_DAYS)

    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip virtual environments and git directories
        dirnames[:] = [d for d in dirnames if d not in {"venv", ".git", "__pycache__", "node_modules"}]

        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            ext = os.path.splitext(filename)[1].lower()

            if ext in CLEANUP_EXTENSIONS:
                mtime = datetime.fromtimestamp(os.path.getmtime(filepath))
                if mtime < cutoff:
                    if dry_run:
                        print(f"Would remove: {filepath} (modified: {mtime.date()})")
                    else:
                        os.remove(filepath)
                        print(f"Removed: {filepath}")
                    removed.append(filepath)

    return removed

if __name__ == "__main__":
    import sys
    dry_run = "--execute" not in sys.argv
    if dry_run:
        print("DRY RUN - no files will be removed. Use --execute to actually delete.")
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results = cleanup_directory(project_root, dry_run=dry_run)
    print(f"\nTotal files {'found' if dry_run else 'removed'}: {len(results)}")
