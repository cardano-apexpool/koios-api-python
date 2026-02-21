"""Transactions section functions"""
from typing import Any, Union

from .__config__ import API_BASE_URL
from .library import koios_post_request, koios_post_request_raw, paginated_get


def get_utxo_info(
    utxos: Union[str, list[str]], extended: bool = False
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/utxo_info
    Get UTxO set for requested UTxO references
    :param utxos: utxos as a string (for one utxo) or list (for multiple utxos)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list of UTXO details
    """
    url = API_BASE_URL + "/utxo_info"
    parameters: dict[str, Any] = {}
    if isinstance(utxos, list):
        parameters["_utxo_refs"] = utxos
    else:
        parameters["_utxo_refs"] = [utxos]
    if isinstance(extended, bool):
        parameters["_extended"] = str(extended).lower()
    return koios_post_request(url, {}, parameters)


def get_tx_info(txs: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/tx_info
    Get detailed information about transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of detailed information about transaction(s)
    """
    url = API_BASE_URL + "/tx_info"
    parameters: dict[str, Any] = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, {}, parameters)


def get_tx_metadata(txs: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/tx_metadata
    Get metadata information (if any) for given transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of metadata information present in each of the transactions queried
    """
    url = API_BASE_URL + "/tx_metadata"
    parameters: dict[str, Any] = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, {}, parameters)


def get_tx_metalabels() -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/tx_metalabels
    Get a list of all transaction metadata labels
    :returns: The list of known metadata labels
    """
    url = API_BASE_URL + "/tx_metalabels"
    return paginated_get(url, {})


def submit_tx(transaction: bytes) -> str:
    """
    https://api.koios.rest/#post-/submittx
    Submit an already serialized transaction to the network
    :param transaction: transaction in cbor format (as bytes)
    :returns: transaction hash
    """
    url = API_BASE_URL + "/submittx"
    headers = {"Accept": "application/json", "Content-Type": "application/cbor"}
    return koios_post_request_raw(url, transaction, headers)


def get_tx_status(txs: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/tx_status
    Get the number of block confirmations for a given transaction hash list
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transaction confirmation counts
    """
    url = API_BASE_URL + "/tx_status"
    parameters: dict[str, Any] = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, {}, parameters)
