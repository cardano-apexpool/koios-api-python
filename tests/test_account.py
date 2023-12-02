"""Account tests"""

from src.koios_api.account import *

TEST_STAKE_ADDRESS = "stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250"


def test_account_list():
    """Ensure the get_account_list exists and returns the expected results"""
    assert get_account_list
    account_list = get_account_list(limit=10)
    assert isinstance(account_list, list)
    assert len(account_list) == 10


def test_account_info():
    """Ensure the get_account_info exists and returns the expected results"""
    assert get_account_info
    account_info = get_account_info(TEST_STAKE_ADDRESS)
    assert isinstance(account_info, list)
    assert len(account_info) == 1
    assert account_info[0]["stake_address"] == TEST_STAKE_ADDRESS


def test_account_info_cached():
    """Ensure the get_account_info_cached exists and returns the expected results"""
    assert get_account_info_cached
    account_info = get_account_info_cached(TEST_STAKE_ADDRESS)
    assert isinstance(account_info, list)
    assert (
        len(account_info) == 1
        or get_account_info(TEST_STAKE_ADDRESS)[0]["status"] == "not registered"
    )
    if len(account_info) == 1:
        assert account_info[0]["stake_address"] == TEST_STAKE_ADDRESS


def test_account_utxos():
    """Ensure the get_account_utxos exists and returns the expected results"""
    assert get_account_utxos
    account_utxos = get_account_utxos(TEST_STAKE_ADDRESS)
    assert isinstance(account_utxos, list)
    assert (
        len(account_utxos) > 0
        or int(get_account_info(TEST_STAKE_ADDRESS)[0]["total_balance"]) == 0
    )


def test_account_txs():
    """Ensure the get_account_txs exists and returns the expected results"""
    assert get_account_txs
    account_txs = get_account_txs(TEST_STAKE_ADDRESS)
    assert isinstance(account_txs, list)
    assert len(account_txs) > 0


def test_account_rewards():
    """Ensure the get_account_rewards exists and returns the expected results"""
    assert get_account_rewards
    account_rewards = get_account_rewards(TEST_STAKE_ADDRESS, 450)
    assert isinstance(account_rewards, list)
    assert len(account_rewards) == 1
    assert account_rewards[0]["stake_address"] == TEST_STAKE_ADDRESS
    assert int(account_rewards[0]["rewards"][0]["amount"]) == 1248608991


def test_account_updates():
    """Ensure the get_account_updates exists and returns the expected results"""
    assert get_account_updates
    account_updates = get_account_updates(TEST_STAKE_ADDRESS)
    assert isinstance(account_updates, list)
    assert len(account_updates) == 1
    assert account_updates[0]["stake_address"] == TEST_STAKE_ADDRESS
    assert len(account_updates[0]["updates"])


def test_account_addresses():
    """Ensure the get_account_addresses exists and returns the expected results"""
    assert get_account_addresses
    account_addresses = get_account_addresses(TEST_STAKE_ADDRESS)
    assert isinstance(account_addresses, list)
    assert len(account_addresses) == 1
    assert account_addresses[0]["stake_address"] == TEST_STAKE_ADDRESS
    assert len(account_addresses[0]["addresses"])


def test_account_assets():
    """Ensure the get_account_assets exists and returns the expected results"""
    assert get_account_assets
    account_assets = get_account_assets(TEST_STAKE_ADDRESS)
    assert isinstance(account_assets, list)
    if len(account_assets) > 0:
        assert account_assets[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert account_assets[0]["policy_id"]


def test_account_history():
    """Ensure the get_account_history exists and returns the expected results"""
    assert get_account_history
    account_history = get_account_history(TEST_STAKE_ADDRESS)
    assert isinstance(account_history, list)
    assert len(account_history) == 1
    assert account_history[0]["stake_address"] == TEST_STAKE_ADDRESS
    assert len(account_history[0]["history"])
