import os

from pydantic import BaseModel


class ConfigError(ValueError):
    """Configuration related errors."""

    def __init__(self, value: str) -> None:
        super().__init__(f"{value} environment variable is not set")


def get_key_from_env(key: str) -> str:
    """Get a key from the environment variables."""
    value = os.getenv(key)
    if not value:
        raise ConfigError(key)

    return value


class Settings(BaseModel):
    """Application configuration"""

    ALPHA_VANTAGE_KEY: str = get_key_from_env("ALPHA_VANTAGE_KEY")
    API_BASE_URL: str = "https://www.alphavantage.co"

    class Config:
        frozen = True
