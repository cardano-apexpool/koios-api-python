"""Epoch section functions"""
from typing import Any

from .__config__ import API_BASE_URL
from .library import koios_get_request


def get_epoch_info(
    epoch: int = 0, include_next_epoch: bool = False
) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/epoch_info
    Get the epoch information, all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :param include_next_epoch: (optional) Include information about nearing but not yet started epoch,
    to get access to active stake snapshot information if available
    :returns: The list of detailed summary for each epoch
    """
    url = API_BASE_URL + "/epoch_info"
    parameters: dict[str, Any] = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    if isinstance(include_next_epoch, bool):
        parameters["_include_next_epoch"] = str(include_next_epoch).lower()
    return koios_get_request(url, parameters)


def get_epoch_params(epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/epoch_params
    Get the protocol parameters for specific epoch, returns information about all epochs if no epoch specified
    :param epoch: (optional) Epoch
    :returns: The list of protocol parameters for each epoch
    """
    url = API_BASE_URL + "/epoch_params"
    parameters: dict[str, Any] = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_get_request(url, parameters)


def get_epoch_block_protocols(epoch: int = 0) -> list[dict[str, Any]]:
    """
    https://api.koios.rest/#get-/epoch_block_protocols
    Get the information about block protocol distribution in epoch
    :param epoch: (optional) Epoch
    :returns: The list of distinct block protocol versions counts in epoch
    """
    url = API_BASE_URL + "/epoch_block_protocols"
    parameters: dict[str, Any] = {}
    if isinstance(epoch, int) and epoch > 0:
        parameters["_epoch_no"] = epoch
    return koios_get_request(url, parameters)
