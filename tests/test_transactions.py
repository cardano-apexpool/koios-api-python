"""Transaction integration tests."""

import pytest

from src.koios_api.transactions import (
    get_tx_info,
    get_tx_metalabels,
    get_tx_metadata,
    get_tx_status,
    get_utxo_info,
    submit_tx,
)

from .conftest import (
    TEST_TX,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestUtxoInfo:
    """Tests for get_utxo_info."""

    def test_utxo_info_exists(self):
        """Ensure get_utxo_info function exists."""
        assert get_utxo_info

    def test_utxo_info_single_utxo(self):
        """Test get_utxo_info with single utxo reference."""
        utxo_info = get_utxo_info(TEST_TX + "#0")
        assert_list_length(utxo_info, 1)
        assert utxo_info[0]["tx_hash"] == TEST_TX

    def test_utxo_info_as_list(self):
        """Test get_utxo_info with list of utxo references."""
        utxo_info = get_utxo_info([TEST_TX + "#0"])
        assert_list_length(utxo_info, 1)

    def test_utxo_info_has_expected_fields(self):
        """Test that utxo info contains expected fields."""
        utxo_info = get_utxo_info(TEST_TX + "#0")
        assert_non_empty_list(utxo_info)
        expected_fields = ["tx_hash", "tx_index", "address", "value"]
        for field in expected_fields:
            assert field in utxo_info[0]


@pytest.mark.integration
class TestTxInfo:
    """Tests for get_tx_info."""

    def test_tx_info_exists(self):
        """Ensure get_tx_info function exists."""
        assert get_tx_info

    def test_tx_info_single_tx(self):
        """Test get_tx_info with single transaction hash."""
        tx_info = get_tx_info(TEST_TX)
        assert_list_length(tx_info, 1)
        assert tx_info[0]["tx_hash"] == TEST_TX

    def test_tx_info_as_list(self):
        """Test get_tx_info with list of transaction hashes."""
        tx_info = get_tx_info([TEST_TX])
        assert_list_length(tx_info, 1)

    def test_tx_info_has_expected_fields(self):
        """Test that tx info contains expected fields."""
        tx_info = get_tx_info(TEST_TX)
        assert_non_empty_list(tx_info)
        expected_fields = ["tx_hash", "block_hash", "block_height", "tx_timestamp"]
        for field in expected_fields:
            assert field in tx_info[0]


@pytest.mark.integration
class TestTxMetadata:
    """Tests for get_tx_metadata."""

    def test_tx_metadata_exists(self):
        """Ensure get_tx_metadata function exists."""
        assert get_tx_metadata

    def test_tx_metadata_single_tx(self):
        """Test get_tx_metadata with single transaction hash."""
        tx_metadata = get_tx_metadata(TEST_TX)
        assert_list_length(tx_metadata, 1)
        assert isinstance(tx_metadata[0]["metadata"], dict)

    def test_tx_metadata_as_list(self):
        """Test get_tx_metadata with list of transaction hashes."""
        tx_metadata = get_tx_metadata([TEST_TX])
        assert_list_length(tx_metadata, 1)


@pytest.mark.integration
class TestTxMetalabels:
    """Tests for get_tx_metalabels."""

    def test_tx_metalabels_exists(self):
        """Ensure get_tx_metalabels function exists."""
        assert get_tx_metalabels

    def test_tx_metalabels_returns_non_empty(self):
        """Test get_tx_metalabels returns non-empty list."""
        tx_metalabels = get_tx_metalabels()
        assert_non_empty_list(tx_metalabels)
        assert_has_key(tx_metalabels, "key")


@pytest.mark.integration
class TestSubmitTx:
    """Tests for submit_tx."""

    def test_submit_tx_exists(self):
        """Ensure submit_tx function exists."""
        assert submit_tx


@pytest.mark.integration
class TestTxStatus:
    """Tests for get_tx_status."""

    def test_tx_status_exists(self):
        """Ensure get_tx_status function exists."""
        assert get_tx_status

    def test_tx_status_single_tx(self):
        """Test get_tx_status with single transaction hash."""
        tx_status = get_tx_status(TEST_TX)
        assert_valid_response(tx_status)

    def test_tx_status_as_list(self):
        """Test get_tx_status with list of transaction hashes."""
        tx_status = get_tx_status([TEST_TX])
        assert_valid_response(tx_status)


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestTransactionNegativeCases:
    """Negative test cases for transaction functions."""

    def test_tx_info_empty_list(self):
        """Test get_tx_info with empty list."""
        tx_info = get_tx_info([])
        assert_valid_response(tx_info)
        assert len(tx_info) == 0

    def test_utxo_info_empty_list(self):
        """Test get_utxo_info with empty list."""
        utxo_info = get_utxo_info([])
        assert_valid_response(utxo_info)
        assert len(utxo_info) == 0

    def test_tx_metadata_empty_list(self):
        """Test get_tx_metadata with empty list."""
        tx_metadata = get_tx_metadata([])
        assert_valid_response(tx_metadata)
        assert len(tx_metadata) == 0
