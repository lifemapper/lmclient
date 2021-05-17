"""Tests the env_layer service end-point."""
import pytest
from xml.etree.ElementTree import fromstring

from lm_client.common.constants import INTERFACES
from lm_client.common.exceptions import (
    BadRequestError,
    NotAcceptableError,
    NotFoundError
)


# .....................................................................................
class Test_env_layer_api_service(object):
    """This class tests the environmental layers service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layer_count = cl.env_layer.count()
            assert env_layer_count >= 0

    # ...........................
    def test_count_with_bad_parameter_values(self, client_generator):
        """Tests count with invalid parameter values.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layer_count = cl.env_layer.count(after_time='bad_value')
            assert env_layer_count == 0

    # ...........................
    def test_count_with_parameters(self, client_generator):
        """Tests count with parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            test_time = '{}T{}Z'.format(
                *env_layers[0]['modificationTime'].split(' '))
            all_count = cl.env_layer.count()
            count_before = cl.env_layer.count(before_time=test_time)
            assert count_before < all_count

    # ...........................
    def test_get_invalid_bad_id(self, client_generator):
        """Tests get with invalid environmental layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            with pytest.raises(NotFoundError):
                cl.env_layer.get(-9999999)

    # ...........................
    def test_get_invalid_string_id(self, client_generator):
        """Tests get with invalid environmental layer id (string).

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            with pytest.raises(BadRequestError):
                cl.env_layer.get('invalid_id')

    # ...........................
    def test_get_invalid_interface(self, client_generator):
        """Test for valid env layer but invalid interface.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            with pytest.raises(NotAcceptableError):
                cl.env_layer.get(
                    env_layer_id, interface=INTERFACES.SHAPEFILE)

    # ...........................
    def test_get_valid_eml(self, client_generator):
        """Tests that an env layer EML can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.EML)
            assert fromstring(env_layer) is not None

    # ...........................
    def test_get_valid_gtiff(self, client_generator):
        """Tests that an env layer geotiff can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.GTIFF)
            assert isinstance(env_layer, bytes)
            # TODO: Validate GeoTiff for env layer

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that an env layer JSON can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer = cl.env_layer.get(env_layer_id)
            assert isinstance(env_layer, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            lyrs = cl.env_layer.list()
            assert len(lyrs) >= 0

    # ...........................
    def test_list_with_bad_parameter_values(self, client_generator):
        """Tests list with invalid parameter values.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.env_layer.list(after_time='bad_value')
            assert len(layers) == 0

    # ...........................
    def test_list_with_parameters(self, client_generator):
        """Tests list with parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.env_layer.list()
            test_time = '{}T{}Z'.format(
                *layers[0]['modificationTime'].split(' '))
            all_count = cl.env_layer.count()
            layers_before = cl.env_layer.list(before_time=test_time)
            assert len(layers_before) < all_count
