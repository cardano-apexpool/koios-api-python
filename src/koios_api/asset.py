"""Asset section functions"""
import warnings
from typing import Any, Union

from .__config__ import API_BASE_URL, API_RESP_COUNT
from .library import koios_post_request, paginated_get, paginated_post


def get_asset_list(
    policy: str = "", offset: int = 0, limit: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/asset_list
    Get the list of all native assets (paginated)
    :param policy: Asset Policy (optional), default: all policies
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of policy IDs and asset names
    """
    url = API_BASE_URL + "/asset_list"
    parameters: dict[str, Any] = {}
    if isinstance(policy, str) and policy != "":
        parameters["policy_id"] = "eq." + policy
    return paginated_get(url, parameters, offset, limit)


def get_policy_asset_list(
    policy: str, offset: int = 0, limit: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/policy_asset_list
    Get the list of asset under the given policy (including balances)
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of detailed information of assets under the same policy
    """
    url = API_BASE_URL + "/policy_asset_info"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    return paginated_get(url, parameters, offset, limit)


def get_asset_token_registry(logo: bool = True) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/asset_token_registry
    Get a list of assets registered via token registry on github
    :param logo: Include the logo in the response if True, otherwise skip it
    :returns: The list of token registry information for each asset
    """
    url = API_BASE_URL + "/asset_token_registry"
    parameters: dict[str, Any] = {"order": "policy_id.asc,asset_name.asc"}
    if not logo:
        parameters[
            "select"
        ] = "policy_id,asset_name,asset_name_ascii,ticker,description,url,decimals"
    return paginated_get(url, parameters)


def get_asset_info(assets: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/asset_info
    Get the information of a list of assets including first minting & token registry metadata
    :param assets: Asset list in the format [policy.name_hex]
    :returns: List of detailed asset information
    """
    url = API_BASE_URL + "/asset_info"
    parameters: dict[str, Any] = {"_asset_list": []}
    if isinstance(assets, str):
        asset_list = [assets]
    else:
        asset_list = assets
    for asset in asset_list:
        asset_split = asset.split(".")
        parameters["_asset_list"].append([asset_split[0], asset_split[1]])
    return koios_post_request(url, {}, parameters)


def get_asset_utxos(
    assets: Union[str, list[str]], extended: bool = False
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/asset_utxos
    Get the UTXO information of a list of assets
    :param assets: Assets as string (for one asset) or list (for multiple assets)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list UTXOs for given asset list
    """
    url = API_BASE_URL + "/asset_utxos"
    parameters: dict[str, Any] = {"_asset_list": []}
    if isinstance(assets, str):
        asset_list = [assets]
    else:
        asset_list = assets
    for asset in asset_list:
        asset_split = asset.split(".")
        parameters["_asset_list"].append([asset_split[0], asset_split[1]])
    parameters["_extended"] = str(extended).lower()
    return paginated_post(url, {"limit": API_RESP_COUNT}, parameters)


def get_asset_history(policy: str, name: str = "") -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/asset_history
    Get the mint/burn history of an asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of asset mint/burn history
    """
    url = API_BASE_URL + "/asset_history"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    if isinstance(name, str) and name != "":
        parameters["_asset_name"] = name
    return paginated_get(url, parameters)


def get_asset_addresses(policy: str, name: str = "") -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/asset_addresses
    Get the list of all addresses holding a given asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of payment addresses holding the given token (including balances)
    """
    url = API_BASE_URL + "/asset_addresses"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    if isinstance(name, str) and name != "":
        parameters["_asset_name"] = name
    return paginated_get(url, parameters)


def get_asset_nft_address(policy: str, name: str = "") -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/asset_nft_address
    Get the address where specified NFT currently reside on
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format
    :returns: The list of payment addresses currently holding the given NFT
    """
    url = API_BASE_URL + "/asset_nft_address"
    parameters: dict[str, Any] = {"_asset_policy": policy, "_asset_name": name}
    return paginated_get(url, parameters)


def get_policy_asset_addresses(
    policy: str, offset: int = 0, limit: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/policy_asset_addresses
    Get the list of addresses with quantity for each asset on the given policy
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of asset names and payment addresses for the given policy (including balances)
    """
    url = API_BASE_URL + "/policy_asset_addresses"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    return paginated_get(url, parameters, offset, limit)


def get_policy_asset_info(
    policy: str, offset: int = 0, limit: int = 0
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/policy_asset_info
    Get the information for all assets under the same policy
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of detailed information of assets under the same policy
    """
    url = API_BASE_URL + "/policy_asset_info"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    return paginated_get(url, parameters, offset, limit)


def get_asset_summary(policy: str, name: str = "") -> list[dict[str, Any]]:
    """
    Get the summary of an asset (total transactions exclude minting/total wallets
    include only wallets with asset balance)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of asset summary information
    """
    url = API_BASE_URL + "/asset_summary"
    parameters: dict[str, Any] = {"_asset_policy": policy, "_asset_name": name}
    return koios_post_request(url, {}, parameters)


def get_asset_txs(
    policy: str, name: str = "", block_height: int = 0, history: bool = False
) -> list[dict[str, Any]]:
    """
    Get the list of all asset transaction hashes (the newest first)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :param block_height: (optional) Return only the transactions after this block height
    :param history: (optional) Include all historical transactions, setting to false includes only the non-empty ones
    :returns: The list of Tx hashes that included the given asset (latest first)
    """
    url = API_BASE_URL + "/asset_txs"
    parameters: dict[str, Any] = {
        "_asset_policy": policy,
        "_asset_name": name,
        "_after_block_height": block_height,
        "_history": str(history).lower(),
    }
    return paginated_get(url, parameters)


def get_asset_address_list(policy: str, name: str = "") -> list[dict[str, Any]]:
    """
    DEPRECATED: Use get_asset_addresses instead.

    https://api.koios.rest/#get-/asset_address_list
    Get the list of all addresses holding a given asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the wallets holding the asset and the amount of assets per wallet
    """
    warnings.warn(
        "get_asset_address_list is deprecated, use get_asset_addresses instead",
        DeprecationWarning,
        stacklevel=2,
    )
    url = API_BASE_URL + "/asset_address_list"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    if isinstance(name, str) and name != "":
        parameters["_asset_name"] = name
    return paginated_get(url, parameters)


def get_asset_policy_info(policy: str) -> list[dict[str, Any]]:
    """
    DEPRECATED: Use get_policy_asset_info instead.

    https://api.koios.rest/#get-/asset_policy_info
    Get the information for all assets under the same policy
    :param policy: Asset Policy
    :returns: List of maps with the policy assets
    """
    warnings.warn(
        "get_asset_policy_info is deprecated, use get_policy_asset_info instead",
        DeprecationWarning,
        stacklevel=2,
    )
    url = API_BASE_URL + "/asset_policy_info"
    parameters: dict[str, Any] = {"_asset_policy": policy}
    return paginated_get(url, parameters)
