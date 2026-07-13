from src.external.enrichment_client import fetch_enrichment
from src.utils.circuit_breaker import CircuitBreaker

breaker = CircuitBreaker()


class EnrichmentService:

    @staticmethod
    def get_enrichment(user_id: str):

        return breaker.call(
            fetch_enrichment,
            user_id
        )