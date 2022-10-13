import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_tx_info(txs):
    """
    https://api.koios.rest/#post-/tx_info
    Get detailed information about transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transactions details maps
    """
    url = API_BASE_URL + '/tx_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {}
    if isinstance(txs, list):
        tx_hashes['_tx_hashes'] = txs
    else:
        tx_hashes['_tx_hashes'] = [txs]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_utxos(txs):
    """
    https://api.koios.rest/#post-/tx_utxos
    Get UTxO set (inputs/outputs) of transactions.
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transactions UTxOs maps
    """
    url = API_BASE_URL + '/tx_utxos'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {}
    if isinstance(txs, list):
        tx_hashes['_tx_hashes'] = txs
    else:
        tx_hashes['_tx_hashes'] = [txs]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_metadata(txs):
    """
    https://api.koios.rest/#post-/tx_metadata
    Get metadata information (if any) for given transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transactions metadata maps
    """
    url = API_BASE_URL + '/tx_metadata'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {}
    if isinstance(txs, list):
        tx_hashes['_tx_hashes'] = txs
    else:
        tx_hashes['_tx_hashes'] = [txs]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_metalabels():
    """
    https://api.koios.rest/#get-/tx_metalabels
    Get a list of all transaction metadata labels
    :returns: The list of transaction metadata labels maps
    """
    url = API_BASE_URL + '/tx_metalabels'
    metalabels_list = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('Offset %d, retrying...' % offset)
        metalabels_list += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return metalabels_list


def submit_tx(tx):
    """
    https://api.koios.rest/#post-/submittx
    Submit an already serialized transaction to the network.
    :param tx: transaction in cbor format
    :returns: transaction hash
    """
    url = API_BASE_URL + '/submittx'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/cbor'}
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=tx).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_status(txs):
    """
    https://api.koios.rest/#post-/tx_status
    Get the number of block confirmations for a given transaction hash list
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transactions block confirmations maps
    """
    url = API_BASE_URL + '/tx_status'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    tx_hashes = {}
    if isinstance(txs, list):
        tx_hashes['_tx_hashes'] = txs
    else:
        tx_hashes['_tx_hashes'] = [txs]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(tx_hashes)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
