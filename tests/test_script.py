"""Script tests"""

from src.koios_api.script import *

TEST_SCRIPT = "30b8e7fa4674409240889f955623c187397e7346d276ab2e845d3a25"
TEST_DATUM = "45b0cfc220ceec5b7c1c62c4d4193d38e4eba48e8815729ce75f9c0ab0e4c1c0"


def test_script_info():
    """Ensure the get_script_info exists and returns the expected results"""
    assert get_script_info
    script_info = get_script_info(TEST_SCRIPT)
    assert isinstance(script_info, list)
    assert len(script_info) == 1
    assert script_info[0]["script_hash"] == TEST_SCRIPT


def test_native_script_list():
    """Ensure the get_native_script_list exists"""
    assert get_native_script_list


def test_plutus_script_list():
    """Ensure the get_plutus_script_list exists"""
    assert get_plutus_script_list


def test_script_redeemers():
    """Ensure the get_script_redeemers exists and returns the expected results"""
    assert get_script_redeemers
    script_redeemers = get_script_redeemers(TEST_SCRIPT)
    assert isinstance(script_redeemers, list)
    assert len(script_redeemers) == 1
    assert script_redeemers[0]["script_hash"] == TEST_SCRIPT


def test_script_utxos():
    """Ensure the get_script_utxos exists and returns the expected results"""
    assert get_script_utxos
    script_utxos = get_script_utxos(TEST_SCRIPT)
    assert isinstance(script_utxos, list)
    assert len(script_utxos) > 0
    assert script_utxos[0]["tx_hash"]


def test_datum_info():
    """Ensure the get_datum_info exists and returns the expected results"""
    assert get_datum_info
    datum_info = get_datum_info(TEST_DATUM)
    assert isinstance(datum_info, list)
    assert len(datum_info) == 1
    assert datum_info[0]["datum_hash"] == TEST_DATUM
