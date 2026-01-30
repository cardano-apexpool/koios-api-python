"""Script integration tests."""

import pytest

from src.koios_api.script import (
    get_datum_info,
    get_native_script_list,
    get_plutus_script_list,
    get_script_info,
    get_script_redeemers,
    get_script_utxos,
)

from .conftest import (
    TEST_DATUM,
    TEST_SCRIPT,
    assert_has_key,
    assert_list_length,
    assert_non_empty_list,
    assert_valid_response,
)


@pytest.mark.integration
class TestScriptInfo:
    """Tests for get_script_info."""

    def test_script_info_exists(self):
        """Ensure the get_script_info function exists."""
        assert get_script_info

    def test_script_info_single_script(self):
        """Test get_script_info with single script hash."""
        script_info = get_script_info(TEST_SCRIPT)
        assert_list_length(script_info, 1)
        assert script_info[0]["script_hash"] == TEST_SCRIPT

    def test_script_info_as_list(self):
        """Test get_script_info with list of script hashes."""
        script_info = get_script_info([TEST_SCRIPT])
        assert_list_length(script_info, 1)

    def test_script_info_has_expected_fields(self):
        """Test that script info contains expected fields."""
        script_info = get_script_info(TEST_SCRIPT)
        assert_non_empty_list(script_info)
        expected_fields = ["script_hash", "creation_tx_hash", "type"]
        for field in expected_fields:
            assert field in script_info[0]


@pytest.mark.integration
class TestNativeScriptList:
    """Tests for get_native_script_list."""

    def test_native_script_list_exists(self):
        """Ensure the get_native_script_list function exists."""
        assert get_native_script_list

    def test_native_script_list_returns_valid_response(self):
        """Test get_native_script_list returns valid response."""
        native_scripts = get_native_script_list(limit=10)
        assert_valid_response(native_scripts)


@pytest.mark.integration
class TestPlutusScriptList:
    """Tests for get_plutus_script_list."""

    def test_plutus_script_list_exists(self):
        """Ensure the get_plutus_script_list function exists."""
        assert get_plutus_script_list

    def test_plutus_script_list_returns_valid_response(self):
        """Test get_plutus_script_list returns valid response."""
        plutus_scripts = get_plutus_script_list(limit=10)
        assert_valid_response(plutus_scripts)


@pytest.mark.integration
class TestScriptRedeemers:
    """Tests for get_script_redeemers."""

    def test_script_redeemers_exists(self):
        """Ensure the get_script_redeemers function exists."""
        assert get_script_redeemers

    def test_script_redeemers_returns_redeemers(self):
        """Test get_script_redeemers returns redeemer info."""
        script_redeemers = get_script_redeemers(TEST_SCRIPT)
        assert_list_length(script_redeemers, 1)
        assert script_redeemers[0]["script_hash"] == TEST_SCRIPT


@pytest.mark.integration
class TestScriptUtxos:
    """Tests for get_script_utxos."""

    def test_script_utxos_exists(self):
        """Ensure the get_script_utxos function exists."""
        assert get_script_utxos

    def test_script_utxos_returns_utxos(self):
        """Test get_script_utxos returns script utxos."""
        script_utxos = get_script_utxos(TEST_SCRIPT)
        assert_non_empty_list(script_utxos)
        assert_has_key(script_utxos, "tx_hash")


@pytest.mark.integration
class TestDatumInfo:
    """Tests for get_datum_info."""

    def test_datum_info_exists(self):
        """Ensure the get_datum_info function exists."""
        assert get_datum_info

    def test_datum_info_single_datum(self):
        """Test get_datum_info with single datum hash."""
        datum_info = get_datum_info(TEST_DATUM)
        assert_list_length(datum_info, 1)
        assert datum_info[0]["datum_hash"] == TEST_DATUM

    def test_datum_info_as_list(self):
        """Test get_datum_info with list of datum hashes."""
        datum_info = get_datum_info([TEST_DATUM])
        assert_list_length(datum_info, 1)

    def test_datum_info_has_expected_fields(self):
        """Test that datum info contains expected fields."""
        datum_info = get_datum_info(TEST_DATUM)
        assert_non_empty_list(datum_info)
        expected_fields = ["datum_hash", "creation_tx_hash", "value"]
        for field in expected_fields:
            assert field in datum_info[0]


# =============================================================================
# Negative Test Cases
# =============================================================================


@pytest.mark.integration
class TestScriptNegativeCases:
    """Negative test cases for script functions."""

    def test_script_info_empty_list(self):
        """Test get_script_info with empty list."""
        script_info = get_script_info([])
        assert_valid_response(script_info)
        assert len(script_info) == 0

    def test_datum_info_empty_list(self):
        """Test get_datum_info with empty list."""
        datum_info = get_datum_info([])
        assert_valid_response(datum_info)
        assert len(datum_info) == 0
