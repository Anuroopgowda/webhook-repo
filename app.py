

from flask import Flask, request, jsonify, send_from_directory
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection — replace with your actual string
client = MongoClient("mongodb+srv://anuroop:anuroop@cluster0.r7ik2a3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["github_events"]
collection = db["events"]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    author = "unknown"
    action = "push"
    from_branch = None
    to_branch = None
    timestamp = datetime.utcnow().isoformat()

    # Push
    if "pusher" in data:
        author = data.get("pusher", {}).get("name", "unknown")
        to_branch = data.get("ref", "").split("/")[-1]
        action = "push"

    # Pull request
    if "pull_request" in data:
        author = data["pull_request"]["user"]["login"]
        from_branch = data["pull_request"]["head"]["ref"]
        to_branch = data["pull_request"]["base"]["ref"]
        action = "pull_request"

        if data.get("action") == "closed" and data["pull_request"].get("merged"):
            action = "merge"

    event_doc = {
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    collection.insert_one(event_doc)
    return jsonify({"status": "success"}), 200

@app.route("/events", methods=["GET"])
def get_events():
    events = list(collection.find({}, {"_id": 0}))
    return jsonify(events)

@app.route("/")
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
