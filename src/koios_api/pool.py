"""Pool section functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def get_pool_list() -> list:
    """
    https://api.koios.rest/#get-/pool_list
    List of brief info for all pools
    :returns: The list of pool IDs and tickers
    """
    url = API_BASE_URL + "/pool_list"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    pools_list = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(
                    url, headers=headers, params=parameters, timeout=REQUEST_TIMEOUT
                )
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        pools_list += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return pools_list


def get_pool_info(pool_id: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/pool_info
    Current pool statuses and details for a specified list of pool ids
    :param pool_id: Stake pool bech32 ID as string (for one stake pool)
    or list of stake pool bech32 IDs (for multiple stake pools)
    :returns: The list of pool information
    """
    url = API_BASE_URL + "/pool_info"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    while True:
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(parameters),
                timeout=REQUEST_TIMEOUT,
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                logger.warning(f"status code: {response.status_code}, retrying...")
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            sleep(SLEEP_TIME)
            logger.warning("retrying...")
    return resp


def get_pool_stake_snapshot(pool_id: str) -> list:
    """
    https://api.koios.rest/#get-/pool_stake_snapshot
    Returns Mark, Set and Go stake snapshots for the selected pool, useful for leaderlog calculation
    :param pool_id: stake pool bech32 id
    :returns: The list of pool stake information for 3 snapshots
    """
    url = API_BASE_URL + "/pool_stake_snapshot"
    parameters = {"_pool_bech32": pool_id}
    while True:
        try:
            response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                logger.warning(f"status code: {response.status_code}, retrying...")
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            sleep(SLEEP_TIME)
            logger.warning("retrying...")
    return resp


def get_pool_delegators(pool_id: str) -> list:
    """
    https://api.koios.rest/#get-/pool_delegators
    Return information about live delegators for a given pool
    :param pool_id: stake pool bech32 id
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators"
    parameters = {"_pool_bech32": pool_id}
    delegators = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        delegators += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return delegators


def get_pool_delegators_history(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_delegators_history
    Return information about active delegators (incl. history) for a given pool and epoch number
    (all epochs if not specified)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool delegator information
    """
    url = API_BASE_URL + "/pool_delegators_history"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    delegators = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        delegators += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return delegators


def get_pool_blocks(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_blocks
    Return information about blocks minted by a given pool for all epochs (or _epoch_no if provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of blocks created by pool
    """
    url = API_BASE_URL + "/pool_blocks"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    blocks = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        blocks += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return blocks


def get_pool_history(pool_id: str, epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_history
    Return information about pool stake, block and reward history in a given epoch _epoch_no
    (or all epochs that pool existed for, in descending order if no _epoch_no was provided)
    :param pool_id: stake pool bech32 id
    :param epoch: (optional) epoch
    :returns: The list of pool history information
    """
    url = API_BASE_URL + "/pool_history"
    parameters = {"_pool_bech32": pool_id}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    while True:
        try:
            response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                logger.warning(f"status code: {response.status_code}, retrying...")
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            sleep(SLEEP_TIME)
            logger.warning("retrying...")
    return resp


def get_pool_updates(pool_id: str = "") -> list:
    """
    https://api.koios.rest/#get-/pool_updates
    Return all pool updates for all pools or only updates for specific pool if specified
    :param pool_id: stake pool bech32 id
    :returns: The list of historical pool updates
    """
    url = API_BASE_URL + "/pool_updates"
    parameters = {}
    pool_updates = []
    offset = 0
    if pool_id:
        parameters["_pool_bech32"] = pool_id
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        pool_updates += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return pool_updates


def get_pool_registrations(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_registrations
    Return all pool registrations initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool registrations
    """
    url = API_BASE_URL + "/pool_registrations"
    parameters = {}
    registrations = []
    offset = 0
    if epoch:
        parameters["_epoch_no"] = epoch
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        registrations += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return registrations


def get_pool_retirements(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/pool_retirements
    Return all pool retirements initiated in the requested epoch
    :param epoch: The epoch
    :returns: The list of pool retirements
    """
    url = API_BASE_URL + "/pool_retirements"
    parameters = {}
    retirements = []
    offset = 0
    if epoch:
        parameters["_epoch_no"] = epoch
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        retirements += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return retirements


def get_pool_relays() -> list:
    """
    https://api.koios.rest/#get-/pool_relays
    A list of registered relays for all currently registered/retiring (not retired) pools
    :returns: The list of pool relay information
    """
    url = API_BASE_URL + "/pool_relays"
    parameters = {}
    relays = []
    offset = 0
    while True:
        if offset > 0:
            parameters["offset"] = offset
        while True:
            try:
                response = requests.get(url, params=parameters, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    resp = json.loads(response.text)
                    break
                else:
                    logger.warning(f"status code: {response.status_code}, retrying...")
            except Exception as exc:
                logger.exception(
                    f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
                )
                sleep(SLEEP_TIME)
                logger.warning(f"offset: {offset}, retrying...")
        relays += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return relays


def get_pool_metadata(pool_id: str) -> list:
    """
    https://api.koios.rest/#post-/pool_metadata
    A list of registered relays for all currently registered/retiring (not retired) pools
    :param pool_id: stake pool bech32 id
    :returns: The list of pool metadata maps
    """
    url = API_BASE_URL + "/pool_metadata"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(pool_id, list):
        parameters["_pool_bech32_ids"] = pool_id
    else:
        parameters["_pool_bech32_ids"] = [pool_id]
    while True:
        try:
            response = requests.post(
                url,
                headers=headers,
                data=json.dumps(parameters),
                timeout=REQUEST_TIMEOUT,
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                logger.warning(f"status code: {response.status_code}, retrying...")
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            sleep(SLEEP_TIME)
            logger.warning("retrying...")
    return resp


def get_retiring_pools() -> list:
    """
    Get the retiring stake pools list
    :returns: The list of retiring pools maps
    """
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    url = API_BASE_URL + "/pool_list"
    parameters = {"pool_status": "eq.retiring"}
    while True:
        try:
            response = requests.get(
                url, headers=headers, params=parameters, timeout=REQUEST_TIMEOUT
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                logger.warning(f"status code: {response.status_code}, retrying...")
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            sleep(SLEEP_TIME)
            logger.warning("retrying...")
    return resp
