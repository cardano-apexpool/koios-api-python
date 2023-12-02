"""Pool tests"""

from src.koios_api.pool import *

TEST_POOL = "pool155efqn9xpcf73pphkk88cmlkdwx4ulkg606tne970qswczg3asc"


def test_pool_list():
    """Ensure get_pool_list exists and returns the expected results"""
    assert get_pool_list
    pool_list = get_pool_list()
    assert isinstance(pool_list, list)
    assert len(pool_list) > 0
    assert pool_list[0]["pool_id_bech32"].startswith("pool1")


def test_pool_info():
    """Ensure get_pool_info exists and returns the expected results"""
    assert get_pool_info
    pool_info = get_pool_info(TEST_POOL)
    assert isinstance(pool_info, list)
    assert len(pool_info) == 1
    assert pool_info[0]["pool_id_bech32"] == TEST_POOL


def test_pool_stake_snapshot():
    """Ensure get_pool_stake_snapshot exists and returns the expected results"""
    assert get_pool_stake_snapshot
    pool_stake_snapshot = get_pool_stake_snapshot(TEST_POOL)
    assert isinstance(pool_stake_snapshot, list)
    assert len(pool_stake_snapshot) == 3
    assert pool_stake_snapshot[0]["snapshot"] == "Go"


def test_pool_delegators():
    """Ensure get_pool_delegators exists and returns the expected results"""
    assert get_pool_delegators
    pool_delegators = get_pool_delegators(TEST_POOL)
    assert isinstance(pool_delegators, list)
    assert len(pool_delegators) > 0
    assert pool_delegators[0]["stake_address"]


def test_pool_delegators_history():
    """Ensure get_pool_delegators_history exists and returns the expected results"""
    assert get_pool_delegators_history
    pool_delegators_history = get_pool_delegators_history(TEST_POOL, 450)
    assert isinstance(pool_delegators_history, list)
    assert len(pool_delegators_history) == 5
    assert pool_delegators_history[0]["stake_address"]


def test_pool_blocks():
    """Ensure get_pool_blocks exists and returns the expected results"""
    assert get_pool_blocks
    pool_blocks = get_pool_blocks(TEST_POOL, 450)
    assert isinstance(pool_blocks, list)
    assert len(pool_blocks) == 64
    assert int(pool_blocks[0]["epoch_no"]) == 450


def test_pool_history():
    """Ensure get_pool_history exists and returns the expected results"""
    assert get_pool_history
    pool_history = get_pool_history(TEST_POOL, 450)
    assert isinstance(pool_history, list)
    assert len(pool_history) == 1
    assert int(pool_history[0]["epoch_no"]) == 450


def test_pool_updates():
    """Ensure get_pool_updates exists and returns the expected results"""
    assert get_pool_updates
    pool_updates = get_pool_updates(TEST_POOL)
    assert isinstance(pool_updates, list)
    assert len(pool_updates) > 0
    assert pool_updates[0]["tx_hash"]


def test_pool_registrations():
    """Ensure get_pool_registrations exists and returns the expected results"""
    assert get_pool_registrations
    pool_registrations = get_pool_registrations(450)
    assert isinstance(pool_registrations, list)
    assert len(pool_registrations) == 23
    assert int(pool_registrations[0]["active_epoch_no"]) == 453


def test_pool_retirements():
    """Ensure get_pool_retirements exists and returns the expected results"""
    assert get_pool_retirements
    pool_retirements = get_pool_retirements(450)
    assert isinstance(pool_retirements, list)
    assert len(pool_retirements) == 3
    assert int(pool_retirements[0]["active_epoch_no"]) == 451


def test_pool_relays():
    """Ensure get_pool_relays exists and returns the expected results"""
    assert get_pool_relays
    pool_relays = get_pool_relays()
    assert isinstance(pool_relays, list)
    assert len(pool_relays) > 0
    assert pool_relays[0]["pool_id_bech32"]
    assert isinstance(pool_relays[0]["relays"], list)


def test_pool_metadata():
    """Ensure get_pool_metadata exists and returns the expected results"""
    assert get_pool_metadata
    pool_metadata = get_pool_metadata(TEST_POOL)
    assert isinstance(pool_metadata, list)
    assert len(pool_metadata) == 1
    assert pool_metadata[0]["pool_id_bech32"] == TEST_POOL
    assert isinstance(pool_metadata[0]["meta_json"], dict)


def test_retiring_pools():
    """Ensure get_retiring_pools exists and returns the expected results"""
    assert get_retiring_pools
    retiring_pools = get_retiring_pools()
    assert isinstance(retiring_pools, list)
