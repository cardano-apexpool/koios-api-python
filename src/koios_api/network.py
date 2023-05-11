import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_tip() -> list:
    """
    https://api.koios.rest/#get-/tip
    Get the tip info about the latest block seen by chain
    :returns: A list with the tip as a map
    """
    url = API_BASE_URL + '/tip'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_genesis() -> list:
    """
    https://api.koios.rest/#get-/genesis
    Get the Genesis parameters used to start specific era on chain
    :returns: A list with the genesis parameters map
    """
    url = API_BASE_URL + '/genesis'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_totals(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/totals
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace
    for specified epoch, all epochs if empty
    :param epoch: (Optional) The epoch
    :returns: The list of tokenomic stats maps
    """
    url = API_BASE_URL + '/totals'
    parameters = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters['_epoch_no'] = epoch
    while True:
        try:
            resp = json.loads(requests.get(url, params=parameters).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_param_updates() -> list:
    """
    https://api.koios.rest/#get-/param_updates
    Get all parameter update proposals submitted to the chain starting Shelley era
    :returns: A list with the parameters updates
    """
    url = API_BASE_URL + '/param_updates'
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
