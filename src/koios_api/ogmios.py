"""Ogmios section functions"""
from .library import *


def get_ogmios(jsonrpc: str, method: str, params=None) -> list:
    """
    https://api.koios.rest/#post-/ogmios
    Multiple ogmios queries are supported,
    you can read about them here: https://api.koios.rest/#tag--Ogmios).
    :param jsonrpc: Identifier for JSON-RPC 2.0 standard
    :param method: The Ogmios method to be called
        Allowed:
            queryNetwork/blockHeight
            queryNetwork/genesisConfiguration
            queryNetwork/startTime
            queryNetwork/tip
            queryLedgerState/epoch
            queryLedgerState/eraStart
            queryLedgerState/eraSummaries
            queryLedgerState/liveStakeDistribution
            queryLedgerState/protocolParameters
            queryLedgerState/proposedProtocolParameters
            queryLedgerState/stakePools
            submitTransaction
            evaluateTransaction
    :param params: Any parameters relevant to the specific method to be called
    :returns resp: The response for the query
    """
    if params is None:
        params = {}
    url = API_BASE_URL + "/ogmios"
    parameters = {"jsonrpc": jsonrpc, "method": method}
    for param, value in params.items():
        parameters[param] = value
    resp = koios_post_request(url, parameters)
    return resp
