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

from .conftest import assert_has_key, assert_list_length, assert_non_empty_list, assert_valid_response


@pytest.mark.integration
class TestGetTip:
    """Tests for get_tip."""

    def test_get_tip_exists(self):
        """Ensure get_tip function exists."""
        assert get_tip

    def test_get_tip_returns_single_result(self):
        """Test get_tip returns single result."""
        tip = get_tip()
        assert_list_length(tip, 1)

    def test_get_tip_has_expected_fields(self):
        """Test that tip contains expected fields."""
        tip = get_tip()
        assert_non_empty_list(tip)
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
        """Test get_genesis returns single result."""
        genesis = get_genesis()
        assert_list_length(genesis, 1)

    def test_get_genesis_max_lovelace_supply(self):
        """Test get_genesis returns correct max lovelace supply."""
        genesis = get_genesis()
        assert int(genesis[0]["maxlovelacesupply"]) == 45000000000000000

    def test_get_genesis_has_expected_fields(self):
        """Test that genesis contains expected fields."""
        genesis = get_genesis()
        assert_non_empty_list(genesis)
        expected_fields = ["networkmagic", "networkid", "epochlength", "maxlovelacesupply"]
        for field in expected_fields:
            assert field in genesis[0]


@pytest.mark.integration
class TestGetTotals:
    """Tests for get_totals."""

    def test_get_totals_exists(self):
        """Ensure get_totals function exists."""
        assert get_totals

    def test_get_totals_returns_non_empty(self):
        """Test get_totals returns non-empty list."""
        totals = get_totals()
        assert_non_empty_list(totals)

    def test_get_totals_has_epoch_no(self):
        """Test that totals contain epoch_no field."""
        totals = get_totals()
        assert_has_key(totals, "epoch_no")

    def test_get_totals_has_expected_fields(self):
        """Test that totals contains expected fields."""
        totals = get_totals()
        assert_non_empty_list(totals)
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
        """Test get_param_updates returns non-empty list."""
        param_updates = get_param_updates()
        assert_non_empty_list(param_updates)
        assert len(param_updates) >= 60

    def test_get_param_updates_has_tx_hash(self):
        """Test that param updates contain tx_hash field."""
        param_updates = get_param_updates()
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
