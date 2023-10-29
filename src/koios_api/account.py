import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_account_list(offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/account_list
    Get a list of all stake addresses that have at least 1 transaction
    :param offset: (optional) The offset to start from
    :param limit: (optional) The maximum number of accounts to return
    :returns: The list of account (stake address) IDs
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
                response = requests.get(url, headers=headers, params=parameters)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    print(f"status code: {response.status_code}, retrying...")
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print(f"offset: {offset}, retrying...")
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
    :returns: The list of account information
    """
    url = API_BASE_URL + '/account_info'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
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


def get_account_info_cached(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/account_info_cached
    Get the cached account information for given stake addresses
    (effective for performance query against registered accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account information
    """
    url = API_BASE_URL + '/account_info_cached'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
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


def get_account_utxos(addr: [str, list], extended: bool = False, offset: int = 0, limit: int = 0) -> list:
    """
    https://api.koios.rest/#get-/account_utxos
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :param offset: (optional) The offset to start from
    :param limit: (optional) The maximum number of UTxOs to return
    :return: The list of all UTxOs for a given stake address (account)
    """
    url = API_BASE_URL + '/account_utxos'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
    parameters['_extended'] = str(extended).lower()
    utxos = []
    while True:
        if offset > 0:
            parameters['offset'] = offset
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
                print(f"offset: {offset}, retrying...")
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


def get_account_txs(addr: str, block_height: int = 0) -> list:
    """
    https://api.koios.rest/#get-/account_txs
    Get a list of all Txs for a given stake address (account)
    :param addr: Stake address
    :param block_height: (optional) Return only the transactions after this block height
    :returns: The list of transactions associated with stake address (account)
    """
    url = API_BASE_URL + '/account_txs'
    parameters = {'_stake_address': addr}
    if block_height > 0:
        parameters['_after_block_height'] = block_height
    txs = []
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
        txs += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return txs


def get_account_rewards(addr: [str, list], epoch: int = 0) -> list:
    """
    https://api.koios.rest/#post-/account_rewards
    Get the full rewards history (including MIR) for given stake addresses (accounts)
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param epoch: (optional) Epoch, default: current epoch
    :returns: The list of reward history information
    """
    url = API_BASE_URL + '/account_rewards'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
    if isinstance(epoch, int) and epoch > 0:
        parameters['_epoch_no'] = epoch
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


def get_account_updates(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/account_updates
    Get the account updates (registration, deregistration, delegation and withdrawals) for given stake addresses
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of account updates information
    """
    url = API_BASE_URL + '/account_updates'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
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


def get_account_addresses(addr: [str, list], first_only: bool = False, empty: bool = True) -> list:
    """
    https://api.koios.rest/#post-/account_addresses
    Get all addresses associated with given staking accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :param first_only: Return only the first address if True
    :param empty: Return also addresses with 0 balance if True
    :returns: The list of payment addresses
    """
    url = API_BASE_URL + '/account_addresses'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
    parameters['_first_only'] = str(first_only).lower()
    parameters['_empty'] = str(empty).lower()
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


def get_account_assets(addr: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/account_assets
    Get the native asset balance of given accounts
    :param addr: Stake address(es), as a string (for one address) or a list (for multiple addresses)
    :returns: The list of assets owned by account
    """
    url = API_BASE_URL + '/account_assets'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    qs_parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
    assets = []
    offset = 0
    while True:
        if offset > 0:
            qs_parameters['offset'] = offset
        while True:
            try:
                response = requests.post(url, headers=headers, params=qs_parameters, data=json.dumps(parameters))
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    print(f"status code: {response.status_code}, retrying...")
            except Exception as e:
                print(f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {e}")
                sleep(SLEEP_TIME)
                print(f"offset: {offset}, retrying...")
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
    :param epoch: (optional) Epoch to fetch information for, default: all epochs
    :returns: The list of active stake values per epoch
    """
    url = API_BASE_URL + '/account_history'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    parameters = {}
    if isinstance(addr, list):
        parameters['_stake_addresses'] = addr
    else:
        parameters['_stake_addresses'] = [addr]
    if epoch:
        parameters['_epoch_no'] = epoch
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
