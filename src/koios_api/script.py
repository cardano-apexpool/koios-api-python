import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_native_script_list() -> list:
    """
    https://api.koios.rest/#get-/native_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all native scripts maps
    """
    url = API_BASE_URL + '/native_script_list'
    parameters = {}
    scripts_list = []
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
        scripts_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return scripts_list


def get_plutus_script_list() -> list:
    """
    https://api.koios.rest/#get-/plutus_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all plutus scripts maps
    """
    url = API_BASE_URL + '/plutus_script_list'
    parameters = {}
    scripts_list = []
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
        scripts_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return scripts_list


def get_script_redeemers(script: str) -> list:
    """
    https://api.koios.rest/#get-/script_redeemers
    List of all redeemers for a given script hash
    :param script: script hash
    :returns resp: redeemers list as map
    """
    url = API_BASE_URL + '/script_redeemers'
    parameters = {'_script_hash':  script}
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
            print('retrying...')
    return resp


def get_datum_info(datum: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/datum_info
    List of datum information for given datum hashes
    :param datum: datum hash as string (for one datum hash) or list (for a list of datum hashes)
    :returns resp: datum information as list of maps
    """
    url = API_BASE_URL + '/datum_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    datum_hashes = {}
    if isinstance(datum, list):
        datum_hashes['_datum_hashes'] = datum
    else:
        datum_hashes['_datum_hashes'] = [datum]
    while True:
        try:
            response = requests.post(url, headers=headers, data=json.dumps(datum_hashes))
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
