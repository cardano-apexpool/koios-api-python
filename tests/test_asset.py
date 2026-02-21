"""Asset integration tests."""

import pytest

from src.koios_api.asset import (
    get_asset_addresses,
    get_asset_history,
    get_asset_info,
    get_asset_list,
    get_asset_nft_address,
    get_asset_summary,
    get_asset_token_registry,
    get_asset_txs,
    get_asset_utxos,
    get_policy_asset_addresses,
    get_policy_asset_info,
    get_policy_asset_list,
)

from .conftest import (
    TEST_ASSET,
    TEST_ASSET_NAME,
    TEST_FT_POLICY,
    TEST_NFT_POLICY,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestAssetList:
    """Tests for get_asset_list."""

    def test_asset_list_exists(self):
        """Ensure the get_asset_list function exists."""
        assert get_asset_list

    @pytest.mark.parametrize("limit", [1, 10, 50])
    def test_asset_list_with_limits(self, limit):
        """Test get_asset_list with different limits."""
        asset_list = get_asset_list(limit=limit)
        assert_list_length(asset_list, limit)


@pytest.mark.integration
class TestPolicyAssetList:
    """Tests for get_policy_asset_list."""

    def test_policy_asset_list_exists(self):
        """Ensure the get_policy_asset_list function exists."""
        assert get_policy_asset_list

    def test_policy_asset_list_returns_assets(self):
        """Test get_policy_asset_list returns assets for policy."""
        asset_list = get_policy_asset_list(TEST_FT_POLICY)
        assert_non_empty_list(asset_list)
        assert_has_key(asset_list, "fingerprint")


@pytest.mark.integration
class TestAssetTokenRegistry:
    """Tests for get_asset_token_registry."""

    def test_asset_token_registry_exists(self):
        """Ensure the get_asset_token_registry function exists."""
        assert get_asset_token_registry

    def test_asset_token_registry_without_logo(self):
        """Test get_asset_token_registry without logo (faster response)."""
        # Use logo=False to reduce response size and speed up test
        asset_token_registry = get_asset_token_registry(logo=False)
        assert_non_empty_list(asset_token_registry)


@pytest.mark.integration
class TestAssetInfo:
    """Tests for get_asset_info."""

    def test_asset_info_exists(self):
        """Ensure the get_asset_info function exists."""
        assert get_asset_info

    def test_asset_info_with_dot_notation(self):
        """Test get_asset_info with policy.asset notation."""
        asset_info = get_asset_info(TEST_NFT_POLICY + "." + TEST_ASSET_NAME)
        assert_list_length(asset_info, 1)
        assert asset_info[0]["fingerprint"] == TEST_ASSET

    def test_asset_info_as_list(self):
        """Test get_asset_info with list of assets."""
        asset_info = get_asset_info([TEST_NFT_POLICY + "." + TEST_ASSET_NAME])
        assert_list_length(asset_info, 1)

    def test_asset_info_has_expected_fields(self):
        """Test that asset info contains expected fields."""
        asset_info = get_asset_info(TEST_NFT_POLICY + "." + TEST_ASSET_NAME)
        assert_non_empty_list(asset_info)
        expected_fields = ["policy_id", "asset_name", "fingerprint"]
        for field in expected_fields:
            assert field in asset_info[0]


@pytest.mark.integration
class TestAssetUtxos:  # pylint: disable=R0903
    """Tests for get_asset_utxos."""

    def test_asset_utxos_exists(self):
        """Ensure the get_asset_utxos function exists."""
        assert get_asset_utxos


@pytest.mark.integration
class TestAssetHistory:
    """Tests for get_asset_history."""

    def test_asset_history_exists(self):
        """Ensure the get_asset_history function exists."""
        assert get_asset_history

    def test_asset_history_returns_history(self):
        """Test get_asset_history returns mint/burn history."""
        asset_history = get_asset_history(TEST_NFT_POLICY, TEST_ASSET_NAME)
        assert_non_empty_list(asset_history)
        assert asset_history[0]["fingerprint"] == TEST_ASSET


@pytest.mark.integration
class TestAssetAddresses:
    """Tests for get_asset_addresses."""

    def test_asset_addresses_exists(self):
        """Ensure the get_asset_addresses function exists."""
        assert get_asset_addresses

    def test_asset_addresses_returns_addresses(self):
        """Test get_asset_addresses returns holder addresses."""
        asset_addresses = get_asset_addresses(TEST_NFT_POLICY, TEST_ASSET_NAME)
        assert_non_empty_list(asset_addresses)
        assert_has_key(asset_addresses, "payment_address")


@pytest.mark.integration
class TestAssetNftAddress:
    """Tests for get_asset_nft_address."""

    def test_asset_nft_address_exists(self):
        """Ensure the get_asset_nft_address function exists."""
        assert get_asset_nft_address

    def test_asset_nft_address_returns_address(self):
        """Test get_asset_nft_address returns NFT holder address."""
        asset_nft_address = get_asset_nft_address(TEST_NFT_POLICY, TEST_ASSET_NAME)
        assert_non_empty_list(asset_nft_address)
        assert_has_key(asset_nft_address, "payment_address")


@pytest.mark.integration
class TestPolicyAssetAddresses:
    """Tests for get_policy_asset_addresses."""

    def test_policy_asset_addresses_exists(self):
        """Ensure the get_policy_asset_addresses function exists."""
        assert get_policy_asset_addresses

    @pytest.mark.parametrize("limit", [5, 10])
    def test_policy_asset_addresses_with_limits(self, limit):
        """Test get_policy_asset_addresses with different limits."""
        policy_asset_addresses = get_policy_asset_addresses(TEST_FT_POLICY, limit=limit)
        assert_valid_response(policy_asset_addresses)
        assert len(policy_asset_addresses) == limit
        assert_has_key(policy_asset_addresses, "payment_address")


@pytest.mark.integration
class TestPolicyAssetInfo:
    """Tests for get_policy_asset_info."""

    def test_policy_asset_info_exists(self):
        """Ensure the get_policy_asset_info function exists."""
        assert get_policy_asset_info

    def test_policy_asset_info_returns_info(self):
        """Test get_policy_asset_info returns asset info for policy."""
        policy_asset_info = get_policy_asset_info(TEST_FT_POLICY)
        assert_non_empty_list(policy_asset_info)
        assert policy_asset_info[0]["mint_cnt"] == 1


@pytest.mark.integration
class TestAssetSummary:
    """Tests for get_asset_summary."""

    def test_asset_summary_exists(self):
        """Ensure the get_asset_summary function exists."""
        assert get_asset_summary

    def test_asset_summary_returns_summary(self):
        """Test get_asset_summary returns asset summary."""
        asset_summary = get_asset_summary(TEST_NFT_POLICY, TEST_ASSET_NAME)
        assert_non_empty_list(asset_summary)
        assert asset_summary[0]["policy_id"] == TEST_NFT_POLICY


@pytest.mark.integration
class TestAssetTxs:
    """Tests for get_asset_txs."""

    def test_asset_txs_exists(self):
        """Ensure the get_asset_txs function exists."""
        assert get_asset_txs

    def test_asset_txs_returns_transactions(self):
        """Test get_asset_txs returns transaction history."""
        asset_txs = get_asset_txs(TEST_NFT_POLICY, TEST_ASSET_NAME)
        assert_non_empty_list(asset_txs)
        assert_has_key(asset_txs, "tx_hash")


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestAssetNegativeCases:  # pylint: disable=R0903
    """Negative test cases for asset functions."""

    def test_asset_info_empty_list(self):
        """Test get_asset_info with empty list."""
        asset_info = get_asset_info([])
        assert_valid_response(asset_info)
        assert len(asset_info) == 0
