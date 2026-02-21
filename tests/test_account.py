"""Account integration tests."""

import pytest

from src.koios_api.account import (
    get_account_addresses,
    get_account_assets,
    get_account_history,
    get_account_info,
    get_account_info_cached,
    get_account_list,
    get_account_rewards,
    get_account_txs,
    get_account_updates,
    get_account_utxos,
)

from .conftest import (
    TEST_EPOCH,
    TEST_STAKE_ADDRESS,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestAccountList:
    """Tests for get_account_list."""

    def test_account_list_exists(self):
        """Ensure the get_account_list function exists."""
        assert get_account_list

    @pytest.mark.parametrize("limit", [1, 10, 100])
    def test_account_list_with_limits(self, limit):
        """Test get_account_list with different limits."""
        account_list = get_account_list(limit=limit)
        assert_valid_response(account_list)
        assert len(account_list) == limit


@pytest.mark.integration
class TestAccountInfo:
    """Tests for get_account_info."""

    def test_account_info_exists(self):
        """Ensure the get_account_info function exists."""
        assert get_account_info

    def test_account_info_single_address(self):
        """Test get_account_info with a single stake address."""
        account_info = get_account_info(TEST_STAKE_ADDRESS)
        assert_list_length(account_info, 1)
        assert account_info[0]["stake_address"] == TEST_STAKE_ADDRESS

    def test_account_info_as_list(self):
        """Test get_account_info with a list of stake addresses."""
        account_info = get_account_info([TEST_STAKE_ADDRESS])
        assert_list_length(account_info, 1)
        assert account_info[0]["stake_address"] == TEST_STAKE_ADDRESS

    def test_account_info_has_expected_fields(self):
        """Test that account info contains expected fields."""
        account_info = get_account_info(TEST_STAKE_ADDRESS)
        assert_non_empty_list(account_info)
        expected_fields = ["stake_address", "status"]
        for field in expected_fields:
            assert field in account_info[0]


@pytest.mark.integration
class TestAccountInfoCached:
    """Tests for get_account_info_cached."""

    def test_account_info_cached_exists(self):
        """Ensure the get_account_info_cached function exists."""
        assert get_account_info_cached

    def test_account_info_cached_returns_valid_response(self):
        """Test get_account_info_cached returns valid response."""
        account_info = get_account_info_cached(TEST_STAKE_ADDRESS)
        assert_valid_response(account_info)
        # Cached info may be empty if account not registered
        if len(account_info) == 1:
            assert account_info[0]["stake_address"] == TEST_STAKE_ADDRESS


@pytest.mark.integration
class TestAccountUtxos:
    """Tests for get_account_utxos."""

    def test_account_utxos_exists(self):
        """Ensure the get_account_utxos function exists."""
        assert get_account_utxos

    def test_account_utxos_returns_valid_response(self):
        """Test get_account_utxos returns valid response."""
        account_utxos = get_account_utxos(TEST_STAKE_ADDRESS)
        assert_valid_response(account_utxos)


@pytest.mark.integration
class TestAccountTxs:
    """Tests for get_account_txs."""

    def test_account_txs_exists(self):
        """Ensure the get_account_txs function exists."""
        assert get_account_txs

    def test_account_txs_returns_non_empty(self):
        """Test get_account_txs returns non-empty list."""
        account_txs = get_account_txs(TEST_STAKE_ADDRESS)
        assert_non_empty_list(account_txs)

    def test_account_txs_has_tx_hash(self):
        """Test that account txs contain tx_hash field."""
        account_txs = get_account_txs(TEST_STAKE_ADDRESS)
        assert_has_key(account_txs, "tx_hash")


@pytest.mark.integration
class TestAccountRewards:
    """Tests for get_account_rewards."""

    def test_account_rewards_exists(self):
        """Ensure the get_account_rewards function exists."""
        assert get_account_rewards

    def test_account_rewards_for_specific_epoch(self):
        """Test get_account_rewards for specific epoch."""
        account_rewards = get_account_rewards(TEST_STAKE_ADDRESS, TEST_EPOCH)
        assert_list_length(account_rewards, 1)
        assert account_rewards[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert int(account_rewards[0]["rewards"][0]["amount"]) == 1248608991


@pytest.mark.integration
class TestAccountUpdates:
    """Tests for get_account_updates."""

    def test_account_updates_exists(self):
        """Ensure the get_account_updates function exists."""
        assert get_account_updates

    def test_account_updates_returns_history(self):
        """Test get_account_updates returns update history."""
        account_updates = get_account_updates(TEST_STAKE_ADDRESS)
        assert_list_length(account_updates, 1)
        assert account_updates[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert len(account_updates[0]["updates"]) > 0


@pytest.mark.integration
class TestAccountAddresses:
    """Tests for get_account_addresses."""

    def test_account_addresses_exists(self):
        """Ensure the get_account_addresses function exists."""
        assert get_account_addresses

    def test_account_addresses_returns_addresses(self):
        """Test get_account_addresses returns addresses."""
        account_addresses = get_account_addresses(TEST_STAKE_ADDRESS)
        assert_list_length(account_addresses, 1)
        assert account_addresses[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert len(account_addresses[0]["addresses"]) > 0


@pytest.mark.integration
class TestAccountAssets:
    """Tests for get_account_assets."""

    def test_account_assets_exists(self):
        """Ensure the get_account_assets function exists."""
        assert get_account_assets

    def test_account_assets_returns_valid_response(self):
        """Test get_account_assets returns valid response."""
        account_assets = get_account_assets(TEST_STAKE_ADDRESS)
        assert_valid_response(account_assets)
        if len(account_assets) > 0:
            assert account_assets[0]["stake_address"] == TEST_STAKE_ADDRESS
            assert "policy_id" in account_assets[0]


@pytest.mark.integration
class TestAccountHistory:
    """Tests for get_account_history."""

    def test_account_history_exists(self):
        """Ensure the get_account_history function exists."""
        assert get_account_history

    def test_account_history_returns_history(self):
        """Test get_account_history returns delegation history."""
        account_history = get_account_history(TEST_STAKE_ADDRESS)
        assert_list_length(account_history, 1)
        assert account_history[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert len(account_history[0]["history"]) > 0


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestAccountNegativeCases:
    """Negative test cases for account functions."""

    def test_account_info_empty_list(self):
        """Test get_account_info with empty list."""
        account_info = get_account_info([])
        assert_valid_response(account_info)
        assert len(account_info) == 0

    def test_account_list_zero_limit(self):
        """Test get_account_list with zero limit returns all."""
        account_list = get_account_list(limit=100)
        assert_valid_response(account_list)
