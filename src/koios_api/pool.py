"""Pool section functions"""
from .library import *


def get_pool_list() -> list:
    """
    https://api.koios.rest/#get-/pool_list
    List of brief info for all pools
    :returns: The list of pool IDs and tickers
    """
    url = API_BASE_URL + "/pool_list"
    parameters = {}
    pools_list = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        pools_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return pools_list


def get_pool_info(pool_id: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/pool_info
    Current pool statuses and details for a specified list of pool ids
    :param pool_id: Stake pool bech32 ID as string (for one stake pool)
    or list of stake pool bech32 IDs (for multiple stake pools)
    :returns: The list of pool information
    """
    url = API_BASE_URL + "/pool_info"
    parameters = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    return koios_post_request(url, parameters)


def get_pool_stake_snapshot(pool_id: str) -> list:
    """
    https://api.koios.rest/#get-/pool_stake_snapshot
    Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation
    :param pool_id: stake pool bech32 id
    :returns: The list of pool stake information for 3 snapshots
    """
    url = API_BASE_URL + "/pool_stake_snapshot"
    parameters = {"_pool_bech32": pool_id}
    return koios_get_request(url, parameters)


def get_pool_delegators(pool_id: str) -> list:
    """
    https://api.koios.rest/#get-/pool_delegators
    Return information about live delegators for a given pool
    :param pool_id: stake pool bech32 id
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators"
    parameters = {"_pool_bech32": pool_id}
    delegators = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        delegators += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return delegators


def get_pool_delegators_history(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_delegators_history
    Return information about active delegators (incl. history) for a given pool and epoch number
    (all epochs if not specified)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators_history"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    delegators = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        delegators += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return delegators


def get_pool_blocks(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_blocks
    Return information about blocks minted by a given pool for all epochs (or _epoch_no if provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of blocks created by pool
    """
    url = API_BASE_URL + "/pool_blocks"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    blocks = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        blocks += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return blocks


def get_pool_history(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_history
    Return information about pool stake, block and reward history in a given epoch _epoch_no
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool history information
    """
    url = API_BASE_URL + "/pool_history"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_get_request(url, parameters)


def get_pool_updates(pool_id: str = "") -> list:
    """
    https://api.koios.rest/#get-/pool_updates
    Return all pool updates for all pools or only updates for specific pool if specified
    :param pool_id: stake pool bech32 id
    :returns: The list of historical pool updates
    """
    url = API_BASE_URL + "/pool_updates"
    parameters = {}
    pool_updates = []
    offset = 0
    if pool_id:
        parameters["_pool_bech32"] = pool_id
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        pool_updates += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return pool_updates


def get_pool_registrations(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_registrations
    Return all pool registrations initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool registrations
    """
    url = API_BASE_URL + "/pool_registrations"
    parameters = {}
    registrations = []
    offset = 0
    if epoch:
        parameters["_epoch_no"] = epoch
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        registrations += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return registrations


def get_pool_retirements(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_retirements
    Return all pool retirements initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool retirements
    """
    url = API_BASE_URL + "/pool_retirements"
    parameters = {}
    retirements = []
    offset = 0
    if epoch:
        parameters["_epoch_no"] = epoch
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        retirements += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return retirements


def get_pool_relays() -> list:
    """
    https://api.koios.rest/#get-/pool_relays
    A list of registered relays for all currently registered/retiring (not retired) pools
    :returns: The list of pool relay information
    """
    url = API_BASE_URL + "/pool_relays"
    parameters = {}
    relays = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        relays += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return relays


def get_pool_metadata(pool_id: str) -> list:
    """
    https://api.koios.rest/#post-/pool_metadata
    A list of registered relays for all currently registered/retiring (not retired) pools
    :param pool_id: stake pool bech32 id
    :returns: The list of pool metadata maps
    """
    url = API_BASE_URL + "/pool_metadata"
    parameters = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    return koios_post_request(url, parameters)


def get_retiring_pools() -> list:
    """
    Get the retiring stake pools list
    :returns: The list of retiring pools maps
    """
    url = API_BASE_URL + "/pool_list"
    parameters = {"pool_status": "eq.retiring"}
    return koios_get_request(url, parameters)
