import os
import time
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(
        {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
        }
    )


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Welcome to ACME Inc!",
            "service": "web-application",
            "version": "1.0.0",
            "endpoints": {"health": "/health", "info": "/api/info"},
        }
    )


@app.route("/api/info")
def info():
    return jsonify(
        {
            "application": "ACME Web Application",
            "version": "1.0.0",
            "environment": os.environ.get("FLASK_ENV", "development"),
            "uptime": time.time(),
        }
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    print(f"ACME Web App running on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
