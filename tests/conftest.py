"""Pytest configuration and shared fixtures for koios-api tests."""

import pytest

# =============================================================================
# Test Data Constants - Mainnet
# =============================================================================

# Account/Stake Address test data
TEST_STAKE_ADDRESS = "stake1uyrx65wjqjgeeksd8hptmcgl5jfyrqkfq0xe8xlp367kphsckq250"

# Address test data
TEST_ADDRESS = "addr1q9ur45a5t58dyx5mu5zts997s24vxft9uuvwjep25dpym8qxd4gaypy3nndq60wzhhs3lfyjgxpvjq7djwd7rr4avr0qcmdyc0"
TEST_CREDENTIAL = "783ad3b45d0ed21a9be504b814be82aac32565e718e9642aa3424d9c"

# Asset test data
TEST_ASSET = "asset100pa5wvqk7xgqava96745yny2wk6tq5v9sr67d"
TEST_NFT_POLICY = "0e14267a8020229adc0184dd25fa3174c3f7d6caadcb4425c70e7c04"
TEST_ASSET_NAME = "756e7369673132393834"
TEST_FT_POLICY = "750900e4999ebe0d58f19b634768ba25e525aaf12403bfe8fe130501"

# Block test data
TEST_BLOCK = "8a2e06c0bf499d8feefb43ec739be8de1aeb474f458a21cce381d39f51a055c4"
TEST_BLOCK_TX_COUNT = 7

# Pool test data
TEST_POOL = "pool17rjst78s67lvellg8s586rf076jxa3wnsdz730f4xk2zwuhrtej"

# Script test data
TEST_SCRIPT = "bd2119ee2bfb8c8d7c427e8af3c35d537534281e09e23013bca5b138"
TEST_DATUM = "818ee3db3bbbd04f9f2ce21778cac3ac605802a4fcb00c8b3a58ee2dafc17d46"

# Transaction test data
TEST_TX = "291b5533227331999eca2e63934c1061e5f85993e77747a90d9901413d7bb937"

# Epoch test data
TEST_EPOCH = 450


# =============================================================================
# Invalid Test Data - For negative test cases
# =============================================================================

INVALID_STAKE_ADDRESS = "stake1invalid_address_format_12345"
INVALID_ADDRESS = "addr1invalid_address_format_12345"
INVALID_TX_HASH = "0000000000000000000000000000000000000000000000000000000000000000"
INVALID_BLOCK_HASH = "0000000000000000000000000000000000000000000000000000000000000000"
INVALID_POOL_ID = "pool1invalid_pool_id_12345"
INVALID_POLICY_ID = "invalid_policy_id"
INVALID_SCRIPT_HASH = "invalid_script_hash"


# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def stake_address():
    """Return a valid test stake address."""
    return TEST_STAKE_ADDRESS


@pytest.fixture
def address():
    """Return a valid test address."""
    return TEST_ADDRESS


@pytest.fixture
def credential():
    """Return a valid test credential."""
    return TEST_CREDENTIAL


@pytest.fixture
def asset_info():
    """Return test asset information."""
    return {
        "fingerprint": TEST_ASSET,
        "policy_id": TEST_NFT_POLICY,
        "asset_name": TEST_ASSET_NAME,
    }


@pytest.fixture
def pool_id():
    """Return a valid test pool ID."""
    return TEST_POOL


@pytest.fixture
def block_hash():
    """Return a valid test block hash."""
    return TEST_BLOCK


@pytest.fixture
def tx_hash():
    """Return a valid test transaction hash."""
    return TEST_TX


@pytest.fixture
def script_hash():
    """Return a valid test script hash."""
    return TEST_SCRIPT


@pytest.fixture
def datum_hash():
    """Return a valid test datum hash."""
    return TEST_DATUM


@pytest.fixture
def epoch():
    """Return a test epoch number."""
    return TEST_EPOCH


# =============================================================================
# Mock Response Fixtures
# =============================================================================


@pytest.fixture
def mock_api_success_response():
    """Return a mock successful API response structure."""
    return [{"status": "success", "data": "test"}]


@pytest.fixture
def mock_api_empty_response():
    """Return a mock empty API response."""
    return []


@pytest.fixture
def mock_api_error_response():
    """Return a mock error response structure."""
    return {"message": "API Error", "code": 500}


@pytest.fixture
def mock_account_info():
    """Return a mock account info response."""
    return [
        {
            "stake_address": TEST_STAKE_ADDRESS,
            "status": "registered",
            "delegated_pool": TEST_POOL,
            "total_balance": "1000000000",
            "utxo": "1000000000",
            "rewards": "0",
            "withdrawals": "0",
            "rewards_available": "0",
        }
    ]


@pytest.fixture
def mock_block_info():
    """Return a mock block info response."""
    return [
        {
            "hash": TEST_BLOCK,
            "epoch_no": TEST_EPOCH,
            "abs_slot": 12345678,
            "epoch_slot": 12345,
            "block_height": 9876543,
            "block_size": 1234,
            "block_time": 1234567890,
            "tx_count": TEST_BLOCK_TX_COUNT,
            "vrf_key": "vrf_key_here",
            "pool": TEST_POOL,
        }
    ]


@pytest.fixture
def mock_tip_response():
    """Return a mock tip response."""
    return [
        {
            "hash": TEST_BLOCK,
            "epoch_no": TEST_EPOCH,
            "abs_slot": 12345678,
            "epoch_slot": 12345,
            "block_no": 9876543,
            "block_time": 1234567890,
        }
    ]


# =============================================================================
# Helper Functions
# =============================================================================


def assert_valid_response(response, expected_type=list):
    """Assert that an API response is valid and of the expected type."""
    assert response is not None
    assert isinstance(response, expected_type)


def assert_non_empty_list(response):
    """Assert that a response is a non-empty list."""
    assert_valid_response(response, list)
    assert len(response) > 0


def assert_list_length(response, expected_length):
    """Assert that a response list has the expected length."""
    assert_valid_response(response, list)
    assert len(response) == expected_length


def assert_has_key(response, key):
    """Assert that the first item in a response list has a specific key."""
    assert_non_empty_list(response)
    assert key in response[0]
