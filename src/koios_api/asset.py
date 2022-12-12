import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_asset_list(policy=''):
    """
    https://api.koios.rest/#get-/asset_list
    Get the list of all native assets (paginated)
    :param policy: Asset Policy (optional), default: all policies
    :returns: The list of assets maps by policy
    """
    url = API_BASE_URL + '/asset_list'
    assets_names_hex = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        if isinstance(policy, str) and policy != '':
            url += '&policy_id=eq.%s' % policy
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('retrying...')
        assets_names_hex += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return assets_names_hex


def get_asset_address_list(policy, name=''):
    """
    https://api.koios.rest/#get-/asset_address_list
    Get the list of all addresses holding a given asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the wallets holding the asset and the amount of assets per wallet
    """
    url = API_BASE_URL + '/asset_address_list?_asset_policy=%s' % policy
    if isinstance(name, str) and name != '':
        url += '&_asset_name=%s' % name
    wallets = []
    offset = 0
    while True:
        paginated_url = url + '&offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('offset: %d, retrying...' % offset)
        wallets += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return wallets


def get_asset_info(policy, name=''):
    """
    https://api.koios.rest/#get-/asset_info
    Get the information of an asset including first minting & token registry metadata
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the wallets holding the asset and the amount of assets per wallet
    """
    url = API_BASE_URL + '/asset_info?_asset_policy=%s' % policy
    if isinstance(name, str) and name != '':
        url += '&_asset_name=%s' % name
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_asset_history(policy, name=''):
    """
    https://api.koios.rest/#get-/asset_history
    Get the mint/burn history of an asset
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the mint/burn history of an asset
    """
    url = API_BASE_URL + '/asset_history?_asset_policy=%s' % policy
    if isinstance(name, str) and name != '':
        url += '&_asset_name=%s' % name
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_asset_policy_info(policy):
    """
    https://api.koios.rest/#get-/asset_policy_info
    Get the information for all assets under the same policy
    :param policy: Asset Policy
    :returns: List of maps with the policy assets
    """
    url = API_BASE_URL + '/asset_policy_info?_asset_policy=%s' % policy
    assets = []
    offset = 0
    while True:
        paginated_url = url + '&offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('retrying...')
        assets += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return assets


def get_asset_summary(policy, name=''):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets
    include only wallets with asset balance)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :returns: List of maps with the mint/burn history of an asset
    """
    url = API_BASE_URL + '/asset_summary?_asset_policy=%s' % policy
    if isinstance(name, str) and name != '':
        url += '&_asset_name=%s' % name
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_asset_txs(policy, name='', block=0, history=False):
    """
    Get the list of all asset transaction hashes (the newest first)
    :param policy: Asset Policy
    :param name: Asset Name in hexadecimal format (optional), default: all policy assets
    :param block: (optional) Return only the transactions after this block
    :param history: (optional) Include all historical transactions, setting to false includes only the non-empty ones
    :returns: List of maps with the mint/burn history of an asset
    """
    url = API_BASE_URL + '/asset_txs?_asset_policy=%s' % policy
    if isinstance(name, str) and name != '':
        url += '&_asset_name=%s' % name
    if isinstance(block, int) and block > 0:
        url += '&_after_block_height=%d' % block
    if isinstance(history, bool):
        url += '&_history=%s' % str(history).lower()
    while True:
        try:
            resp = json.loads(requests.get(url).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
