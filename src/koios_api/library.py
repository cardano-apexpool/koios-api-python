"""Library functions"""
import inspect
import json
from time import sleep
from typing import Any, Optional

import requests

from .__config__ import (
    API_RESP_COUNT,
    KOIOS_API_TOKEN,
    REQUEST_TIMEOUT,
    SLEEP_TIME,
    logger,
)

# Maximum number of retries for failed requests
MAX_RETRIES = 10


class MaxRetriesExceeded(Exception):
    """Exception raised when maximum retries are exceeded."""

    pass


def get_error_message(response: requests.Response) -> str:
    """
    Get the error message from the response
    :param response: The response to the request
    :return: The error message
    """
    try:
        error_message = json.loads(response.text).get("message", "")
        if not error_message:
            error_message = response.text
    except (json.decoder.JSONDecodeError, KeyError):
        error_message = response.text
        if not error_message:
            error_message = response.reason
    if "deny-reason" in response.headers:
        error_message += " " + response.headers["deny-reason"]
    return error_message


def koios_get_request(url: str, parameters: dict[str, Any]) -> list[dict[str, Any]]:
    """
    Create a GET request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param parameters: Parameters to include as data in the GET request
    :return: A list with the body of the response
    :raises MaxRetriesExceeded: When maximum retries are exceeded
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

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(
                url, headers=headers, params=parameters, timeout=REQUEST_TIMEOUT
            )
            if response.status_code == 200:
                resp = json.loads(response.text)
                return resp
            else:
                error_message = get_error_message(response)
                logger.warning(
                    f"status code: {response.status_code} ({error_message}), "
                    f"attempt {attempt + 1}/{MAX_RETRIES}, retrying..."
                )
                logger.error(inspect.stack()[-1])
                sleep(SLEEP_TIME)
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            offset = parameters.get("offset", 0)
            logger.warning(
                f"offset: {offset}, attempt {attempt + 1}/{MAX_RETRIES}, "
                f"retrying in {SLEEP_TIME} second(s)..."
            )
            sleep(SLEEP_TIME)

    raise MaxRetriesExceeded(f"Failed to get {url} after {MAX_RETRIES} attempts")


def koios_post_request(
    url: str,
    params: dict[str, Any],
    parameters: dict[str, Any],
    headers: Optional[dict[str, str]] = None,
) -> list[dict[str, Any]]:
    """
    Create a POST request to Koios API using the "requests" library and return the text of the response as a list
    :param url: URL
    :param params: Parameters to include in the query string
    :param parameters: Parameters to include as data in the POST request
    :param headers: Headers to include in the request
    :return: A list with the body of the response
    :raises MaxRetriesExceeded: When maximum retries are exceeded
    """
    if headers is None:
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
        params["order"] = "block_height.asc"

    for attempt in range(MAX_RETRIES):
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
                return resp
            else:
                error_message = get_error_message(response)
                logger.warning(
                    f"status code: {response.status_code} ({error_message}), "
                    f"attempt {attempt + 1}/{MAX_RETRIES}, retrying..."
                )
                logger.error(inspect.stack()[-1])
                sleep(SLEEP_TIME)
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            offset = parameters.get("offset", 0) if isinstance(parameters, dict) else 0
            logger.warning(
                f"offset: {offset}, attempt {attempt + 1}/{MAX_RETRIES}, "
                f"retrying in {SLEEP_TIME} second(s)..."
            )
            sleep(SLEEP_TIME)

    raise MaxRetriesExceeded(f"Failed to post to {url} after {MAX_RETRIES} attempts")


def koios_post_request_raw(
    url: str,
    data: bytes,
    headers: dict[str, str],
) -> Any:
    """
    Create a POST request to Koios API with raw data (e.g., CBOR)
    :param url: URL
    :param data: Raw data to include in the POST request body
    :param headers: Headers to include in the request
    :return: The response body
    :raises MaxRetriesExceeded: When maximum retries are exceeded
    """
    if KOIOS_API_TOKEN:
        headers["Authorization"] = "Bearer " + KOIOS_API_TOKEN

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                url,
                headers=headers,
                data=data,
                timeout=REQUEST_TIMEOUT,
            )
            if response.status_code in (200, 202):
                return json.loads(response.text)
            else:
                error_message = get_error_message(response)
                logger.warning(
                    f"status code: {response.status_code} ({error_message}), "
                    f"attempt {attempt + 1}/{MAX_RETRIES}, retrying..."
                )
                logger.error(inspect.stack()[-1])
                sleep(SLEEP_TIME)
        except Exception as exc:
            logger.exception(
                f"Exception in {inspect.getframeinfo(inspect.currentframe()).function}: {exc}"
            )
            logger.warning(
                f"attempt {attempt + 1}/{MAX_RETRIES}, "
                f"retrying in {SLEEP_TIME} second(s)..."
            )
            sleep(SLEEP_TIME)

    raise MaxRetriesExceeded(f"Failed to post to {url} after {MAX_RETRIES} attempts")


def paginated_get(
    url: str,
    parameters: dict[str, Any],
    offset: int = 0,
    limit: int = 0,
) -> list[dict[str, Any]]:
    """
    Perform a paginated GET request to Koios API
    :param url: URL
    :param parameters: Parameters to include in the GET request
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of results to return (optional, 0 = unlimited)
    :return: A list with all paginated results
    """
    results: list[dict[str, Any]] = []
    while True:
        if offset > 0:
            parameters["offset"] = offset
        resp = koios_get_request(url, parameters)
        results += resp
        if len(resp) < API_RESP_COUNT:
            break
        offset += len(resp)
        if 0 < limit <= len(results):
            return results[:limit]
    return results[:limit] if limit > 0 else results


def paginated_post(
    url: str,
    qs_parameters: dict[str, Any],
    parameters: dict[str, Any],
    offset: int = 0,
    limit: int = 0,
) -> list[dict[str, Any]]:
    """
    Perform a paginated POST request to Koios API
    :param url: URL
    :param qs_parameters: Parameters to include in the query string
    :param parameters: Parameters to include as data in the POST request
    :param offset: The offset to start from (optional)
    :param limit: The maximum number of results to return (optional, 0 = unlimited)
    :return: A list with all paginated results
    """
    if "limit" not in qs_parameters:
        qs_parameters["limit"] = API_RESP_COUNT
    results: list[dict[str, Any]] = []
    while True:
        if offset > 0:
            qs_parameters["offset"] = offset
        resp = koios_post_request(url, qs_parameters, parameters)
        results += resp
        if len(resp) < API_RESP_COUNT:
            break
        offset += len(resp)
        if 0 < limit <= len(results):
            return results[:limit]
    return results[:limit] if limit > 0 else results
