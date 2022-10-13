import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_epoch_info(epoch=0):
    """
    https://api.koios.rest/#post-/tx_info
    Get the epoch information, all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :returns: The list of epoch info maps
    """
    url = API_BASE_URL + '/epoch_info'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_epoch_params(epoch=0):
    """
    https://api.koios.rest/#get-/epoch_params
    Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :returns: The list of epoch protocol parameters maps
    """
    url = API_BASE_URL + '/epoch_params'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_epoch_block_protocols(epoch=0):
    """
    https://api.koios.rest/#get-/epoch_block_protocols
    Get the information about block protocol distribution in epoch
    :param epoch: (optional) Epoch
    :returns: The list of epoch protocol distribution maps
    """
    url = API_BASE_URL + '/epoch_block_protocols'
    if isinstance(epoch, int) and epoch > 0:
        url += '?_epoch_no=%d' % epoch
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
