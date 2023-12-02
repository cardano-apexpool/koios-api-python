"""Ogmios tests"""

from src.koios_api.ogmios import *


def test_tip():
    """Ensure the get_epoch_info exists and returns the expected results"""
    assert get_ogmios
    tip = get_ogmios("2.0", "queryNetwork/tip")
    assert isinstance(tip, dict)
    assert len(tip)
    assert tip["method"] == "queryNetwork/tip"
    assert tip["result"]
