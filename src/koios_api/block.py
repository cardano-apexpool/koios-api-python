import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_blocks(limit=0):
    """
    https://api.koios.rest/#get-/blocks
    Get summarised details about all blocks (paginated - latest first)
    :param limit: the limit of the returned blocks number
    :returns: The list of block maps (the newest first)
    """
    url = API_BASE_URL + '/blocks'
    blocks = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        if isinstance(limit, int) and limit > 0:
            paginated_url += '&limit=%d' % limit
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('retrying...')
        blocks += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
        if isinstance(limit, int) and len(blocks) > limit:
            break
    if isinstance(limit, int) and limit > 0:
        return blocks[0:limit]
    else:
        return blocks


def get_block_info(block):
    """
    Get detailed information about a specific block
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of block maps
    """
    url = API_BASE_URL + '/block_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    block_hashes = {}
    if isinstance(block, list):
        block_hashes['_block_hashes'] = block
    else:
        block_hashes['_block_hashes'] = [block]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(block_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_block_txs(block):
    """
    https://api.koios.rest/#post-/block_txs
    Get a list of all transactions included in provided blocks
    :param block: Block hash as string (for one block) or list of block hashes (for multiple blocks)
    :returns: The list of transaction maps by block
    """
    url = API_BASE_URL + '/block_txs'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    block_hashes = {}
    if isinstance(block, list):
        block_hashes['_block_hashes'] = block
    else:
        block_hashes['_block_hashes'] = [block]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(block_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
