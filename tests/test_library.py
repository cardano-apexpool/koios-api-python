"""Library tests"""

from src.koios_api.library import *


def test_library():
    """Ensure the library functions exist"""
    assert get_error_message
    assert koios_get_request
    assert koios_post_request
