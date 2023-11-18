"""Network section functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def get_tip() -> list:
    """
    https://api.koios.rest/#get-/tip
    Get the tip info about the latest block seen by chain
    :returns: The list of block summary (limit+paginated)
    """
    url = API_BASE_URL + "/tip"
    while True:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
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


def get_genesis() -> list:
    """
    https://api.koios.rest/#get-/genesis
    Get the Genesis parameters used to start specific era on chain
    :returns: The list of genesis parameters used to start each era on chain
    """
    url = API_BASE_URL + "/genesis"
    while True:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
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


def get_totals(epoch: int = 0) -> list:
    """
    https://api.koios.rest/#get-/totals
    Get the circulating utxo, treasury, rewards, supply and reserves in lovelace
    for specified epoch, all epochs if empty
    :param epoch: (Optional) The epoch
    :returns: The list of supply/reserves/utxo/fees/treasury stats
    """
    url = API_BASE_URL + "/totals"
    parameters = {}
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


def get_param_updates() -> list:
    """
    https://api.koios.rest/#get-/param_updates
    Get all parameter update proposals submitted to the chain starting Shelley era
    :returns: The list of unique param update proposals submitted on chain
    """
    url = API_BASE_URL + "/param_updates"
    while True:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
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


def get_reserve_withdrawals() -> list:
    """
    https://api.koios.rest/#get-/reserve_withdrawals
    List of all withdrawals from reserves against stake accounts
    :returns: The list of withdrawals from reserves against stake accounts
    """
    url = API_BASE_URL + "/reserve_withdrawals"
    while True:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
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


def get_treasury_withdrawals() -> list:
    """
    https://api.koios.rest/#get-/treasury_withdrawals
    List of all withdrawals from treasury against stake accounts
    :returns: The list of withdrawals from treasury against stake accounts
    """
    url = API_BASE_URL + "/treasury_withdrawals"
    while True:
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
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
