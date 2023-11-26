"""Address section functions"""
from .library import *


def get_address_info(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/address_info
    Get address info - balance, associated stake address (if any) and UTxO set for given addresses
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :returns: The list of address information
    """
    url = API_BASE_URL + "/address_info"
    parameters = {}
    if isinstance(addr, list):
        parameters["_addresses"] = addr
    else:
        parameters["_addresses"] = [addr]
    return koios_post_request(url, parameters)


def get_address_utxos(addr: [str, list], extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/address_utxos
    Get UTxO set for given addresses
    :param addr: Aaddress as string (for one address) or list (for multiple addresses)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list of address UTXOs
    """
    url = API_BASE_URL + "/address_utxos"
    parameters = {}
    if isinstance(addr, list):
        parameters["_addresses"] = addr
    else:
        parameters["_addresses"] = [addr]
    parameters["_extended"] = str(extended).lower()
    utxos = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_post_request(url, parameters)
        utxos += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return utxos


def get_credential_utxos(cred: [str, list], extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/credential_utxos
    Get a list of UTxO against input payment credential array including their balances
    :param cred: Payment credential in hex format as string (for one credential) or list (for multiple credentials)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list of input payment credentials maps
    """
    url = API_BASE_URL + "/credential_utxos"
    parameters = {}
    if isinstance(cred, list):
        parameters["_payment_credentials"] = cred
    else:
        parameters["_payment_credentials"] = [cred]
    parameters["_extended"] = str(extended).lower()
    utxos = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_post_request(url, parameters)
        utxos += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return utxos


def get_address_txs(addr: [str, list], block_height: int = 0) -> list:
    """
    https://api.koios.rest/#post-/address_txs
    Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :param block_height: (optional) Return only the transactions after this block height
    :returns: The list of transaction hashes
    """
    url = API_BASE_URL + "/address_txs"
    parameters = {}
    qs_parameters = {}
    if isinstance(addr, list):
        parameters["_addresses"] = addr
    else:
        parameters["_addresses"] = [addr]
    if block_height > 0:
        parameters["_after_block_height"] = block_height
    txs = []
    offset = 0
    while True:
        if offset > 0:
            qs_parameters["offset"] = offset
        resp = koios_post_request(url, parameters)
        txs += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return txs


def get_credential_txs(cred: [str, list], block_height: int = 0) -> list:
    """
    https://api.koios.rest/#post-/credential_txs
    Get the transaction hash list of input payment credential array,
    optionally filtering after specified block height (inclusive)
    :param cred: Credential(s) as string (for one credential) or list (for multiple credentials)
    :param block_height: (optional) Only fetch information after specific block height
    :returns: The list of transaction hashes
    """
    url = API_BASE_URL + "/credential_txs"
    parameters = {}
    if isinstance(cred, list):
        parameters["_payment_credentials"] = cred
    else:
        parameters["_payment_credentials"] = [cred]
    if block_height:
        parameters["_after_block_height"] = block_height
    return koios_post_request(url, parameters)


def get_address_assets(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/address_assets
    Get the list of all the assets (policy, name and quantity) for given addresses
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :returns: The list of address-owned assets
    """
    url = API_BASE_URL + "/address_assets"
    parameters = {}
    qs_parameters = {}
    if isinstance(addr, list):
        parameters["_addresses"] = addr
    else:
        parameters["_addresses"] = [addr]
    assets = []
    offset = 0
    while True:
        if offset > 0:
            qs_parameters["offset"] = offset
        resp = koios_post_request(url, parameters)
        assets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets
