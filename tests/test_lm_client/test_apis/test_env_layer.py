"""Tests the env_layer service end-point
"""
import json
import os
import random
from xml.etree.ElementTree import fromstring

import pytest

from lm_client.client.client import LmApiClient
from lm_client.common.constants import INTERFACES
from lm_client.common.exceptions import NotFoundError

# .............................................................................
class Test_env_layer_api_service_anon(object):
    """This class anonymously tests the environmental layers service
    """
    # ...........................
    def test_count_no_parameters(self):
        """Tests count without providing any parameters
        """
        cl = LmApiClient()
        env_layer_count = cl.env_layer.count()
        assert env_layer_count >= 0

    # ...........................
    def test_count_with_bad_parameter_values(self):
        """Tests count with invalid parameter values
        """
        cl = LmApiClient()
        env_layer_count = cl.env_layer.count(after_time='bad_value')
        assert env_layer_count == 0

    # ...........................
    def test_count_with_parameters(self):
        """Tests count with parameters
        """
        cl = LmApiClient()
        env_layers = cl.env_layer.list()
        test_time = '{}T{}Z'.format(
            *env_layers[0]['modificationTime'].split(' '))
        all_count = cl.env_layer.count()
        count_before = cl.env_layer.count(before_time=test_time)
        assert count_before < all_count

    # ...........................
    def test_get_invalid(self):
        """Test for invalid environmental layer
        """
        cl = LmApiClient()
        with pytest.raises(NotFoundError):
            cl.env_layer.get('invalid_id')

    # ...........................
    def test_get_invalid_interface(self):
        """Test for valid env layer but invalid interface
        """
        cl = LmApiClient()
        env_layers = cl.env_layer.list()
        env_layer_id = env_layer[0]['id']
        with pytest.raises(NotAcceptableError):
            cl.env_layer.get(env_layer_id, interface='invalid')

    # ...........................
    def test_get_valid_eml(self):
        """Tests that an env layer EML can be retrieved
        """
        cl = LmApiClient()
        env_layers = cl.env_layer.list()
        env_layer_id = env_layers[0]['id']
        env_layer = cl.env_layer.get(
            env_layer_id, interface=INTERFACES.EML)
        assert isinstance(env_layer, str)
        assert fromstring(env_layer)

    # ...........................
    def test_get_valid_gtiff(self):
        """Tests that an env layer geotiff can be retrieved
        """
        cl = LmApiClient()
        env_layers = cl.env_layer.list()
        env_layer_id = env_layers[0]['id']
        env_layer = cl.env_layer.get(
            env_layer_id, interface=INTERFACES.GTIFF)
        assert isinstance(env_layer, bytes)
        # TODO: Validate GeoTiff for env layer

    # ...........................
    def test_get_valid_json(self):
        """Tests that an env layer JSON can be retrieved
        """
        cl = LmApiClient()
        env_layers = cl.env_layer.list()
        env_layer_id = env_layers[0]['id']
        env_layer = cl.env_layer.get(env_layer_id)
        assert isinstance(env_layer, dict)
