"""Ogmios integration tests."""

import pytest

from src.koios_api.ogmios import get_ogmios

from .conftest import assert_valid_response


@pytest.mark.integration
class TestOgmios:
    """Tests for get_ogmios."""

    def test_ogmios_exists(self):
        """Ensure the get_ogmios function exists."""
        assert get_ogmios

    def test_ogmios_tip_query(self):
        """Test get_ogmios with tip query."""
        tip = get_ogmios("2.0", "queryNetwork/tip")
        assert_valid_response(tip, dict)
        assert len(tip) > 0
        assert tip["method"] == "queryNetwork/tip"
        assert "result" in tip

    def test_ogmios_has_expected_structure(self):
        """Test that Ogmios response has expected structure."""
        tip = get_ogmios("2.0", "queryNetwork/tip")
        expected_fields = ["jsonrpc", "method", "result"]
        for field in expected_fields:
            assert field in tip


@pytest.mark.integration
class TestOgmiosQueries:
    """Tests for various Ogmios queries."""

    @pytest.mark.parametrize(
        "method",
        [
            "queryNetwork/tip",
            "queryNetwork/genesisConfiguration",
        ],
    )
    def test_ogmios_various_queries(self, method):
        """Test get_ogmios with various query methods."""
        result = get_ogmios("2.0", method)
        assert_valid_response(result, dict)
        assert result["method"] == method
