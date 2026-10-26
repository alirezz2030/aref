import os

from flask import Flask, jsonify
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", "6379")),
    decode_responses=True,
    socket_connect_timeout=2,
    socket_timeout=2,
)

@app.get("/")
def index():
    return jsonify(
        message="Hello from Kubernetes",
        environment=os.getenv("APP_ENV", "development"),
    )

@app.get("/health")
def health():
    # Liveness: this checks whether the web process can respond.
    return jsonify(status="alive"), 200

@app.get("/ready")
def ready():
    # Readiness: only receive normal traffic when Redis is reachable.
    try:
        redis_client.ping()
    except redis.RedisError:
        return jsonify(status="not_ready", dependency="redis"), 503
    return jsonify(status="ready"), 200

@app.get("/visits")
def visits():
    # This counter is shared by app replicas because Redis is a separate service.
    count = redis_client.incr("page_visits")
    return jsonify(visits=count)

if __name__ == "__main__":
    # Bind to all interfaces inside the container; Kubernetes Service routes to this port.
    app.run(host="0.0.0.0", port=5000)
