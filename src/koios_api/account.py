import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_account_list():
    """
    https://api.koios.rest/#get-/account_list
    Get a list of all accounts
    :returns: The list of accounts maps
    """
    url = API_BASE_URL + '/account_list'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    account_list = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.get(paginated_url, headers=headers).text)
                break
            except Exception as e:
                print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
                sleep(SLEEP_TIME)
                print('offset: %s, retrying...' % offset)
        account_list += resp
        if len(resp) < 1000:
            break
        else:
            offset += len(resp)
    return account_list


def get_account_info(addr):
    """
    https://api.koios.rest/#post-/account_info
    Get the account information for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account information maps
    """
    url = API_BASE_URL + '/account_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_rewards(addr, epoch=0):
    """
    https://api.koios.rest/#post-/account_rewards
    Get the full rewards history (including MIR) for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param epoch: Epoch (optional), default: current epoch
    :returns: The list of rewards maps by account (stake address)
    """
    url = API_BASE_URL + '/account_rewards'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    if isinstance(epoch, int) and epoch > 0:
        stake_addresses['_epoch_no'] = epoch
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_updates(addr):
    """
    https://api.koios.rest/#post-/account_updates
    Get the account updates (registration, deregistration, delegation and withdrawals)
    for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account updates maps by account (stake address)
    """
    url = API_BASE_URL + '/account_updates'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_addresses(addr):
    """
    https://api.koios.rest/#post-/account_addresses
    Get all addresses associated with given staking accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of addresses maps by account (stake address)
    """
    url = API_BASE_URL + '/account_addresses'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_assets(addr):
    """
    https://api.koios.rest/#post-/account_assets
    Get the native asset balance of given accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account assets maps by account (stake address)
    """
    url = API_BASE_URL + '/account_assets'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    assets = []
    offset = 0
    while True:
        paginated_url = url + '?offset=%d' % offset
        while True:
            try:
                resp = json.loads(requests.post(paginated_url, headers=headers, data=json.dumps(stake_addresses)).text)
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


def get_account_history(addr):
    """
    https://api.koios.rest/#post-/account_history
    Get the staking history of given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of staking history maps by account (stake address)
    """
    url = API_BASE_URL + '/account_history'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print('Exception in %s: %s' % (inspect.getframeinfo(inspect.currentframe()).function, e))
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
