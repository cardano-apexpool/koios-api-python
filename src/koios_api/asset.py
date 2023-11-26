"""Asset section functions"""
from .library import *


def get_asset_list(policy: str = "", offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/asset_list
    Get the list of all native assets (paginated)
    :param policy: Asset Policy (optional), default: all policies
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of policy IDs and asset names
    """
    url = API_BASE_URL + "/asset_list"
    parameters = {}
    assets_names_hex = []
    while True:
        if offset > 0:
            parameters["offset"] = offset
        if isinstance(policy, str) and policy != "":
            parameters["policy_id"] = "eq." + policy
        resp = koios_get_request(url, parameters)
        assets_names_hex += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(assets_names_hex):
                assets_names_hex = assets_names_hex[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(assets_names_hex):
            assets_names_hex = assets_names_hex[0:limit]
            break
    return assets_names_hex


def get_policy_asset_list(policy: str, offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/policy_asset_list
    Get the list of asset under the given policy (including balances)
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of detailed information of assets under the same policy
    """
    url = API_BASE_URL + "/policy_asset_info"
    parameters = {"_asset_policy": policy}
    assets = []
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        assets += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(assets):
                assets = assets[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(assets):
            assets = assets[0:limit]
            break
    return assets


def get_asset_token_registry() -> list:
    """
    https://api.koios.rest/#get-/asset_token_registry
    Get a list of assets registered via token registry on github
    :returns: The list of token registry information for each asset
    """
    url = API_BASE_URL + "/asset_token_registry"
    parameters = {}
    assets_token_registry = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        assets_token_registry += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets_token_registry


def get_asset_info(assets: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/asset_info
    Get the information of a list of assets including first minting & token registry metadata
    :param assets: Asset list in the format [policy.name_hex]
    :returns: List of detailed asset information
    """
    url = API_BASE_URL + "/asset_info"
    parameters = {"_asset_list": []}
    if isinstance(assets, str):
        asset_list = [assets]
    else:
        asset_list = assets
    for asset in asset_list:
        asset_split = asset.split(".")
        parameters["_asset_list"].append([asset_split[0], asset_split[1]])
    return koios_post_request(url, parameters)


def get_asset_utxos(assets: [str, list], extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/asset_utxos
    Get the UTXO information of a list of assets
    :param assets: Assets as string (for one asset) or list (for multiple assets)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list UTXOs for given asset list
    """
    url = API_BASE_URL + "/asset_utxos"
    parameters = {"_asset_list": []}
    qs_parameters = {}
    if isinstance(assets, str):
        asset_list = [assets]
    else:
        asset_list = assets
    for asset in asset_list:
        asset_split = asset.split(".")
        parameters["_asset_list"].append([asset_split[0], asset_split[1]])
    parameters["_extended"] = str(extended).lower()
    utxos = []
    offset = 0
    while True:
        if offset > 0:
            qs_parameters["offset"] = offset
        resp = koios_post_request(url, parameters)
        utxos += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return utxos


def get_asset_history(policy: str, name: str = "") -> list:
    """
    https://api.koios.rest/#get-/asset_history
    Get the mint/burn history of an asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of asset mint/burn history
    """
    url = API_BASE_URL + "/asset_history"
    parameters = {"_asset_policy": policy}
    if isinstance(name, str) and name != "":
        parameters["_asset_name"] = name
    assets = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        assets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets


def get_asset_addresses(policy: str, name: str = "") -> list:
    """
    https://api.koios.rest/#get-/asset_addresses
    Get the list of all addresses holding a given asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of payment addresses holding the given token (including balances)
    """
    url = API_BASE_URL + "/asset_addresses"
    parameters = {"_asset_policy": policy}
    if isinstance(name, str) and name != "":
        parameters["_asset_name"] = name
    wallets = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        wallets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return wallets


def get_asset_nft_address(policy: str, name: str = "") -> list:
    """
    https://api.koios.rest/#get-/asset_nft_address
    Get the address where specified NFT currently reside on
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format
    :returns: The list of payment addresses currently holding the given NFT
    """
    url = API_BASE_URL + "/asset_nft_address"
    parameters = {"_asset_policy": policy, "_asset_name": name}
    wallets = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        wallets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return wallets


def get_policy_asset_addresses(policy: str, offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/policy_asset_addresses
    Get the list of addresses with quantity for each asset on the given policy
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of asset names and payment addresses for the given policy (including balances)
    """
    url = API_BASE_URL + "/policy_asset_addresses"
    parameters = {"_asset_policy": policy}
    asset_addresses = []
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        asset_addresses += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(asset_addresses):
                asset_addresses = asset_addresses[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(asset_addresses):
            asset_addresses = asset_addresses[0:limit]
            break
    return asset_addresses


def get_policy_asset_info(policy: str, offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/policy_asset_info
    Get the information for all assets under the same policy
    :param policy: Asset Policy
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of detailed information of assets under the same policy
    """
    url = API_BASE_URL + "/policy_asset_info"
    parameters = {"_asset_policy": policy}
    assets = []
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        assets += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(assets):
                assets = assets[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(assets):
            assets = assets[0:limit]
            break
    return assets


def get_asset_summary(policy: str, name: str = "") -> list:
    """
    Get the summary of an asset (total transactions exclude minting/total wallets
    include only wallets with asset balance)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: The list of asset summary information
    """
    url = API_BASE_URL + "/asset_summary"
    parameters = {"_asset_policy": policy, "_asset_name": name}
    return koios_post_request(url, parameters)


def get_asset_txs(
    policy: str, name: str = "", block_height: int = 0, history: bool = False
) -> list:
    """
    Get the list of all asset transaction hashes (the newest first)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :param block: (optional) Return only the transactions after this block
    :param history: (optional) Include all historical transactions, setting to false includes only the non-empty ones
    :returns: The list of Tx hashes that included the given asset (latest first)
    """
    url = API_BASE_URL + "/asset_txs"
    parameters = {
        "_asset_policy": policy,
        "_asset_name": name,
        "_after_block_height": block_height,
        "_history": str(history).lower(),
    }
    assets_txs = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        assets_txs += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets_txs


def get_asset_address_list(policy: str, name: str = "") -> list:
    """
    DEPRECATED
    https://api.koios.rest/#get-/asset_address_list
    Get the list of all addresses holding a given asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the wallets holding the asset and the amount of assets per wallet
    """
    url = API_BASE_URL + f"/asset_address_list?_asset_policy={policy}"
    if isinstance(name, str) and name != "":
        url += f"&_asset_name={name}"
    wallets = []
    offset = 0
    while True:
        paginated_url = url + f"&offset={offset}"
        while True:
            try:
                response = requests.get(paginated_url, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        wallets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return wallets


def get_asset_policy_info(policy: str) -> list:
    """
    DEPRECATED
    https://api.koios.rest/#get-/asset_policy_info
    Get the information for all assets under the same policy
    :param policy: Asset Policy
    :returns: List of maps with the policy assets
    """
    url = API_BASE_URL + f"/asset_policy_info?_asset_policy={policy}"
    assets = []
    offset = 0
    while True:
        paginated_url = url + f"&offset={offset}"
        while True:
            try:
                response = requests.get(paginated_url, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        assets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets
