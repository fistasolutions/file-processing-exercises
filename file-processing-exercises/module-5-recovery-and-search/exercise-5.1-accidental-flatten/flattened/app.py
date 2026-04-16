"""Main application entry point."""

from flask import Flask
from .models.user import User

app = Flask(__name__)

@app.route("/")
def index():
    return {"message": "Task Tracker API v3.0"}

if __name__ == "__main__":
    app.run(debug=True)
