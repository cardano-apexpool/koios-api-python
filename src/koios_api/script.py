"""Script section functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def get_script_info(script_hashes: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/script_info
    List of datum information for given datum hashes
    :param script_hashes: Script hash as string (for one script hash) or list (for a list of script hashes)
    :returns resp: The list of script information for given script hashes
    """
    url = API_BASE_URL + "/script_info"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(script_hashes, list):
        parameters["_script_hashes"] = script_hashes
    else:
        parameters["_script_hashes"] = [script_hashes]
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


def get_native_script_list() -> list:
    """
    https://api.koios.rest/#get-/native_script_list
    List of all existing native script hashes along with their creation transaction hashes
    :returns: The list of all native scripts maps
    """
    url = API_BASE_URL + "/native_script_list"
    parameters = {}
    scripts_list = []
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
    url = API_BASE_URL + "/plutus_script_list"
    parameters = {}
    scripts_list = []
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
    url = API_BASE_URL + "/script_redeemers"
    parameters = {"_script_hash": script}
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


def get_script_utxos(script_hash: str, extended: bool = False) -> list:
    """
    https://api.koios.rest/#post-/asset_utxos
    Get the UTXO information of a list of assets including
    :param script_hash: Script hash
    :param extended: (optional) Include certain optional fields are populated as a part of the call
    :returns: The list UTXOs for given asset list
    """
    url = API_BASE_URL + "/script_utxos"
    parameters = {
        "_script_hash": script_hash.split(".")[0],
        "_extended": str(extended).lower(),
    }
    utxos = []
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
        utxos += resp
        if len(resp) < API_RESP_COUNT:
            break
        else:
            offset += len(resp)
    return utxos


def get_datum_info(datum: [str, list]) -> list:
    """
    https://api.koios.rest/#post-/datum_info
    List of datum information for given datum hashes
    :param datum: datum hash as string (for one datum hash) or list (for a list of datum hashes)
    :returns resp: datum information as list of maps
    """
    url = API_BASE_URL + "/datum_info"
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    parameters = {}
    if isinstance(datum, list):
        parameters["_datum_hashes"] = datum
    else:
        parameters["_datum_hashes"] = [datum]
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
