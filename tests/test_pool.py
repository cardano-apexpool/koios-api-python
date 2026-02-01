"""Pool integration tests."""

import pytest

from src.koios_api.pool import (
    get_pool_blocks,
    get_pool_delegators,
    get_pool_delegators_history,
    get_pool_history,
    get_pool_info,
    get_pool_list,
    get_pool_metadata,
    get_pool_registrations,
    get_pool_relays,
    get_pool_retirements,
    get_pool_stake_snapshot,
    get_pool_updates,
    get_retiring_pools,
)

from .conftest import (
    TEST_EPOCH,
    TEST_POOL,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestPoolList:
    """Tests for get_pool_list."""

    def test_pool_list_exists(self):
        """Ensure get_pool_list function exists."""
        assert get_pool_list

    def test_pool_list_returns_non_empty(self):
        """Test get_pool_list returns non-empty list with correct format."""
        # Note: get_pool_list() doesn't have a limit param, but returns paginated results
        # We just verify the response format with first page
        pool_list = get_pool_list()
        assert_non_empty_list(pool_list)
        assert pool_list[0]["pool_id_bech32"].startswith("pool1")


@pytest.mark.integration
class TestPoolInfo:
    """Tests for get_pool_info."""

    def test_pool_info_exists(self):
        """Ensure get_pool_info function exists."""
        assert get_pool_info

    def test_pool_info_single_pool(self):
        """Test get_pool_info with single pool ID."""
        pool_info = get_pool_info(TEST_POOL)
        assert_list_length(pool_info, 1)
        assert pool_info[0]["pool_id_bech32"] == TEST_POOL

    def test_pool_info_as_list(self):
        """Test get_pool_info with list of pool IDs."""
        pool_info = get_pool_info([TEST_POOL])
        assert_list_length(pool_info, 1)

    def test_pool_info_has_expected_fields(self):
        """Test that pool info contains expected fields."""
        pool_info = get_pool_info(TEST_POOL)
        assert_non_empty_list(pool_info)
        expected_fields = ["pool_id_bech32", "pool_id_hex", "active_stake", "live_stake"]
        for field in expected_fields:
            assert field in pool_info[0]


@pytest.mark.integration
class TestPoolStakeSnapshot:
    """Tests for get_pool_stake_snapshot."""

    def test_pool_stake_snapshot_exists(self):
        """Ensure get_pool_stake_snapshot function exists."""
        assert get_pool_stake_snapshot

    def test_pool_stake_snapshot_returns_three_snapshots(self):
        """Test get_pool_stake_snapshot returns three snapshots."""
        pool_stake_snapshot = get_pool_stake_snapshot(TEST_POOL)
        assert_list_length(pool_stake_snapshot, 3)
        assert pool_stake_snapshot[0]["snapshot"] == "Go"


@pytest.mark.integration
class TestPoolDelegators:
    """Tests for get_pool_delegators."""

    def test_pool_delegators_exists(self):
        """Ensure get_pool_delegators function exists."""
        assert get_pool_delegators

    def test_pool_delegators_returns_non_empty(self):
        """Test get_pool_delegators returns non-empty list."""
        pool_delegators = get_pool_delegators(TEST_POOL)
        assert_non_empty_list(pool_delegators)
        assert_has_key(pool_delegators, "stake_address")


@pytest.mark.integration
class TestPoolDelegatorsHistory:
    """Tests for get_pool_delegators_history."""

    def test_pool_delegators_history_exists(self):
        """Ensure get_pool_delegators_history function exists."""
        assert get_pool_delegators_history

    def test_pool_delegators_history_for_epoch(self):
        """Test get_pool_delegators_history for specific epoch."""
        pool_delegators_history = get_pool_delegators_history(TEST_POOL, TEST_EPOCH)
        assert_list_length(pool_delegators_history, 5)
        assert_has_key(pool_delegators_history, "stake_address")


@pytest.mark.integration
class TestPoolBlocks:
    """Tests for get_pool_blocks."""

    def test_pool_blocks_exists(self):
        """Ensure get_pool_blocks function exists."""
        assert get_pool_blocks

    def test_pool_blocks_for_epoch(self):
        """Test get_pool_blocks for specific epoch."""
        pool_blocks = get_pool_blocks(TEST_POOL, TEST_EPOCH)
        assert_list_length(pool_blocks, 64)
        assert int(pool_blocks[0]["epoch_no"]) == TEST_EPOCH


@pytest.mark.integration
class TestPoolHistory:
    """Tests for get_pool_history."""

    def test_pool_history_exists(self):
        """Ensure get_pool_history function exists."""
        assert get_pool_history

    def test_pool_history_for_epoch(self):
        """Test get_pool_history for specific epoch."""
        pool_history = get_pool_history(TEST_POOL, TEST_EPOCH)
        assert_list_length(pool_history, 1)
        assert int(pool_history[0]["epoch_no"]) == TEST_EPOCH


@pytest.mark.integration
class TestPoolUpdates:
    """Tests for get_pool_updates."""

    def test_pool_updates_exists(self):
        """Ensure get_pool_updates function exists."""
        assert get_pool_updates

    def test_pool_updates_returns_non_empty(self):
        """Test get_pool_updates returns non-empty list."""
        pool_updates = get_pool_updates(TEST_POOL)
        assert_non_empty_list(pool_updates)
        assert_has_key(pool_updates, "tx_hash")


@pytest.mark.integration
class TestPoolRegistrations:
    """Tests for get_pool_registrations."""

    def test_pool_registrations_exists(self):
        """Ensure get_pool_registrations function exists."""
        assert get_pool_registrations

    def test_pool_registrations_for_epoch(self):
        """Test get_pool_registrations for specific epoch."""
        pool_registrations = get_pool_registrations(TEST_EPOCH)
        assert_list_length(pool_registrations, 23)
        assert int(pool_registrations[0]["active_epoch_no"]) == 453


@pytest.mark.integration
class TestPoolRetirements:
    """Tests for get_pool_retirements."""

    def test_pool_retirements_exists(self):
        """Ensure get_pool_retirements function exists."""
        assert get_pool_retirements

    def test_pool_retirements_for_epoch(self):
        """Test get_pool_retirements for specific epoch."""
        pool_retirements = get_pool_retirements(TEST_EPOCH)
        assert_list_length(pool_retirements, 3)
        assert int(pool_retirements[0]["active_epoch_no"]) == 451


@pytest.mark.integration
class TestPoolRelays:
    """Tests for get_pool_relays."""

    def test_pool_relays_exists(self):
        """Ensure get_pool_relays function exists."""
        assert get_pool_relays

    def test_pool_relays_returns_non_empty(self):
        """Test get_pool_relays returns non-empty list."""
        # Note: get_pool_relays() doesn't have a limit param
        pool_relays = get_pool_relays()
        assert_non_empty_list(pool_relays)
        assert_has_key(pool_relays, "pool_id_bech32")
        assert isinstance(pool_relays[0]["relays"], list)


@pytest.mark.integration
class TestPoolMetadata:
    """Tests for get_pool_metadata."""

    def test_pool_metadata_exists(self):
        """Ensure get_pool_metadata function exists."""
        assert get_pool_metadata

    def test_pool_metadata_single_pool(self):
        """Test get_pool_metadata with single pool ID."""
        pool_metadata = get_pool_metadata(TEST_POOL)
        assert_list_length(pool_metadata, 1)
        assert pool_metadata[0]["pool_id_bech32"] == TEST_POOL
        assert isinstance(pool_metadata[0]["meta_hash"], str)


@pytest.mark.integration
class TestRetiringPools:
    """Tests for get_retiring_pools."""

    def test_retiring_pools_exists(self):
        """Ensure get_retiring_pools function exists."""
        assert get_retiring_pools

    def test_retiring_pools_returns_valid_response(self):
        """Test get_retiring_pools returns valid response."""
        retiring_pools = get_retiring_pools()
        assert_valid_response(retiring_pools)


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestPoolNegativeCases:
    """Negative test cases for pool functions."""

    def test_pool_info_empty_list(self):
        """Test get_pool_info with empty list."""
        pool_info = get_pool_info([])
        assert_valid_response(pool_info)
        assert len(pool_info) == 0

    def test_pool_metadata_empty_list(self):
        """Test get_pool_metadata with empty list."""
        pool_metadata = get_pool_metadata([])
        assert_valid_response(pool_metadata)
        assert len(pool_metadata) == 0
