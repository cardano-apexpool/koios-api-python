import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_account_list(offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/account_list
    Get a list of all stake addresses that have at least 1 transaction
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of accounts to return (optional)
    :returns: The list of accounts maps
    """
    url = API_BASE_URL + '/account_list'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    account_list = []
    while True:
        if offset > 0:
            parameters['offset'] = offset
        while True:
            try:
                resp = json.loads(requests.get(url, headers=headers, params=parameters).text)
                break
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print('offset: %s, retrying...' % offset)
        account_list += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(account_list):
                account_list = account_list[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(account_list):
            account_list = account_list[0:limit]
            break
    return account_list


def get_account_info(addr: [str, list]) -> list:
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
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_utxos(addr: str, offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/account_utxos
    :param addr: Cardano staking address (reward account) in bech32 format
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of UTxOs to return (optional)
    :return: The list of all UTxOs for a given stake address (account)
    """
    url = API_BASE_URL + '/account_utxos'
    parameters = {'_stake_address': addr}
    utxos = []
    while True:
        if offset > 0:
            parameters['offset'] = offset
        while True:
            try:
                resp = json.loads(requests.get(url, params=parameters).text)
                break
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print('retrying...')
        utxos += resp
        if len(resp) < API_RESP_COUNT:
            if 0 < limit <= len(utxos):
                utxos = utxos[0:limit]
            break
        else:
            offset += len(resp)
        if 0 < limit <= len(utxos):
            utxos = utxos[0:limit]
            break
    return utxos


def get_account_info_cached(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/account_info_cached
    Get the cached account information for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account information maps
    """
    url = API_BASE_URL + '/account_info_cached'
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
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_rewards(addr: [str, list], epoch: int = 0) -> list:
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
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_updates(addr: [str, list]) -> list:
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
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_addresses(addr: [str, list]) -> list:
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
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp


def get_account_assets(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/account_assets
    Get the native asset balance of given accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account assets maps by account (stake address)
    """
    url = API_BASE_URL + '/account_assets'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    assets = []
    offset = 0
    while True:
        if offset > 0:
            parameters['offset'] = offset
        while True:
            try:
                resp = json.loads(requests.post(url, headers=headers, params=parameters,
                                                data=json.dumps(stake_addresses)).text)
                break
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print('retrying...')
        assets += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return assets


def get_account_history(addr: [str, list], epoch: int = 0) -> list:
    """
    https://api.koios.rest/#post-/account_history
    Get the staking history of given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param epoch: Epoch (optional) to fetch information for, default: all epochs
    :returns: The list of staking history maps by account (stake address)
    """
    url = API_BASE_URL + '/account_history'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    stake_addresses = {}
    if isinstance(addr, list):
        stake_addresses['_stake_addresses'] = addr
    else:
        stake_addresses['_stake_addresses'] = [addr]
    if epoch:
        stake_addresses['_epoch_no'] = epoch
    while True:
        try:
            resp = json.loads(requests.post(url, headers=headers, data=json.dumps(stake_addresses)).text)
            break
        except Exception as e:
            print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
            sleep(SLEEP_TIME)
            print('retrying...')
    return resp
