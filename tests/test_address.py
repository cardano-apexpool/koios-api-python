"""Address tests"""

from src.koios_api.address import *

TEST_ADDRESS = "addr1q9ur45a5t58dyx5mu5zts997s24vxft9uuvwjep25dpym8qxd4gaypy3nndq60wzhhs3lfyjgxpvjq7djwd7rr4avr0qcmdyc0"
TEST_CREDENTIAL = "783ad3b45d0ed21a9be504b814be82aac32565e718e9642aa3424d9c"
TEST_STAKE_ADDRESS = "stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250"


def test_address_info():
    """Ensure the get_address_info exists and returns the expected results"""
    assert get_address_info
    address_info = get_address_info(TEST_ADDRESS)
    assert isinstance(address_info, list)
    assert len(address_info) == 1
    assert address_info[0]["stake_address"] == TEST_STAKE_ADDRESS


def test_address_utxos():
    """Ensure the get_address_utxos exists and returns the expected results"""
    assert get_address_utxos
    address_utxos = get_address_utxos(TEST_ADDRESS)
    assert isinstance(address_utxos, list)
    if len(address_utxos) > 0:
        assert address_utxos[0]["address"] == TEST_ADDRESS
        assert address_utxos[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert address_utxos[0]["payment_cred"] == TEST_CREDENTIAL


def test_credential_utxos():
    """Ensure the get_credential_utxos exists and returns the expected results"""
    assert get_credential_utxos
    credential_utxos = get_credential_utxos(TEST_CREDENTIAL)
    assert isinstance(credential_utxos, list)
    if len(credential_utxos) > 0:
        assert credential_utxos[0]["address"] == TEST_ADDRESS
        assert credential_utxos[0]["stake_address"] == TEST_STAKE_ADDRESS
        assert credential_utxos[0]["payment_cred"] == TEST_CREDENTIAL


def test_address_txs():
    """Ensure the get_address_txs exists and returns the expected results"""
    assert get_address_txs
    address_txs = get_address_txs(TEST_ADDRESS)
    assert isinstance(address_txs, list)
    assert len(address_txs) > 0
    assert address_txs[0]["tx_hash"]


def test_credential_txs():
    """Ensure the get_credential_txs exists and returns the expected results"""
    assert get_credential_txs
    credential_txs = get_credential_txs(TEST_CREDENTIAL)
    assert isinstance(credential_txs, list)
    assert len(credential_txs) > 0
    assert credential_txs[0]["tx_hash"]


def test_address_assets():
    """Ensure the get_address_assets exists and returns the expected results"""
    assert get_address_assets
    address_assets = get_address_assets(TEST_ADDRESS)
    assert isinstance(address_assets, list)
    if len(address_assets) > 0:
        assert address_assets[0]["address"] == TEST_ADDRESS
        assert address_assets[0]["policy_id"]
