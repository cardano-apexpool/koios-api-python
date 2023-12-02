"""Asset tests"""

from src.koios_api.asset import *

TEST_ASSET = "asset100pa5wvqk7xgqava96745yny2wk6tq5v9sr67d"
TEST_NFT_POLICY = "0e14267a8020229adc0184dd25fa3174c3f7d6caadcb4425c70e7c04"
TEST_ASSET_NAME = "756e7369673132393834"
TEST_FT_POLICY = "750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501"


def test_asset_list():
    """Ensure the get_asset_list exists and returns the expected results"""
    assert get_asset_list
    asset_list = get_asset_list(limit=10)
    assert len(asset_list) == 10


def test_policy_asset_list():
    """Ensure the get_policy_asset_list exists and returns the expected results"""
    assert get_policy_asset_list
    asset_list = get_policy_asset_list(TEST_FT_POLICY)
    assert isinstance(asset_list, list)
    assert len(asset_list) > 0
    assert asset_list[0]["fingerprint"]


def test_asset_token_registry():
    """Ensure the get_asset_token_registry exists"""
    assert get_asset_token_registry


def test_asset_info():
    """Ensure the get_asset_info exists and returns the expected results"""
    assert get_asset_info
    asset_info = get_asset_info(TEST_NFT_POLICY + "." + TEST_ASSET_NAME)
    assert isinstance(asset_info, list)
    assert len(asset_info) == 1
    assert asset_info[0]["fingerprint"] == TEST_ASSET


def test_asset_utxos():
    """Ensure the get_asset_utxos exists and returns the expected results"""
    assert get_asset_utxos


def test_asset_history():
    """Ensure the get_asset_history exists and returns the expected results"""
    assert get_asset_history
    asset_history = get_asset_history(TEST_NFT_POLICY, TEST_ASSET_NAME)
    assert isinstance(asset_history, list)
    assert len(asset_history) > 0
    assert asset_history[0]["fingerprint"] == TEST_ASSET


def test_asset_addresses():
    """Ensure the get_asset_addresses exists and returns the expected results"""
    assert get_asset_addresses
    asset_addresses = get_asset_addresses(TEST_NFT_POLICY, TEST_ASSET_NAME)
    assert isinstance(asset_addresses, list)
    assert len(asset_addresses) > 0
    assert asset_addresses[0]["payment_address"]


def test_asset_nft_address():
    """Ensure the get_asset_nft_address exists and returns the expected results"""
    assert get_asset_nft_address
    asset_nft_address = get_asset_nft_address(TEST_NFT_POLICY, TEST_ASSET_NAME)
    assert isinstance(asset_nft_address, list)
    assert len(asset_nft_address) > 0
    assert asset_nft_address[0]["payment_address"]


def test_policy_asset_addresses():
    """Ensure the get_policy_asset_addresses exists and returns the expected results"""
    assert get_policy_asset_addresses
    policy_asset_addresses = get_policy_asset_addresses(TEST_FT_POLICY, limit=10)
    assert isinstance(policy_asset_addresses, list)
    assert len(policy_asset_addresses) == 10
    assert policy_asset_addresses[0]["payment_address"]


def test_policy_asset_info():
    """Ensure the get_policy_asset_info exists and returns the expected results"""
    assert get_policy_asset_info
    policy_asset_info = get_policy_asset_info(TEST_FT_POLICY)
    assert isinstance(policy_asset_info, list)
    assert len(policy_asset_info) > 0
    assert policy_asset_info[0]["mint_cnt"] == 1


def test_asset_summary():
    """Ensure the get_asset_summary exists and returns the expected results"""
    assert get_asset_summary
    asset_summary = get_asset_summary(TEST_NFT_POLICY, TEST_ASSET_NAME)
    assert isinstance(asset_summary, list)
    assert len(asset_summary) > 0
    assert asset_summary[0]["policy_id"] == TEST_NFT_POLICY


def test_asset_txs():
    """Ensure the get_asset_txs exists and returns the expected results"""
    assert get_asset_txs
    asset_txs = get_asset_txs(TEST_NFT_POLICY, TEST_ASSET_NAME)
    assert isinstance(asset_txs, list)
    assert len(asset_txs) > 0
    assert asset_txs[0]["tx_hash"]
