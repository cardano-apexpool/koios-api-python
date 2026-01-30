"""Ogmios section functions"""
from typing import Any, Optional

from .__config__ import API_BASE_URL
from .library import koios_post_request


def get_ogmios(
    jsonrpc: str, method: str, params: Optional[dict[str, Any]] = None
) -> list[dict[str, Any]]:
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
    parameters: dict[str, Any] = {"jsonrpc": jsonrpc, "method": method}
    for param, value in params.items():
        parameters[param] = value
    return koios_post_request(url, {}, parameters)
