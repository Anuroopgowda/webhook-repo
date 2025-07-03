# Webhook Repo

A Flask-based webhook receiver for GitHub events. It captures push, pull request, and merge events from `action-repo`, stores them in MongoDB Atlas, and displays them live on a frontend page.

---

## Tech Stack

- **Flask** (Python) — Webhook endpoint and API
- **MongoDB Atlas** — Cloud database for event storage
- **HTML, JavaScript** — Frontend UI
- **Ngrok** — Expose local server publicly for GitHub webhook

---

## Features

- Receive and log GitHub push, PR, and merge events
- Store events securely in MongoDB
- Live frontend updates every 15 seconds
- Clean and responsive UI with serial numbering

---

## Screenshot

![1751526142372](image/README/1751526142372.png)

---

## How to Run

Install dependencies:

   **pip install -r requirements.txt**

For runing the application:

    **python app.py**
