"""Library functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def koios_get_request(url: str, parameters: dict) -> list:
    """
    Create a GET request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param parameters: Parameters to include as data in the GET request
    :return: A list with the body of the response
    """
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if KOIOS_API_TOKEN:
        headers["Api-Token"] = "Bearer " + KOIOS_API_TOKEN
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
            if "offset" in parameters:
                offset = {parameters["offset"]}
            else:
                offset = 0
            logger.warning(f"offset: {offset}, retrying in {SLEEP_TIME} second(s)...")
            sleep(SLEEP_TIME)
    return resp


def koios_post_request(url: str, parameters: dict, headers: dict = {}) -> list:
    """
    Create a POST request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param parameters: Parameters to include as data in the POST request
    :param headers: Headers to include in the request
    :return: A list with the body of the response
    """
    if not headers:
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
    if KOIOS_API_TOKEN:
        headers["Api-Token"] = "Bearer " + KOIOS_API_TOKEN
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
            if "offset" in parameters:
                offset = {parameters["offset"]}
            else:
                offset = 0
            logger.warning(f"offset: {offset}, retrying in {SLEEP_TIME} second(s)...")
            sleep(SLEEP_TIME)
    return resp
