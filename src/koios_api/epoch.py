import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_epoch_info(epoch: int = 0, include_next_epoch: bool = False) -> list:
    """
    https://api.koios.rest/#get-/epoch_info
    Get the epoch information, all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :param include_next_epoch: (optional) Include information about nearing but not yet started epoch,
    to get access to active stake snapshot information if available
    :returns: The list of epoch info maps
    """
    url = API_BASE_URL + '/epoch_info'
    parameters = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters['_epoch_no'] = epoch
    if isinstance(include_next_epoch, bool):
        parameters['_include_next_epoch'] = str(include_next_epoch).lower()
    while True:
        try:
            resp = json.loads(requests.get(url, params=parameters).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_epoch_params(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/epoch_params
    Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :returns: The list of epoch protocol parameters maps
    """
    url = API_BASE_URL + '/epoch_params'
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


def get_epoch_block_protocols(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/epoch_block_protocols
    Get the information about block protocol distribution in epoch
    :param epoch: (optional) Epoch
    :returns: The list of epoch protocol distribution maps
    """
    url = API_BASE_URL + '/epoch_block_protocols'
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
