"""Block integration tests."""

import pytest

from src.koios_api.block import get_block_info, get_block_txs, get_blocks

from .conftest import (
    TEST_BLOCK,
    TEST_BLOCK_TX_COUNT,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestBlocks:
    """Tests for get_blocks."""

    def test_blocks_exists(self):
        """Ensure get_blocks function exists."""
        assert get_blocks

    @pytest.mark.parametrize("limit", [1, 10, 50])
    def test_blocks_with_limits(self, limit):
        """Test get_blocks with different limits."""
        blocks = get_blocks(limit=limit)
        assert_list_length(blocks, limit)

    def test_blocks_has_expected_fields(self):
        """Test that blocks contain expected fields."""
        blocks = get_blocks(limit=1)
        assert_non_empty_list(blocks)
        expected_fields = ["hash", "epoch_no", "block_height", "block_time"]
        for field in expected_fields:
            assert field in blocks[0]


@pytest.mark.integration
class TestBlockInfo:
    """Tests for get_block_info."""

    def test_block_info_exists(self):
        """Ensure get_block_info function exists."""
        assert get_block_info

    def test_block_info_single_hash(self):
        """Test get_block_info with single block hash."""
        block_info = get_block_info(TEST_BLOCK)
        assert_list_length(block_info, 1)
        assert block_info[0]["hash"] == TEST_BLOCK
        assert block_info[0]["tx_count"] == TEST_BLOCK_TX_COUNT

    def test_block_info_as_list(self):
        """Test get_block_info with list of block hashes."""
        block_info = get_block_info([TEST_BLOCK])
        assert_list_length(block_info, 1)
        assert block_info[0]["hash"] == TEST_BLOCK

    def test_block_info_has_expected_fields(self):
        """Test that block info contains expected fields."""
        block_info = get_block_info(TEST_BLOCK)
        assert_non_empty_list(block_info)
        expected_fields = ["hash", "epoch_no", "block_height", "tx_count", "pool"]
        for field in expected_fields:
            assert field in block_info[0]


@pytest.mark.integration
class TestBlockTxs:
    """Tests for get_block_txs."""

    def test_block_txs_exists(self):
        """Ensure get_block_txs function exists."""
        assert get_block_txs

    def test_block_txs_returns_transactions(self):
        """Test get_block_txs returns transactions for block."""
        block_txs = get_block_txs(TEST_BLOCK)
        assert_list_length(block_txs, TEST_BLOCK_TX_COUNT)
        assert block_txs[0]["block_hash"] == TEST_BLOCK

    def test_block_txs_as_list(self):
        """Test get_block_txs with list of block hashes."""
        block_txs = get_block_txs([TEST_BLOCK])
        assert_valid_response(block_txs)
        assert len(block_txs) == TEST_BLOCK_TX_COUNT

    def test_block_txs_has_tx_hash(self):
        """Test that block txs contain tx_hash field."""
        block_txs = get_block_txs(TEST_BLOCK)
        assert_has_key(block_txs, "tx_hash")


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestBlockNegativeCases:
    """Negative test cases for block functions."""

    def test_block_info_empty_list(self):
        """Test get_block_info with empty list."""
        block_info = get_block_info([])
        assert_valid_response(block_info)
        assert len(block_info) == 0

    def test_block_txs_empty_list(self):
        """Test get_block_txs with empty list."""
        block_txs = get_block_txs([])
        assert_valid_response(block_txs)
        assert len(block_txs) == 0
