"""Network section functions"""
from .library import *


def get_tip() -> list:
    """
    https://api.koios.rest/#get-/tip
    Get the tip info about the latest block seen by chain
    :returns: The list of block summary (limit+paginated)
    """
    url = API_BASE_URL + "/tip"
    return koios_get_request(url, {})


def get_genesis() -> list:
    """
    https://api.koios.rest/#get-/genesis
    Get the Genesis parameters used to start specific era on chain
    :returns: The list of genesis parameters used to start each era on chain
    """
    url = API_BASE_URL + "/genesis"
    return koios_get_request(url, {})


def get_totals(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/totals
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace
    for specified epoch, all epochs if empty
    :param epoch: (Optional) The epoch
    :returns: The list of supply/reserves/utxo/fees/treasury stats
    """
    url = API_BASE_URL + "/totals"
    parameters = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_get_request(url, parameters)


def get_param_updates() -> list:
    """
    https://api.koios.rest/#get-/param_updates
    Get all parameter update proposals submitted to the chain starting Shelley era
    :returns: The list of unique param update proposals submitted on chain
    """
    url = API_BASE_URL + "/param_updates"
    return koios_get_request(url, {})


def get_reserve_withdrawals() -> list:
    """
    https://api.koios.rest/#get-/reserve_withdrawals
    List of all withdrawals from reserves against stake accounts
    :returns: The list of withdrawals from reserves against stake accounts
    """
    url = API_BASE_URL + "/reserve_withdrawals"
    parameters = {}
    withdrawals = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        withdrawals += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return withdrawals


def get_treasury_withdrawals() -> list:
    """
    https://api.koios.rest/#get-/treasury_withdrawals
    List of all withdrawals from treasury against stake accounts
    :returns: The list of withdrawals from treasury against stake accounts
    """
    url = API_BASE_URL + "/treasury_withdrawals"
    parameters = {}
    withdrawals = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        withdrawals += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return withdrawals
