import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_tx_info(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_info
    Get detailed information about transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of detailed information about transaction(s)
    """
    url = API_BASE_URL + '/tx_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(txs, list):
        parameters['_tx_hashes'] = txs
    else:
        parameters['_tx_hashes'] = [txs]
    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(parameters))
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                print(f"status code: {response.status_code}, retrying...")
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_utxo_info(utxos: [str, list], extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/utxo_info
    Get UTxO set for requested UTxO references
    :param utxos: utxos as a string (for one utxo) or list (for multiple utxos)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list of UTXO details
    """
    url = API_BASE_URL + '/utxo_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(txs, list):
        parameters['_utxo_refs'] = utxos
    else:
        parameters['_utxo_refs'] = [utxos]
    if isinstance(extended, bool):
        parameters['_extended'] = str(extended).lower()
    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(parameters))
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                print(f"status code: {response.status_code}, retrying...")
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_metadata(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_metadata
    Get metadata information (if any) for given transaction(s)
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of metadata information present in each of the transactions queried
    """
    url = API_BASE_URL + '/tx_metadata'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(txs, list):
        parameters['_tx_hashes'] = txs
    else:
        parameters['_tx_hashes'] = [txs]
    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(parameters))
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                print(f"status code: {response.status_code}, retrying...")
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_metalabels() -> list:
    """
    https://api.koios.rest/#get-/tx_metalabels
    Get a list of all transaction metadata labels
    :returns: The list of known metadata labels
    """
    url = API_BASE_URL + '/tx_metalabels'
    parameters = {}
    metalabels_list = []
    offset = 0
    while True:
        if offset > 0:
            parameters['offset'] = offset
        while True:
            try:
                response = requests.get(url, params=parameters)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    print(f"status code: {response.status_code}, retrying...")
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print(f"offset: {offset}, retrying...")
        metalabels_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return metalabels_list


def submit_tx(tx: str) -> str:
    """
    https://api.koios.rest/#post-/submittx
    Submit an already serialized transaction to the network
    :param tx: transaction in cbor format
    :returns: transaction hash
    """
    url = API_BASE_URL + '/submittx'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/cbor'}
    while True:
        try:
            response = requests.post(url, headers=headers, data=tx)
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                print(f"status code: {response.status_code}, retrying...")
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_tx_status(txs: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/tx_status
    Get the number of block confirmations for a given transaction hash list
    :param txs: transaction hash as a string (for one transaction) or list (for multiple transactions)
    :returns: The list of transaction confirmation counts
    """
    url = API_BASE_URL + '/tx_status'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(txs, list):
        parameters['_tx_hashes'] = txs
    else:
        parameters['_tx_hashes'] = [txs]
    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(parameters))
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                print(f"status code: {response.status_code}, retrying...")
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
