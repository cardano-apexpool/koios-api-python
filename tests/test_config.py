"""Config integration tests."""

import pytest

from src.koios_api.__config__ import (
    API_BASE_URL,
    API_RESP_COUNT,
    CARDANO_NET,
    REQUEST_TIMEOUT,
    SLEEP_TIME,
)


@pytest.mark.integration
class TestConfig:
    """Tests for configuration variables."""

    def test_api_base_url_exists(self):
        """Ensure the API_BASE_URL exists and is not empty."""
        assert API_BASE_URL
        assert isinstance(API_BASE_URL, str)
        assert API_BASE_URL.startswith("https://")

    def test_api_base_url_contains_koios(self):
        """Ensure the API_BASE_URL contains koios."""
        assert "koios" in API_BASE_URL

    def test_cardano_net_is_valid(self):
        """Ensure CARDANO_NET is a valid network."""
        valid_networks = ["mainnet", "preprod", "preview", "--testnet-magic 1", "--testnet-magic 2"]
        assert CARDANO_NET in valid_networks or CARDANO_NET.startswith("--")

    def test_sleep_time_is_positive(self):
        """Ensure SLEEP_TIME is a positive integer."""
        assert isinstance(SLEEP_TIME, int)
        assert SLEEP_TIME >= 0

    def test_api_resp_count_is_positive(self):
        """Ensure API_RESP_COUNT is a positive integer."""
        assert isinstance(API_RESP_COUNT, int)
        assert API_RESP_COUNT > 0

    def test_request_timeout_is_positive(self):
        """Ensure REQUEST_TIMEOUT is a positive integer."""
        assert isinstance(REQUEST_TIMEOUT, int)
        assert REQUEST_TIMEOUT > 0


@pytest.mark.unit
class TestConfigDefaults:
    """Unit tests for configuration default values."""

    def test_default_sleep_time(self):
        """Test default sleep time value."""
        assert SLEEP_TIME >= 1

    def test_default_api_resp_count(self):
        """Test default API response count value."""
        assert API_RESP_COUNT >= 100

    def test_default_request_timeout(self):
        """Test default request timeout value."""
        assert REQUEST_TIMEOUT >= 30
