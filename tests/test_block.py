"""Block tests"""

from src.koios_api.block import *

TEST_BLOCK = "8a2e06c0bf499d8feefb43ec739be8de1aeb474f458a21cce381d39f51a055c4"
TX_COUNT = 7


def test_blocks():
    """Ensure get_blocks exists and returns the expected results"""
    assert get_blocks
    blocks = get_blocks(limit=10)
    assert len(blocks) == 10


def test_block_info():
    """Ensure get_block_info exists and returns the expected results"""
    assert get_block_info
    block_info = get_block_info(TEST_BLOCK)
    assert isinstance(block_info, list)
    assert len(block_info) == 1
    assert block_info[0]["hash"] == TEST_BLOCK
    assert block_info[0]["tx_count"] == TX_COUNT


def test_block_txs():
    """Ensure get_block_txs exists and returns the expected results"""
    assert get_block_txs
    block_txs = get_block_txs(TEST_BLOCK)
    assert isinstance(block_txs, list)
    assert len(block_txs) == TX_COUNT
    assert block_txs[0]["block_hash"] == TEST_BLOCK
