"""Block section functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


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
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
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
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    while True:
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(parameters),
                timeout=REQUEST_TIMEOUT,
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
    return resp


def get_block_txs(block: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/block_txs
    Get a list of all transactions included in provided blocks
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of transactions hashes
    """
    url = API_BASE_URL + "/block_txs"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(block, list):
        parameters["_block_hashes"] = block
    else:
        parameters["_block_hashes"] = [block]
    while True:
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(parameters),
                timeout=REQUEST_TIMEOUT,
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
    return resp
