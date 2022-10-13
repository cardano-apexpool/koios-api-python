import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_native_script_list():
    """
    https://api.koios.rest/#get-/native_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all native scripts maps
    """
    url = API_BASE_URL + '/native_script_list'
    scripts_list = []
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
        scripts_list += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return scripts_list


def get_plutus_script_list():
    """
    https://api.koios.rest/#get-/plutus_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all plutus scripts maps
    """
    url = API_BASE_URL + '/plutus_script_list'
    scripts_list = []
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
        scripts_list += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return scripts_list


def get_script_redeemers(script):
    """
    https://api.koios.rest/#get-/script_redeemers
    List of all redeemers for a given script hash
    :param script: script hash
    :return resp: redeemers list as map
    """
    url = API_BASE_URL + '/script_redeemers?_script_hash=%s' % script
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
