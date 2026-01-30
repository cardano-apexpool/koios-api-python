"""Epoch integration tests."""

import pytest

from src.koios_api.epoch import get_epoch_block_protocols, get_epoch_info, get_epoch_params

from .conftest import TEST_EPOCH, assert_list_length, assert_non_empty_list, assert_valid_response


@pytest.mark.integration
class TestEpochInfo:
    """Tests for get_epoch_info."""

    def test_epoch_info_exists(self):
        """Ensure get_epoch_info function exists."""
        assert get_epoch_info

    def test_epoch_info_current(self):
        """Test get_epoch_info for current epoch."""
        epoch_info = get_epoch_info()
        assert_non_empty_list(epoch_info)

    def test_epoch_info_specific_epoch(self):
        """Test get_epoch_info for specific epoch."""
        epoch_info = get_epoch_info(TEST_EPOCH)
        assert_list_length(epoch_info, 1)
        assert epoch_info[0]["epoch_no"] == TEST_EPOCH

    def test_epoch_info_has_expected_fields(self):
        """Test that epoch info contains expected fields."""
        epoch_info = get_epoch_info(TEST_EPOCH)
        assert_non_empty_list(epoch_info)
        expected_fields = ["epoch_no", "start_time", "end_time", "blk_count", "tx_count"]
        for field in expected_fields:
            assert field in epoch_info[0]


@pytest.mark.integration
class TestEpochParams:
    """Tests for get_epoch_params."""

    def test_epoch_params_exists(self):
        """Ensure get_epoch_params function exists."""
        assert get_epoch_params

    def test_epoch_params_current(self):
        """Test get_epoch_params for current epoch."""
        epoch_params = get_epoch_params()
        assert_non_empty_list(epoch_params)

    def test_epoch_params_specific_epoch(self):
        """Test get_epoch_params for specific epoch."""
        epoch_params = get_epoch_params(TEST_EPOCH)
        assert_list_length(epoch_params, 1)
        assert epoch_params[0]["epoch_no"] == TEST_EPOCH

    def test_epoch_params_has_expected_fields(self):
        """Test that epoch params contains expected fields."""
        epoch_params = get_epoch_params(TEST_EPOCH)
        assert_non_empty_list(epoch_params)
        expected_fields = ["epoch_no", "min_fee_a", "min_fee_b", "max_block_size"]
        for field in expected_fields:
            assert field in epoch_params[0]


@pytest.mark.integration
class TestEpochBlockProtocols:
    """Tests for get_epoch_block_protocols."""

    def test_epoch_block_protocols_exists(self):
        """Ensure get_epoch_block_protocols function exists."""
        assert get_epoch_block_protocols

    def test_epoch_block_protocols_specific_epoch(self):
        """Test get_epoch_block_protocols for specific epoch."""
        epoch_block_protocols = get_epoch_block_protocols(TEST_EPOCH)
        assert_list_length(epoch_block_protocols, 1)
        assert epoch_block_protocols[0]["proto_major"] == 8

    def test_epoch_block_protocols_has_expected_fields(self):
        """Test that epoch block protocols contains expected fields."""
        epoch_block_protocols = get_epoch_block_protocols(TEST_EPOCH)
        assert_non_empty_list(epoch_block_protocols)
        expected_fields = ["proto_major", "proto_minor", "blocks"]
        for field in expected_fields:
            assert field in epoch_block_protocols[0]


# =============================================================================
# Parametrized Tests
# =============================================================================


@pytest.mark.integration
class TestEpochParametrized:
    """Parametrized tests for epoch functions."""

    @pytest.mark.parametrize("epoch", [TEST_EPOCH, TEST_EPOCH - 1, TEST_EPOCH - 10])
    def test_epoch_info_various_epochs(self, epoch):
        """Test get_epoch_info for various epochs."""
        epoch_info = get_epoch_info(epoch)
        assert_list_length(epoch_info, 1)
        assert epoch_info[0]["epoch_no"] == epoch

    @pytest.mark.parametrize("epoch", [TEST_EPOCH, TEST_EPOCH - 1])
    def test_epoch_params_various_epochs(self, epoch):
        """Test get_epoch_params for various epochs."""
        epoch_params = get_epoch_params(epoch)
        assert_list_length(epoch_params, 1)
        assert epoch_params[0]["epoch_no"] == epoch
