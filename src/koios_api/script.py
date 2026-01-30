"""Script section functions"""
from typing import Any, Union

from .__config__ import API_BASE_URL
from .library import koios_get_request, koios_post_request, paginated_get


def get_script_info(script_hashes: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/script_info
    List of datum information for given datum hashes
    :param script_hashes: Script hash as string (for one script hash) or list (for a list of script hashes)
    :returns resp: The list of script information for given script hashes
    """
    url = API_BASE_URL + "/script_info"
    parameters: dict[str, Any] = {}
    if isinstance(script_hashes, list):
        parameters["_script_hashes"] = script_hashes
    else:
        parameters["_script_hashes"] = [script_hashes]
    return koios_post_request(url, {}, parameters)


def get_native_script_list() -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/native_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all native scripts maps
    """
    url = API_BASE_URL + "/native_script_list"
    return paginated_get(url, {})


def get_plutus_script_list() -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/plutus_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all plutus scripts maps
    """
    url = API_BASE_URL + "/plutus_script_list"
    return paginated_get(url, {})


def get_script_redeemers(script: str) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/script_redeemers
    List of all redeemers for a given script hash
    :param script: script hash
    :returns resp: redeemers list as map
    """
    url = API_BASE_URL + "/script_redeemers"
    parameters: dict[str, Any] = {"_script_hash": script}
    return koios_get_request(url, parameters)


def get_script_utxos(script_hash: str, extended: bool = False) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/asset_utxos
    Get the UTXO information of a list of assets including
    :param script_hash: Script hash
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list UTXOs for given asset list
    """
    url = API_BASE_URL + "/script_utxos"
    parameters: dict[str, Any] = {
        "_script_hash": script_hash.split(".")[0],
        "_extended": str(extended).lower(),
    }
    return paginated_get(url, parameters)


def get_datum_info(datum: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/datum_info
    List of datum information for given datum hashes
    :param datum: datum hash as string (for one datum hash) or list (for a list of datum hashes)
    :returns resp: datum information as list of maps
    """
    url = API_BASE_URL + "/datum_info"
    parameters: dict[str, Any] = {}
    if isinstance(datum, list):
        parameters["_datum_hashes"] = datum
    else:
        parameters["_datum_hashes"] = [datum]
    return koios_post_request(url, {}, parameters)
