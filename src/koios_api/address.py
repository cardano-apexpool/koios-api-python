import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_address_info(addr):
    """
    https://api.koios.rest/#post-/address_info
    Get address info - balance, associated stake address (if any) and UTxO set for given addresses
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :returns: The list of address information maps
    """
    url = API_BASE_URL + '/address_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    addresses = {}
    if isinstance(addr, list):
        addresses['_addresses'] = addr
    else:
        addresses['_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_address_txs(addr):
    """
    https://api.koios.rest/#post-/address_txs
    Get the transaction hash list of input address array, optionally filtering after specified block height (inclusive)
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :returns: The list of transactions maps
    """
    url = API_BASE_URL + '/address_txs'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    addresses = {}
    if isinstance(addr, list):
        addresses['_addresses'] = addr
    else:
        addresses['_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_address_assets(addr):
    """
    https://api.koios.rest/#post-/address_assets
    Get the list of all the assets (policy, name and quantity) for given addresses
    :param addr: Payment address(es) as string (for one address) or list (for multiple addresses)
    :returns: The list of assets maps by address
    """
    url = API_BASE_URL + '/address_assets'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    addresses = {}
    if isinstance(addr, list):
        addresses['_addresses'] = addr
    else:
        addresses['_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_credential_txs(cred):
    """
    https://api.koios.rest/#post-/credential_txs
    Get the transaction hash list of input payment credential array,
    optionally filtering after specified block height (inclusive)
    :param cred: Credential(s) as string (for one credential) or list (for multiple credentials)
    :returns: The list of address information maps
    """
    url = API_BASE_URL + '/credential_txs'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    credentials = {}
    if isinstance(cred, list):
        credentials['_payment_credentials'] = cred
    else:
        credentials['_payment_credentials'] = [cred]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(credentials)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
