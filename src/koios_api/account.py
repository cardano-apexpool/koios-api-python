"""Account section functions"""
from typing import Any, Union

from .__config__ import API_BASE_URL, API_RESP_COUNT
from .library import koios_post_request, paginated_get, paginated_post


def get_account_list(offset: int = 0, limit: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/account_list
    Get a list of all stake addresses that have at least 1 transaction
    :param offset: (optional) The offset to start from
    :param limit: (optional) The maximum number of accounts to return
    :returns: The list of account (stake address) IDs
    """
    url = API_BASE_URL + "/account_list"
    return paginated_get(url, {}, offset, limit)


def get_account_info(addr: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_info
    Get the account information for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account information
    """
    url = API_BASE_URL + "/account_info"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    return koios_post_request(url, {}, parameters)


def get_account_info_cached(addr: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_info_cached
    Get the cached account information for given stake addresses
    (effective for performance query against registered accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account information
    """
    url = API_BASE_URL + "/account_info_cached"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    return koios_post_request(url, {}, parameters)


def get_account_utxos(
    addr: Union[str, list[str]], extended: bool = False, offset: int = 0, limit: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/account_utxos
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :param offset: (optional) The offset to start from
    :param limit: (optional) The maximum number of UTxOs to return
    :return: The list of all UTxOs for a given stake address (account)
    """
    url = API_BASE_URL + "/account_utxos"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    parameters["_extended"] = str(extended).lower()
    return paginated_post(url, {"limit": API_RESP_COUNT}, parameters, offset, limit)


def get_account_txs(addr: str, block_height: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/account_txs
    Get a list of all Txs for a given stake address (account)
    :param addr: Stake address
    :param block_height: (optional) Return only the transactions after this block height
    :returns: The list of transactions associated with stake address (account)
    """
    url = API_BASE_URL + "/account_txs"
    parameters: dict[str, Any] = {"_stake_address": addr}
    if block_height > 0:
        parameters["_after_block_height"] = block_height
    return paginated_get(url, parameters)


def get_account_rewards(
    addr: Union[str, list[str]], epoch: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_rewards
    Get the full rewards history (including MIR) for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param epoch: (optional) Epoch, default: current epoch
    :returns: The list of reward history information
    """
    url = API_BASE_URL + "/account_rewards"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_post_request(url, {}, parameters)


def get_account_updates(addr: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_updates
    Get the account updates (registration, deregistration, delegation and withdrawals) for given stake addresses
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account updates information
    """
    url = API_BASE_URL + "/account_updates"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    return koios_post_request(url, {}, parameters)


def get_account_addresses(
    addr: Union[str, list[str]], first_only: bool = False, empty: bool = True
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_addresses
    Get all addresses associated with given staking accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param first_only: Return only the first address if True
    :param empty: Return also addresses with 0 balance if True
    :returns: The list of payment addresses
    """
    url = API_BASE_URL + "/account_addresses"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    parameters["_first_only"] = str(first_only).lower()
    parameters["_empty"] = str(empty).lower()
    return koios_post_request(url, {}, parameters)


def get_account_assets(addr: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_assets
    Get the native asset balance of given accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of assets owned by account
    """
    url = API_BASE_URL + "/account_assets"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    return paginated_post(url, {"limit": API_RESP_COUNT}, parameters)


def get_account_history(
    addr: Union[str, list[str]], epoch: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/account_history
    Get the staking history of given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param epoch: (optional) Epoch to fetch information for, default: all epochs
    :returns: The list of active stake values per epoch
    """
    url = API_BASE_URL + "/account_history"
    parameters: dict[str, Any] = {}
    if isinstance(addr, list):
        parameters["_stake_addresses"] = addr
    else:
        parameters["_stake_addresses"] = [addr]
    if epoch:
        parameters["_epoch_no"] = epoch
    return koios_post_request(url, {}, parameters)
