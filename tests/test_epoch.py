"""Epoch tests"""

from src.koios_api.epoch import *


def test_epoch_info():
    """Ensure get_epoch_info exists and returns the expected results"""
    assert get_epoch_info
    epoch_info = get_epoch_info()
    assert isinstance(epoch_info, list)
    assert len(epoch_info)
    epoch_info = get_epoch_info(450)
    assert isinstance(epoch_info, list)
    assert len(epoch_info) == 1
    assert epoch_info[0]["epoch_no"] == 450


def test_epoch_params():
    """Ensure get_epoch_params exists and returns the expected results"""
    assert get_epoch_params
    epoch_params = get_epoch_params()
    assert isinstance(epoch_params, list)
    assert len(epoch_params)
    epoch_params = get_epoch_params(450)
    assert isinstance(epoch_params, list)
    assert len(epoch_params) == 1
    assert epoch_params[0]["epoch_no"] == 450


def test_epoch_block_protocols():
    """Ensure get_epoch_block_protocols exists and returns the expected results"""
    assert get_epoch_block_protocols
    epoch_block_protocols = get_epoch_block_protocols(450)
    assert isinstance(epoch_block_protocols, list)
    assert len(epoch_block_protocols) == 1
    assert epoch_block_protocols[0]["proto_major"] == 8
