import pytest

from be.app.config import ConfigError, Settings, get_key_from_env


def test_get_key_from_env(monkeypatch):
    monkeypatch.setenv("TEST_KEY", "test_value")
    assert get_key_from_env("TEST_KEY") == "test_value"


def test_get_key_from_env_missing(monkeypatch):
    monkeypatch.delenv("TEST_KEY", raising=False)
    with pytest.raises(ConfigError, match="TEST_KEY environment variable is not set"):
        get_key_from_env("TEST_KEY")


def test_settings(monkeypatch):
    monkeypatch.setenv("MARKET_API_KEY", "test_key")
    settings = Settings()
    assert settings.API_BASE_URL == "https://www.alphavantage.co"
