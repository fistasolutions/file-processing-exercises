#\!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('APP_ENV', 'dev')
    from src.app import app
    app.run()

if __name__ == '__main__':
    main()
