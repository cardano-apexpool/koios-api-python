"""Config tests"""

from src.koios_api.__config__ import *


def test_config():
    """Ensure the API_BASE_URL exists"""
    assert API_BASE_URL
