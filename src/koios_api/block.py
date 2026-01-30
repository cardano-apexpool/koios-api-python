"""Block section functions"""
from typing import Any, Union

from .__config__ import API_BASE_URL
from .library import koios_post_request, paginated_get


def get_blocks(limit: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/blocks
    Get summarised details about all blocks (paginated - latest first)
    :param limit: the limit of the returned blocks number
    :returns: The list of block information (the newest first)
    """
    url = API_BASE_URL + "/blocks"
    parameters: dict[str, Any] = {}
    if isinstance(limit, int) and limit > 0:
        parameters["limit"] = limit
    return paginated_get(url, parameters, limit=limit)


def get_block_info(block: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/block_info
    Get detailed information about a specific block
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of detailed block information
    """
    url = API_BASE_URL + "/block_info"
    parameters: dict[str, Any] = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    return koios_post_request(url, {}, parameters)


def get_block_txs(block: Union[str, list[str]]) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#post-/block_txs
    Get a list of all transactions included in provided blocks
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of transactions hashes
    """
    url = API_BASE_URL + "/block_txs"
    parameters: dict[str, Any] = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    return koios_post_request(url, {}, parameters)
