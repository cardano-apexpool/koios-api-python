"""Ogmios section functions"""
import inspect
import json
from time import sleep

import requests

from .__config__ import *


def get_ogmios_evaluate_transaction(transaction: str) -> str:
    """
    https://api.koios.rest/#post-/ogmios/-EvaluateTransaction
    Evaluate execution units of scripts in a well-formed transaction.
    Please refer to Ogmios documentation here for complete spec
    :param transaction: CBOR-serialized signed transaction (base16)
    :returns resp: Evaluate response
    """
    url = API_BASE_URL + "/ogmios/?EvaluateTransaction"
    headers = {"Accept": "application/json", "Content-Type": "application/cbor"}
    if KOIOS_API_TOKEN:
        headers["Api-Token"] = "Bearer " + KOIOS_API_TOKEN
    while True:
        try:
            response = requests.post(
                url, headers=headers, data=transaction, timeout=REQUEST_TIMEOUT
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
