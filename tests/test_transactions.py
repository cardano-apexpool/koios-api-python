"""Asset tests"""

from src.koios_api.transactions import *

TEST_TX = "291b5533227331999eca2e63934c1061e5f85993e77747a90d9901413d7bb937"


def test_utxo_info():
    """Ensure get_utxo_info exists and returns the expected results"""
    assert get_utxo_info
    utxo_info = get_utxo_info(TEST_TX + "#0")
    assert isinstance(utxo_info, list)
    assert len(utxo_info) == 1
    assert utxo_info[0]["tx_hash"] == TEST_TX


def test_tx_info():
    """Ensure get_tx_info exists and returns the expected results"""
    assert get_tx_info
    tx_info = get_tx_info(TEST_TX)
    assert isinstance(tx_info, list)
    assert len(tx_info) == 1
    assert tx_info[0]["tx_hash"] == TEST_TX


def test_tx_metadata():
    """Ensure get_tx_metadata exists and returns the expected results"""
    assert get_tx_metadata
    tx_metadata = get_tx_metadata(TEST_TX)
    assert isinstance(tx_metadata, list)
    assert len(tx_metadata) == 1
    assert isinstance(tx_metadata[0]["metadata"], dict)


def test_tx_metalabels():
    """Ensure get_tx_metalabels exists and returns the expected results"""
    assert get_tx_metalabels
    tx_metalabels = get_tx_metalabels()
    assert isinstance(tx_metalabels, list)
    assert len(tx_metalabels) > 0
    assert tx_metalabels[0]["key"]


def test_submit_tx():
    """Ensure submit_tx exists"""
    assert submit_tx


def test_tx_status():
    """Ensure tx_status exists"""
    assert get_tx_status
