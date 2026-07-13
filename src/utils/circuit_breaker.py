import os
import time
from enum import Enum


class CircuitState(Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitBreaker:

    def __init__(self):

        self.failure_threshold = int(
            os.getenv(
                "CIRCUIT_BREAKER_FAILURE_THRESHOLD",
                "5"
            )
        )

        self.reset_timeout = int(
            os.getenv(
                "CIRCUIT_BREAKER_RESET_TIMEOUT_MS",
                "30000"
            )
        ) / 1000

        self.success_threshold = int(
            os.getenv(
                "CIRCUIT_BREAKER_HALF_OPEN_SUCCESS_THRESHOLD",
                "2"
            )
        )

        self.state = CircuitState.CLOSED

        self.failure_count = 0

        self.success_count = 0

        self.last_failure_time = None

    def call(self, func, *args, **kwargs):

        if self.state == CircuitState.OPEN:

            if (
                time.time() - self.last_failure_time
            ) >= self.reset_timeout:

                self.state = CircuitState.HALF_OPEN

            else:

                raise Exception(
                    "Circuit Breaker is OPEN"
                )

        try:

            result = func(*args, **kwargs)

        except Exception:

            self.failure_count += 1

            if self.state == CircuitState.HALF_OPEN:

                self.state = CircuitState.OPEN

                self.last_failure_time = time.time()

                self.success_count = 0

            elif self.failure_count >= self.failure_threshold:

                self.state = CircuitState.OPEN

                self.last_failure_time = time.time()

            raise

        if self.state == CircuitState.HALF_OPEN:

            self.success_count += 1

            if (
                self.success_count
                >= self.success_threshold
            ):

                self.state = CircuitState.CLOSED

                self.failure_count = 0

                self.success_count = 0

        else:

            self.failure_count = 0

        return result