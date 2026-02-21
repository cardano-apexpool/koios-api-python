"""Library integration tests."""

import pytest

from src.koios_api.library import (
    MaxRetriesExceeded,
    get_error_message,
    koios_get_request,
    koios_post_request,
    koios_post_request_raw,
    paginated_get,
    paginated_post,
)


@pytest.mark.integration
class TestLibraryFunctions:
    """Tests for library functions existence."""

    def test_get_error_message_exists(self):
        """Ensure the get_error_message function exists."""
        assert get_error_message

    def test_koios_get_request_exists(self):
        """Ensure the koios_get_request function exists."""
        assert koios_get_request

    def test_koios_post_request_exists(self):
        """Ensure the koios_post_request function exists."""
        assert koios_post_request

    def test_koios_post_request_raw_exists(self):
        """Ensure the koios_post_request_raw function exists."""
        assert koios_post_request_raw

    def test_paginated_get_exists(self):
        """Ensure the paginated_get function exists."""
        assert paginated_get

    def test_paginated_post_exists(self):
        """Ensure the paginated_post function exists."""
        assert paginated_post

    def test_max_retries_exceeded_exists(self):
        """Ensure the MaxRetriesExceeded exception exists."""
        assert MaxRetriesExceeded
