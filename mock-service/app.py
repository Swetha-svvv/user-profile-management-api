import os
import random
import time

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

FAILURE_RATE = float(
    os.getenv("MOCK_SERVICE_FAILURE_RATE", "0.4")
)

DELAY = int(
    os.getenv("MOCK_SERVICE_DELAY_MS", "200")
)


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.get("/enrich")
def enrich():

    user_id = request.args.get("userId")

    time.sleep(DELAY / 1000)

    if random.random() < FAILURE_RATE:

        return (
            jsonify(
                {
                    "message": "Mock service unavailable"
                }
            ),
            random.choice([500, 503])
        )

    return jsonify(
        {
            "userId": user_id,
            "recentActivity": [
                "Login",
                "Purchase",
                "Profile Update"
            ],
            "loyaltyScore": random.randint(10, 100)
        }
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8081
    )