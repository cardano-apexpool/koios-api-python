"""Unit tests for library.py with mocking - no network access required."""


import pytest
import responses

from src.koios_api.__config__ import API_BASE_URL
from src.koios_api.library import (
    MaxRetriesExceeded,
    get_error_message,
    koios_get_request,
    koios_post_request,
    koios_post_request_raw,
    paginated_get,
    paginated_post,
)

# =============================================================================
# Tests for get_error_message
# =============================================================================


@pytest.mark.unit
class TestGetErrorMessage:
    """Tests for the get_error_message function."""

    def test_get_error_message_with_json_message(self, mocker):
        """Test extracting error message from JSON response."""
        mock_response = mocker.Mock()
        mock_response.text = '{"message": "API rate limit exceeded"}'
        mock_response.headers = {}

        result = get_error_message(mock_response)
        assert result == "API rate limit exceeded"

    def test_get_error_message_with_empty_json_message(self, mocker):
        """Test extracting error message when JSON message is empty."""
        mock_response = mocker.Mock()
        mock_response.text = '{"message": ""}'
        mock_response.headers = {}

        result = get_error_message(mock_response)
        assert result == '{"message": ""}'

    def test_get_error_message_with_invalid_json(self, mocker):
        """Test extracting error message from invalid JSON."""
        mock_response = mocker.Mock()
        mock_response.text = "Internal Server Error"
        mock_response.reason = "Internal Server Error"
        mock_response.headers = {}

        result = get_error_message(mock_response)
        assert result == "Internal Server Error"

    def test_get_error_message_with_empty_text(self, mocker):
        """Test extracting error message when text is empty."""
        mock_response = mocker.Mock()
        mock_response.text = ""
        mock_response.reason = "Bad Gateway"
        mock_response.headers = {}

        result = get_error_message(mock_response)
        assert result == "Bad Gateway"

    def test_get_error_message_with_deny_reason_header(self, mocker):
        """Test extracting error message with deny-reason header."""
        mock_response = mocker.Mock()
        mock_response.text = '{"message": "Access denied"}'
        mock_response.headers = {"deny-reason": "IP blocked"}

        result = get_error_message(mock_response)
        assert "Access denied" in result
        assert "IP blocked" in result


# =============================================================================
# Tests for koios_get_request
# =============================================================================


@pytest.mark.unit
class TestKoiosGetRequest:
    """Tests for the koios_get_request function."""

    @responses.activate
    def test_successful_get_request(self):
        """Test a successful GET request."""
        url = f"{API_BASE_URL}/tip"
        expected_response = [{"epoch_no": 450, "block_no": 12345}]

        responses.add(
            responses.GET,
            url,
            json=expected_response,
            status=200,
        )

        result = koios_get_request(url, {})
        assert result == expected_response

    @responses.activate
    def test_get_request_with_parameters(self):
        """Test GET request with query parameters."""
        url = f"{API_BASE_URL}/blocks"
        expected_response = [{"hash": "abc123"}]

        responses.add(
            responses.GET,
            url,
            json=expected_response,
            status=200,
        )

        result = koios_get_request(url, {"limit": 10})
        assert result == expected_response

    @responses.activate
    def test_get_request_adds_order_for_blocks(self):
        """Test that order parameter is added for blocks endpoint."""
        url = f"{API_BASE_URL}/blocks"
        expected_response = [{"hash": "abc123"}]

        responses.add(
            responses.GET,
            url,
            json=expected_response,
            status=200,
        )

        params = {"limit": 10}
        koios_get_request(url, params)
        assert params.get("order") == "block_height.asc"

    @responses.activate
    def test_get_request_retries_on_500_error(self, mocker):
        """Test that GET request retries on 500 error."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 3)

        url = f"{API_BASE_URL}/tip"

        # Add 2 failures followed by a success
        responses.add(responses.GET, url, status=500)
        responses.add(responses.GET, url, status=500)
        responses.add(responses.GET, url, json=[{"epoch_no": 450}], status=200)

        result = koios_get_request(url, {})
        assert result == [{"epoch_no": 450}]
        assert len(responses.calls) == 3

    @responses.activate
    def test_get_request_raises_max_retries_exceeded(self, mocker):
        """Test that MaxRetriesExceeded is raised after max retries."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/tip"

        # Add failures for all retries
        for _ in range(2):
            responses.add(responses.GET, url, status=500)

        with pytest.raises(MaxRetriesExceeded) as exc_info:
            koios_get_request(url, {})

        assert "Failed to get" in str(exc_info.value)
        assert url in str(exc_info.value)

    @responses.activate
    def test_get_request_handles_connection_error(self, mocker):
        """Test that GET request handles connection errors."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/tip"

        # Simulate connection error then success
        responses.add(
            responses.GET,
            url,
            body=ConnectionError("Connection refused"),
        )
        responses.add(responses.GET, url, json=[{"epoch_no": 450}], status=200)

        result = koios_get_request(url, {})
        assert result == [{"epoch_no": 450}]


# =============================================================================
# Tests for koios_post_request
# =============================================================================


@pytest.mark.unit
class TestKoiosPostRequest:
    """Tests for the koios_post_request function."""

    @responses.activate
    def test_successful_post_request(self):
        """Test a successful POST request."""
        url = f"{API_BASE_URL}/account_info"
        expected_response = [{"stake_address": "stake1abc", "status": "registered"}]

        responses.add(
            responses.POST,
            url,
            json=expected_response,
            status=200,
        )

        result = koios_post_request(url, {}, {"_stake_addresses": ["stake1abc"]})
        assert result == expected_response

    @responses.activate
    def test_post_request_with_custom_headers(self):
        """Test POST request with custom headers."""
        url = f"{API_BASE_URL}/account_info"
        expected_response = [{"stake_address": "stake1abc"}]

        responses.add(
            responses.POST,
            url,
            json=expected_response,
            status=200,
        )

        custom_headers = {"Accept": "application/json", "X-Custom": "value"}
        result = koios_post_request(
            url, {}, {"_stake_addresses": ["stake1abc"]}, headers=custom_headers
        )
        assert result == expected_response

    @responses.activate
    def test_post_request_adds_order_for_utxo_info(self):
        """Test that order parameter is added for utxo_info endpoint."""
        url = f"{API_BASE_URL}/utxo_info"
        expected_response = [{"tx_hash": "abc123"}]

        responses.add(
            responses.POST,
            url,
            json=expected_response,
            status=200,
        )

        params = {}
        koios_post_request(url, params, {"_utxo_refs": ["abc#0"]})
        assert params.get("order") == "block_height.asc"

    @responses.activate
    def test_post_request_retries_on_error(self, mocker):
        """Test that POST request retries on error."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 3)

        url = f"{API_BASE_URL}/account_info"

        responses.add(responses.POST, url, status=503)
        responses.add(
            responses.POST, url, json=[{"stake_address": "stake1abc"}], status=200
        )

        result = koios_post_request(url, {}, {"_stake_addresses": ["stake1abc"]})
        assert result == [{"stake_address": "stake1abc"}]
        assert len(responses.calls) == 2

    @responses.activate
    def test_post_request_raises_max_retries_exceeded(self, mocker):
        """Test that MaxRetriesExceeded is raised after max retries."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/account_info"

        for _ in range(2):
            responses.add(responses.POST, url, status=500)

        with pytest.raises(MaxRetriesExceeded) as exc_info:
            koios_post_request(url, {}, {"_stake_addresses": ["stake1abc"]})

        assert "Failed to post" in str(exc_info.value)


# =============================================================================
# Tests for koios_post_request_raw
# =============================================================================


@pytest.mark.unit
class TestKoiosPostRequestRaw:
    """Tests for the koios_post_request_raw function."""

    @responses.activate
    def test_successful_raw_post_request(self):
        """Test a successful raw POST request."""
        url = f"{API_BASE_URL}/submittx"
        expected_response = {"txHash": "abc123"}

        responses.add(
            responses.POST,
            url,
            json=expected_response,
            status=200,
        )

        result = koios_post_request_raw(
            url,
            b"\x84\xa4\x00\x81",
            {"Content-Type": "application/cbor"},
        )
        assert result == expected_response

    @responses.activate
    def test_raw_post_request_accepts_202(self):
        """Test that raw POST request accepts 202 status code."""
        url = f"{API_BASE_URL}/submittx"
        expected_response = {"txHash": "abc123"}

        responses.add(
            responses.POST,
            url,
            json=expected_response,
            status=202,
        )

        result = koios_post_request_raw(
            url,
            b"\x84\xa4\x00\x81",
            {"Content-Type": "application/cbor"},
        )
        assert result == expected_response

    @responses.activate
    def test_raw_post_request_raises_max_retries_exceeded(self, mocker):
        """Test that MaxRetriesExceeded is raised after max retries."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/submittx"

        for _ in range(2):
            responses.add(responses.POST, url, status=500)

        with pytest.raises(MaxRetriesExceeded):
            koios_post_request_raw(
                url,
                b"\x84\xa4\x00\x81",
                {"Content-Type": "application/cbor"},
            )


# =============================================================================
# Tests for paginated_get
# =============================================================================


@pytest.mark.unit
class TestPaginatedGet:
    """Tests for the paginated_get function."""

    @responses.activate
    def test_paginated_get_single_page(self, mocker):
        """Test paginated GET with a single page of results."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 1000)

        url = f"{API_BASE_URL}/blocks"
        # Return fewer than API_RESP_COUNT to indicate last page
        expected_response = [{"hash": f"block{i}"} for i in range(10)]

        responses.add(
            responses.GET,
            url,
            json=expected_response,
            status=200,
        )

        result = paginated_get(url, {"limit": 10})
        assert len(result) == 10

    @responses.activate
    def test_paginated_get_multiple_pages(self, mocker):
        """Test paginated GET with multiple pages of results."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 10)
        mocker.patch("src.koios_api.library.API_RESP_COUNT", 10)

        url = f"{API_BASE_URL}/blocks"

        # First page - full
        page1 = [{"hash": f"block{i}"} for i in range(10)]
        # Second page - partial (last page)
        page2 = [{"hash": f"block{i}"} for i in range(10, 15)]

        responses.add(responses.GET, url, json=page1, status=200)
        responses.add(responses.GET, url, json=page2, status=200)

        result = paginated_get(url, {})
        assert len(result) == 15

    @responses.activate
    def test_paginated_get_with_limit(self, mocker):
        """Test paginated GET respects the limit parameter."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 10)
        mocker.patch("src.koios_api.library.API_RESP_COUNT", 10)

        url = f"{API_BASE_URL}/blocks"

        # Return full page
        page1 = [{"hash": f"block{i}"} for i in range(10)]

        responses.add(responses.GET, url, json=page1, status=200)

        result = paginated_get(url, {}, limit=5)
        assert len(result) == 5

    @responses.activate
    def test_paginated_get_with_offset(self, mocker):
        """Test paginated GET with starting offset."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 1000)

        url = f"{API_BASE_URL}/blocks"
        expected_response = [{"hash": "block100"}]

        responses.add(responses.GET, url, json=expected_response, status=200)

        result = paginated_get(url, {}, offset=100)
        assert len(result) == 1


# =============================================================================
# Tests for paginated_post
# =============================================================================


@pytest.mark.unit
class TestPaginatedPost:
    """Tests for the paginated_post function."""

    @responses.activate
    def test_paginated_post_single_page(self, mocker):
        """Test paginated POST with a single page of results."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 1000)

        url = f"{API_BASE_URL}/account_utxos"
        expected_response = [{"tx_hash": f"tx{i}"} for i in range(10)]

        responses.add(responses.POST, url, json=expected_response, status=200)

        result = paginated_post(url, {}, {"_stake_addresses": ["stake1abc"]})
        assert len(result) == 10

    @responses.activate
    def test_paginated_post_with_limit(self, mocker):
        """Test paginated POST respects the limit parameter."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 10)
        mocker.patch("src.koios_api.library.API_RESP_COUNT", 10)

        url = f"{API_BASE_URL}/account_utxos"
        page1 = [{"tx_hash": f"tx{i}"} for i in range(10)]

        responses.add(responses.POST, url, json=page1, status=200)

        result = paginated_post(url, {}, {"_stake_addresses": ["stake1abc"]}, limit=5)
        assert len(result) == 5

    @responses.activate
    def test_paginated_post_sets_default_limit(self, mocker):
        """Test that paginated POST sets default limit in query parameters."""
        mocker.patch("src.koios_api.__config__.API_RESP_COUNT", 1000)
        mocker.patch("src.koios_api.library.API_RESP_COUNT", 1000)

        url = f"{API_BASE_URL}/account_utxos"
        expected_response = [{"tx_hash": "tx1"}]

        responses.add(responses.POST, url, json=expected_response, status=200)

        qs_params = {}
        paginated_post(url, qs_params, {"_stake_addresses": ["stake1abc"]})
        assert qs_params.get("limit") == 1000


# =============================================================================
# Tests for MaxRetriesExceeded exception
# =============================================================================


@pytest.mark.unit
class TestMaxRetriesExceeded:
    """Tests for the MaxRetriesExceeded exception."""

    def test_exception_message(self):
        """Test that exception contains the correct message."""
        exc = MaxRetriesExceeded("Custom error message")
        assert str(exc) == "Custom error message"

    def test_exception_inheritance(self):
        """Test that MaxRetriesExceeded inherits from Exception."""
        exc = MaxRetriesExceeded("Test")
        assert isinstance(exc, Exception)

    def test_exception_can_be_raised_and_caught(self):
        """Test that exception can be raised and caught properly."""
        with pytest.raises(MaxRetriesExceeded):
            raise MaxRetriesExceeded("Test error")


# =============================================================================
# Edge Cases and Error Scenarios
# =============================================================================


@pytest.mark.unit
class TestEdgeCases:
    """Tests for edge cases and error scenarios."""

    @responses.activate
    def test_get_request_with_empty_response(self):
        """Test GET request handling empty list response."""
        url = f"{API_BASE_URL}/tip"

        responses.add(responses.GET, url, json=[], status=200)

        result = koios_get_request(url, {})
        assert result == []

    @responses.activate
    def test_post_request_with_empty_response(self):
        """Test POST request handling empty list response."""
        url = f"{API_BASE_URL}/account_info"

        responses.add(responses.POST, url, json=[], status=200)

        result = koios_post_request(url, {}, {"_stake_addresses": []})
        assert result == []

    @responses.activate
    def test_get_request_with_rate_limit_error(self, mocker):
        """Test GET request handling rate limit (429) error."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/tip"

        responses.add(
            responses.GET,
            url,
            json={"message": "Rate limit exceeded"},
            status=429,
        )
        responses.add(responses.GET, url, json=[{"epoch_no": 450}], status=200)

        result = koios_get_request(url, {})
        assert result == [{"epoch_no": 450}]

    @responses.activate
    def test_get_request_with_malformed_json(self, mocker):
        """Test GET request handling malformed JSON response."""
        mocker.patch("src.koios_api.library.SLEEP_TIME", 0)
        mocker.patch("src.koios_api.library.MAX_RETRIES", 2)

        url = f"{API_BASE_URL}/tip"

        # First response is malformed JSON
        responses.add(
            responses.GET,
            url,
            body="not valid json{",
            status=200,
        )
        # Second response is valid
        responses.add(responses.GET, url, json=[{"epoch_no": 450}], status=200)

        result = koios_get_request(url, {})
        assert result == [{"epoch_no": 450}]
