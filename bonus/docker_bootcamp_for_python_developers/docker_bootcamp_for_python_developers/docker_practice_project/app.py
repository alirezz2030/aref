import os

from flask import Flask, jsonify
import redis

app = Flask(__name__)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
)

@app.get("/")
def index():
    return jsonify(
        message="Hello from a containerized Flask app",
        environment=os.getenv("APP_ENV", "development"),
    )

@app.get("/health")
def health():
    # This checks the web process; it does not prove Redis is reachable.
    return jsonify(status="ok"), 200

@app.get("/visits")
def visits():
    # Redis increments a shared counter outside the web container's filesystem.
    count = redis_client.incr("page_visits")
    return jsonify(visits=count)

if __name__ == "__main__":
    # Bind to all interfaces inside the container so the published port can reach Flask.
    app.run(host="0.0.0.0", port=5000)
