"""Address integration tests."""

import pytest

from src.koios_api.address import (
    get_address_assets,
    get_address_info,
    get_address_txs,
    get_address_utxos,
    get_credential_txs,
    get_credential_utxos,
)

from .conftest import (
    TEST_ADDRESS,
    TEST_CREDENTIAL,
    TEST_STAKE_ADDRESS,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestAddressInfo:
    """Tests for get_address_info."""

    def test_address_info_exists(self):
        """Ensure the get_address_info function exists."""
        assert get_address_info

    def test_address_info_single_address(self):
        """Test get_address_info with single address."""
        address_info = get_address_info(TEST_ADDRESS)
        assert_list_length(address_info, 1)
        assert address_info[0]["stake_address"] == TEST_STAKE_ADDRESS

    def test_address_info_as_list(self):
        """Test get_address_info with list of addresses."""
        address_info = get_address_info([TEST_ADDRESS])
        assert_list_length(address_info, 1)

    def test_address_info_has_expected_fields(self):
        """Test that address info contains expected fields."""
        address_info = get_address_info(TEST_ADDRESS)
        assert_non_empty_list(address_info)
        expected_fields = ["address", "stake_address", "balance"]
        for field in expected_fields:
            assert field in address_info[0]


@pytest.mark.integration
class TestAddressUtxos:
    """Tests for get_address_utxos."""

    def test_address_utxos_exists(self):
        """Ensure the get_address_utxos function exists."""
        assert get_address_utxos

    def test_address_utxos_returns_valid_response(self):
        """Test get_address_utxos returns valid response."""
        address_utxos = get_address_utxos(TEST_ADDRESS)
        assert_valid_response(address_utxos)
        if len(address_utxos) > 0:
            assert address_utxos[0]["address"] == TEST_ADDRESS
            assert address_utxos[0]["stake_address"] == TEST_STAKE_ADDRESS
            assert address_utxos[0]["payment_cred"] == TEST_CREDENTIAL

    def test_address_utxos_as_list(self):
        """Test get_address_utxos with list of addresses."""
        address_utxos = get_address_utxos([TEST_ADDRESS])
        assert_valid_response(address_utxos)


@pytest.mark.integration
class TestCredentialUtxos:
    """Tests for get_credential_utxos."""

    def test_credential_utxos_exists(self):
        """Ensure the get_credential_utxos function exists."""
        assert get_credential_utxos

    def test_credential_utxos_returns_valid_response(self):
        """Test get_credential_utxos returns valid response."""
        credential_utxos = get_credential_utxos(TEST_CREDENTIAL)
        assert_valid_response(credential_utxos)
        if len(credential_utxos) > 0:
            assert credential_utxos[0]["address"] == TEST_ADDRESS
            assert credential_utxos[0]["stake_address"] == TEST_STAKE_ADDRESS
            assert credential_utxos[0]["payment_cred"] == TEST_CREDENTIAL


@pytest.mark.integration
class TestAddressTxs:
    """Tests for get_address_txs."""

    def test_address_txs_exists(self):
        """Ensure the get_address_txs function exists."""
        assert get_address_txs

    def test_address_txs_returns_non_empty(self):
        """Test get_address_txs returns non-empty list."""
        address_txs = get_address_txs(TEST_ADDRESS)
        assert_non_empty_list(address_txs)
        assert_has_key(address_txs, "tx_hash")

    @pytest.mark.parametrize("limit", [1, 5, 10])
    def test_address_txs_with_limits(self, limit):
        """Test get_address_txs with different limits."""
        address_txs = get_address_txs(TEST_ADDRESS, limit=limit)
        assert_valid_response(address_txs)
        assert len(address_txs) <= limit


@pytest.mark.integration
class TestCredentialTxs:
    """Tests for get_credential_txs."""

    def test_credential_txs_exists(self):
        """Ensure the get_credential_txs function exists."""
        assert get_credential_txs

    def test_credential_txs_returns_non_empty(self):
        """Test get_credential_txs returns non-empty list."""
        credential_txs = get_credential_txs(TEST_CREDENTIAL)
        assert_non_empty_list(credential_txs)
        assert_has_key(credential_txs, "tx_hash")


@pytest.mark.integration
class TestAddressAssets:
    """Tests for get_address_assets."""

    def test_address_assets_exists(self):
        """Ensure the get_address_assets function exists."""
        assert get_address_assets

    def test_address_assets_returns_valid_response(self):
        """Test get_address_assets returns valid response."""
        address_assets = get_address_assets(TEST_ADDRESS)
        assert_valid_response(address_assets)
        if len(address_assets) > 0:
            assert address_assets[0]["address"] == TEST_ADDRESS
            assert "policy_id" in address_assets[0]


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestAddressNegativeCases:
    """Negative test cases for address functions."""

    def test_address_info_empty_list(self):
        """Test get_address_info with empty list."""
        address_info = get_address_info([])
        assert_valid_response(address_info)
        assert len(address_info) == 0

    def test_address_utxos_empty_list(self):
        """Test get_address_utxos with empty list."""
        address_utxos = get_address_utxos([])
        assert_valid_response(address_utxos)
        assert len(address_utxos) == 0
