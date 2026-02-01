"""Epoch integration tests."""

import pytest

from src.koios_api.epoch import get_epoch_block_protocols, get_epoch_info, get_epoch_params

from .conftest import TEST_EPOCH, assert_list_length, assert_non_empty_list


@pytest.mark.integration
class TestEpochInfo:
    """Tests for get_epoch_info."""

    def test_epoch_info_exists(self):
        """Ensure get_epoch_info function exists."""
        assert get_epoch_info

    def test_epoch_info_specific_epoch(self):
        """Test get_epoch_info for specific epoch with expected fields."""
        epoch_info = get_epoch_info(TEST_EPOCH)
        assert_list_length(epoch_info, 1)
        assert epoch_info[0]["epoch_no"] == TEST_EPOCH
        expected_fields = ["epoch_no", "start_time", "end_time", "blk_count", "tx_count"]
        for field in expected_fields:
            assert field in epoch_info[0]


@pytest.mark.integration
class TestEpochParams:
    """Tests for get_epoch_params."""

    def test_epoch_params_exists(self):
        """Ensure get_epoch_params function exists."""
        assert get_epoch_params

    def test_epoch_params_specific_epoch(self):
        """Test get_epoch_params for specific epoch with expected fields."""
        epoch_params = get_epoch_params(TEST_EPOCH)
        assert_list_length(epoch_params, 1)
        assert epoch_params[0]["epoch_no"] == TEST_EPOCH
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
        """Test get_epoch_block_protocols for specific epoch with expected fields."""
        epoch_block_protocols = get_epoch_block_protocols(TEST_EPOCH)
        assert_list_length(epoch_block_protocols, 1)
        assert epoch_block_protocols[0]["proto_major"] == 8
        expected_fields = ["proto_major", "proto_minor", "blocks"]
        for field in expected_fields:
            assert field in epoch_block_protocols[0]
