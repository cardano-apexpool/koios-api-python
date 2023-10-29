import json
import requests
import inspect
from time import sleep
from .__config__ import *


def get_ogmios_evaluate_transaction(tx: str) -> str:
    """
    https://api.koios.rest/#post-/ogmios/-EvaluateTransaction
    Evaluate execution units of scripts in a well-formed transaction.
    Please refer to Ogmios documentation here for complete spec
    :param tx: CBOR-serialized signed transaction (base16)
    :returns resp: Evaluate response
    """
    url = API_BASE_URL + '/ogmios/?EvaluateTransaction'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/cbor'}
    while True:
        try:
            response = requests.post(url, headers=headers, data=tx)
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
