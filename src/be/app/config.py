import os

from pydantic import BaseModel, Field


class Settings(BaseModel):
    """Application configuration"""
    ALPHA_VANTAGE_KEY: str = Field(..., env='MARKET_API_KEY')
    API_BASE_URL: str = "https://www.alphavantage.co"

    class Config:
        frozen = True


# Initialize settings from environment
settings = Settings(
    ALPHA_VANTAGE_KEY=os.getenv('MARKET_API_KEY')
)
