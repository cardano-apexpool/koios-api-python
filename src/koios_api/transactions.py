"""Transactions section functions"""
from .library import *


def get_tx_info(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_info
    Get detailed information about transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of detailed information about transaction(s)
    """
    url = API_BASE_URL + "/tx_info"
    parameters = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, parameters)


def get_utxo_info(utxos: [str, list], extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/utxo_info
    Get UTxO set for requested UTxO references
    :param utxos: utxos as a string (for one utxo) or list (for multiple utxos)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list of UTXO details
    """
    url = API_BASE_URL + "/utxo_info"
    parameters = {}
    if isinstance(utxos, list):
        parameters["_utxo_refs"] = utxos
    else:
        parameters["_utxo_refs"] = [utxos]
    if isinstance(extended, bool):
        parameters["_extended"] = str(extended).lower()
    return koios_post_request(url, parameters)


def get_tx_metadata(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_metadata
    Get metadata information (if any) for given transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of metadata information present in each of the transactions queried
    """
    url = API_BASE_URL + "/tx_metadata"
    parameters = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, parameters)


def get_tx_metalabels() -> list:
    """
    https://api.koios.rest/#get-/tx_metalabels
    Get a list of all transaction metadata labels
    :returns: The list of known metadata labels
    """
    url = API_BASE_URL + "/tx_metalabels"
    parameters = {}
    metalabels_list = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        metalabels_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return metalabels_list


def submit_tx(transaction: str) -> str:
    """
    https://api.koios.rest/#post-/submittx
    Submit an already serialized transaction to the network
    :param transaction: transaction in cbor format
    :returns: transaction hash
    """
    url = API_BASE_URL + "/submittx"
    headers = {"Accept": "application/json", "Content-Type": "application/cbor"}
    """
    if KOIOS_API_TOKEN:
        headers["Api-Token"] = "Bearer " + KOIOS_API_TOKEN
    while True:
        try:
            response = requests.post(
                url, headers=headers, data=transaction, timeout=REQUEST_TIMEOUT
            )
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
            logger.warning("retrying...")
    """
    resp = koios_post_request(url, transaction, headers)
    return resp


def get_tx_status(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_status
    Get the number of block confirmations for a given transaction hash list
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transaction confirmation counts
    """
    url = API_BASE_URL + "/tx_status"
    parameters = {}
    if isinstance(txs, list):
        parameters["_tx_hashes"] = txs
    else:
        parameters["_tx_hashes"] = [txs]
    return koios_post_request(url, parameters)
