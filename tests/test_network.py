"""Network integration tests."""

import pytest

from src.koios_api.network import (
    get_genesis,
    get_param_updates,
    get_reserve_withdrawals,
    get_tip,
    get_totals,
    get_treasury_withdrawals,
)

from .conftest import (
    TEST_EPOCH,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestGetTip:
    """Tests for get_tip."""

    def test_get_tip_exists(self):
        """Ensure get_tip function exists."""
        assert get_tip

    def test_get_tip_returns_single_result(self):
        """Test get_tip returns single result with expected fields."""
        tip = get_tip()
        assert_list_length(tip, 1)
        expected_fields = ["hash", "epoch_no", "abs_slot", "block_no", "block_time"]
        for field in expected_fields:
            assert field in tip[0]


@pytest.mark.integration
class TestGetGenesis:
    """Tests for get_genesis."""

    def test_get_genesis_exists(self):
        """Ensure get_genesis function exists."""
        assert get_genesis

    def test_get_genesis_returns_single_result(self):
        """Test get_genesis returns single result with correct data."""
        genesis = get_genesis()
        assert_list_length(genesis, 1)
        assert int(genesis[0]["maxlovelacesupply"]) == 45000000000000000
        expected_fields = [
            "networkmagic",
            "networkid",
            "epochlength",
            "maxlovelacesupply",
        ]
        for field in expected_fields:
            assert field in genesis[0]


@pytest.mark.integration
class TestGetTotals:
    """Tests for get_totals."""

    def test_get_totals_exists(self):
        """Ensure get_totals function exists."""
        assert get_totals

    def test_get_totals_for_specific_epoch(self):
        """Test get_totals for specific epoch returns expected data."""
        # Use specific epoch to avoid fetching all epochs
        totals = get_totals(TEST_EPOCH)
        assert_non_empty_list(totals)
        assert_has_key(totals, "epoch_no")
        expected_fields = ["epoch_no", "circulation", "treasury", "reserves"]
        for field in expected_fields:
            assert field in totals[0]


@pytest.mark.integration
class TestGetParamUpdates:
    """Tests for get_param_updates."""

    def test_get_param_updates_exists(self):
        """Ensure get_param_updates function exists."""
        assert get_param_updates

    def test_get_param_updates_returns_non_empty(self):
        """Test get_param_updates returns non-empty list with tx_hash."""
        # This endpoint returns a finite list of protocol parameter updates
        param_updates = get_param_updates()
        assert_non_empty_list(param_updates)
        assert len(param_updates) >= 60
        assert_has_key(param_updates, "tx_hash")


@pytest.mark.integration
class TestGetReserveWithdrawals:
    """Tests for get_reserve_withdrawals."""

    def test_get_reserve_withdrawals_exists(self):
        """Ensure get_reserve_withdrawals function exists."""
        assert get_reserve_withdrawals

    def test_get_reserve_withdrawals_returns_valid_response(self):
        """Test get_reserve_withdrawals returns valid response."""
        reserve_withdrawals = get_reserve_withdrawals()
        assert_valid_response(reserve_withdrawals)


@pytest.mark.integration
class TestGetTreasuryWithdrawals:
    """Tests for get_treasury_withdrawals."""

    def test_get_treasury_withdrawals_exists(self):
        """Ensure get_treasury_withdrawals function exists."""
        assert get_treasury_withdrawals

    def test_get_treasury_withdrawals_returns_valid_response(self):
        """Test get_treasury_withdrawals returns valid response."""
        treasury_withdrawals = get_treasury_withdrawals()
        assert_valid_response(treasury_withdrawals)
