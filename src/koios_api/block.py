"""Block section functions"""
from .library import *


def get_blocks(limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/blocks
    Get summarised details about all blocks (paginated - latest first)
    :param limit: the limit of the returned blocks number
    :returns: The list of block information (the newest first)
    """
    url = API_BASE_URL + "/blocks"
    parameters = {}
    blocks = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        if isinstance(limit, int) and limit > 0:
            parameters["limit"] = limit
        resp = koios_get_request(url, parameters)
        blocks += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
        if isinstance(limit, int) and len(blocks) > limit:
            break
    if isinstance(limit, int) and limit > 0:
        blocks = blocks[0:limit]
    return blocks


def get_block_info(block: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/block_info
    Get detailed information about a specific block
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of detailed block information
    """
    url = API_BASE_URL + "/block_info"
    parameters = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    return koios_post_request(url, parameters)


def get_block_txs(block: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/block_txs
    Get a list of all transactions included in provided blocks
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of transactions hashes
    """
    url = API_BASE_URL + "/block_txs"
    parameters = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    return koios_post_request(url, parameters)
