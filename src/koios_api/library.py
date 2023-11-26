"""Library functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def get_error_message(response: requests.Response) -> str:
    """
    Get the error message from the response
    :param response: The response to the request
    :return: The error message
    """
    try:
        error_message = json.loads(response.text)["message"]
    except json.decoder.JSONDecodeError:
        error_message = response.text
        if not error_message:
            error_message = response.reason
        if "deny-reason" in response.headers:
            error_message += " " + response.headers["deny-reason"]
    return error_message


def koios_get_request(url: str, parameters: dict) -> list:
    """
    Create a GET request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param parameters: Parameters to include as data in the GET request
    :return: A list with the body of the response
    """
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if KOIOS_API_TOKEN:
        headers["Authorization"] = "Bearer " + KOIOS_API_TOKEN

    ordered_requests = [
        "blocks",
        "account_txs",
        "asset_txs",
        "pool_blocks",
        "pool_registrations",
        "pool_retirements",
        "script_utxos",
    ]
    if any(req in url for req in ordered_requests):
        parameters["order"] = "block_height.asc"
    while True:
        try:
            response = requests.get(
                url, headers=headers, params=parameters, timeout=REQUEST_TIMEOUT
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                error_message = get_error_message(response)
                logger.warning(
                    f"status code: {response.status_code} ({error_message}), retrying..."
                )
                logger.error(inspect.stack()[-1])
                sleep(SLEEP_TIME)
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            if "offset" in parameters:
                offset = {parameters["offset"]}
            else:
                offset = 0
            logger.warning(f"offset: {offset}, retrying in {SLEEP_TIME} second(s)...")
            sleep(SLEEP_TIME)
    return resp


def koios_post_request(url: str, parameters: dict, headers=None) -> list:
    """
    Create a POST request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param parameters: Parameters to include as data in the POST request
    :param headers: Headers to include in the request
    :return: A list with the body of the response
    """
    if headers is None:
        headers = {}
    if not headers:
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if KOIOS_API_TOKEN:
        headers["Authorization"] = "Bearer " + KOIOS_API_TOKEN
    ordered_requests = [
        "utxo_info",
        "tx_info",
        "account_utxos",
        "address_utxos",
        "credential_utxos",
        "address_txs",
        "credential_txs",
        "asset_utxos",
    ]
    if any(req in url for req in ordered_requests):
        params = {"order": "block_height.asc"}
    else:
        params = {}
    while True:
        try:
            response = requests.post(
                url,
                headers=headers,
                params=params,
                data=json.dumps(parameters),
                timeout=REQUEST_TIMEOUT,
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                break
            else:
                error_message = get_error_message(response)
                logger.warning(
                    f"status code: {response.status_code} ({error_message}), retrying..."
                )
                logger.error(inspect.stack()[-1])
                sleep(SLEEP_TIME)
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            if "offset" in parameters:
                offset = {parameters["offset"]}
            else:
                offset = 0
            logger.warning(f"offset: {offset}, retrying in {SLEEP_TIME} second(s)...")
            sleep(SLEEP_TIME)
    return resp
