"""Main web application."""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Task Manager API"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": "2.0.1"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
