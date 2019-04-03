"""Tests the layer service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_layer_api_service(object):
    """This class tests the layer service.
    """
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.layer.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that layer JSON can be retrieved
        """
        with client_generator.get_client() as cl:
            layers = cl.layer.list()
            layer_id = layers[0]['id']
            layer = cl.layer.get(layer_id)
            assert isinstance(layer, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.layer.list()
            assert len(layers) >= 0
