from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "User Profile Management API"
    APP_VERSION: str = "1.0.0"

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    EXTERNAL_SERVICE_URL: str

    EXTERNAL_SERVICE_TIMEOUT_MS: int

    CIRCUIT_BREAKER_FAILURE_THRESHOLD: int
    CIRCUIT_BREAKER_RESET_TIMEOUT_MS: int
    CIRCUIT_BREAKER_HALF_OPEN_SUCCESS_THRESHOLD: int

    RETRY_MAX_ATTEMPTS: int
    RETRY_BASE_DELAY_MS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()