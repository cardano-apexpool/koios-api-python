"""Pool section functions"""
from typing import Any, Union

from .__config__ import API_BASE_URL
from .library import koios_get_request, koios_post_request, paginated_get


def get_pool_list() -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_list
    List of brief info for all pools
    :returns: The list of pool IDs and tickers
    """
    url = API_BASE_URL + "/pool_list"
    return paginated_get(url, {})


def get_pool_info(pool_id: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/pool_info
    Current pool statuses and details for a specified list of pool ids
    :param pool_id: Stake pool bech32 ID as string (for one stake pool)
    or list of stake pool bech32 IDs (for multiple stake pools)
    :returns: The list of pool information
    """
    url = API_BASE_URL + "/pool_info"
    parameters: dict[str, Any] = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    return koios_post_request(url, {}, parameters)


def get_pool_stake_snapshot(pool_id: str) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_stake_snapshot
    Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation
    :param pool_id: stake pool bech32 id
    :returns: The list of pool stake information for 3 snapshots
    """
    url = API_BASE_URL + "/pool_stake_snapshot"
    parameters: dict[str, Any] = {"_pool_bech32": pool_id}
    return koios_get_request(url, parameters)


def get_pool_delegators(pool_id: str) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_delegators
    Return information about live delegators for a given pool
    :param pool_id: stake pool bech32 id
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators"
    parameters: dict[str, Any] = {"_pool_bech32": pool_id}
    return paginated_get(url, parameters)


def get_pool_delegators_history(pool_id: str, epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_delegators_history
    Return information about active delegators (incl. history) for a given pool and epoch number
    (all epochs if not specified)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators_history"
    parameters: dict[str, Any] = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return paginated_get(url, parameters)


def get_pool_blocks(pool_id: str, epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_blocks
    Return information about blocks minted by a given pool for all epochs (or _epoch_no if provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of blocks created by pool
    """
    url = API_BASE_URL + "/pool_blocks"
    parameters: dict[str, Any] = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return paginated_get(url, parameters)


def get_pool_history(pool_id: str, epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_history
    Return information about pool stake, block and reward history in a given epoch _epoch_no
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool history information
    """
    url = API_BASE_URL + "/pool_history"
    parameters: dict[str, Any] = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_get_request(url, parameters)


def get_pool_updates(pool_id: str = "") -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_updates
    Return all pool updates for all pools or only updates for specific pool if specified
    :param pool_id: stake pool bech32 id
    :returns: The list of historical pool updates
    """
    url = API_BASE_URL + "/pool_updates"
    parameters: dict[str, Any] = {}
    if pool_id:
        parameters["_pool_bech32"] = pool_id
    return paginated_get(url, parameters)


def get_pool_registrations(epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_registrations
    Return all pool registrations initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool registrations
    """
    url = API_BASE_URL + "/pool_registrations"
    parameters: dict[str, Any] = {}
    if epoch:
        parameters["_epoch_no"] = epoch
    return paginated_get(url, parameters)


def get_pool_retirements(epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_retirements
    Return all pool retirements initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool retirements
    """
    url = API_BASE_URL + "/pool_retirements"
    parameters: dict[str, Any] = {}
    if epoch:
        parameters["_epoch_no"] = epoch
    return paginated_get(url, parameters)


def get_pool_relays() -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/pool_relays
    A list of registered relays for all currently registered/retiring (not retired) pools
    :returns: The list of pool relay information
    """
    url = API_BASE_URL + "/pool_relays"
    return paginated_get(url, {})


def get_pool_metadata(pool_id: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/pool_metadata
    A list of registered relays for all currently registered/retiring (not retired) pools
    :param pool_id: stake pool bech32 id
    :returns: The list of pool metadata maps
    """
    url = API_BASE_URL + "/pool_metadata"
    parameters: dict[str, Any] = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    return koios_post_request(url, {}, parameters)


def get_retiring_pools() -> list[dict[str, Any]]:
    """
    Get the retiring stake pools list
    :returns: The list of retiring pools maps
    """
    url = API_BASE_URL + "/pool_list"
    parameters: dict[str, Any] = {"pool_status": "eq.retiring"}
    return koios_get_request(url, parameters)
