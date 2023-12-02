"""Network tests"""

from src.koios_api.network import *


def test_get_tip():
    """Ensure get_tip exists and returns the expected results"""
    assert get_tip
    tip = get_tip()
    assert isinstance(tip, list)
    assert len(tip) == 1


def test_get_genesis():
    """Ensure get_genesis exists and returns the expected results"""
    assert get_genesis
    genesis = get_genesis()
    assert isinstance(genesis, list)
    assert len(genesis) == 1
    assert int(genesis[0]["maxlovelacesupply"]) == 45000000000000000


def test_get_totals():
    """Ensure get_totals exists and returns the expected results"""
    assert get_totals
    totals = get_totals()
    assert isinstance(totals, list)
    assert len(totals)
    assert totals[0]["epoch_no"]


def test_get_param_updates():
    """Ensure get_param_updates exists and returns the expected results"""
    assert get_param_updates
    param_updates = get_param_updates()
    assert isinstance(param_updates, list)
    assert len(param_updates) >= 60
    assert param_updates[0]["tx_hash"]


def test_get_reserve_withdrawals():
    """Ensure get_reserve_withdrawals exists"""
    assert get_reserve_withdrawals


def test_get_treasury_withdrawals():
    """Ensure get_treasury_withdrawals exists"""
    assert get_treasury_withdrawals
