import os

import requests

from tenacity import retry
from tenacity import stop_after_attempt
from tenacity import wait_exponential

BASE_URL = os.getenv(
    "EXTERNAL_SERVICE_URL",
    "http://localhost:8081/enrich"
)

TIMEOUT = int(
    os.getenv(
        "EXTERNAL_SERVICE_TIMEOUT_MS",
        "1500"
    )
) / 1000


@retry(
    stop=stop_after_attempt(
        int(
            os.getenv(
                "RETRY_MAX_ATTEMPTS",
                "3"
            )
        )
    ),
    wait=wait_exponential(
        multiplier=0.1,
        min=0.1,
        max=2
    ),
    reraise=True
)
def fetch_enrichment(user_id: str):

    response = requests.get(
        BASE_URL,
        params={
            "userId": user_id
        },
        timeout=TIMEOUT
    )

    response.raise_for_status()

    return response.json()