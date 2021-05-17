"""Tests the layer service end-point."""
import pytest
from xml.etree.ElementTree import fromstring

from lm_client.common.constants import INTERFACES
from lm_client.common.exceptions import (
    BadRequestError,
    NotAcceptableError,
    NotFoundError
)


# .....................................................................................
class Test_layer_api_service:
    """This class tests the layers service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layer_count = cl.layer.count()
            assert layer_count >= 0

    # ...........................
    def test_count_with_bad_parameter_values(self, client_generator):
        """Tests count with invalid parameter values.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layer_count = cl.layer.count(after_time='bad_value')
            assert layer_count == 0

    # ...........................
    def test_count_with_parameters(self, client_generator):
        """Tests count with parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.layer.list()
            test_time = '{}T{}Z'.format(
                *layers[0]['modificationTime'].split(' '))
            all_count = cl.layer.count()
            count_before = cl.layer.count(before_time=test_time)
            assert count_before < all_count

    # ...........................
    def test_get_invalid_bad_id(self, client_generator):
        """Tests get with invalid layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            with pytest.raises(NotFoundError):
                cl.layer.get(-9999999)

    # ...........................
    def test_get_invalid_string_id(self, client_generator):
        """Tests get with invalid layer id (string).

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            with pytest.raises(BadRequestError):
                cl.layer.get('invalid_id')

    # ...........................
    def test_get_vector_valid_eml(self, client_generator):
        """Tests retrieving EML for valid vector layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            shapegrid_id = shapegrids[0]['id']
            shapegrid_dict = cl.shapegrid.get(
                shapegrid_id, interface=INTERFACES.JSON)
            lyr_url = shapegrid_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(
                layer_id, interface=INTERFACES.EML)
            assert fromstring(layer) is not None

    # ...........................
    def test_get_vector_valid_json(self, client_generator):
        """Tests retrieving JSON for valid vector layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            shapegrid_id = shapegrids[0]['id']
            shapegrid_dict = cl.shapegrid.get(
                shapegrid_id, interface=INTERFACES.JSON)
            lyr_url = shapegrid_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(layer_id, interface=INTERFACES.JSON)
            assert isinstance(layer, dict)

    # ...........................
    def test_get_vector_valid_shapefile(self, client_generator):
        """Tests retrieving SHAPEFILE for valid vector layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            shapegrid_id = shapegrids[0]['id']
            shapegrid_dict = cl.shapegrid.get(
                shapegrid_id, interface=INTERFACES.JSON)
            lyr_url = shapegrid_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(layer_id, interface=INTERFACES.SHAPEFILE)
            assert isinstance(layer, bytes)
            # TODO: Validate bytes, unzip and check with OGR

    # ...........................
    def test_get_vector_invalid_interface(self, client_generator):
        """Tests retrieving an invalid interface for valid vector layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            shapegrid_id = shapegrids[0]['id']
            shapegrid_dict = cl.shapegrid.get(
                shapegrid_id, interface=INTERFACES.JSON)
            lyr_url = shapegrid_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            with pytest.raises(NotAcceptableError):
                cl.layer.get(layer_id, interface=INTERFACES.GTIFF)

    # ...........................
    def test_get_raster_valid_eml(self, client_generator):
        """Tests retrieving EML for valid raster layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer_dict = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.JSON)
            lyr_url = env_layer_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(
                layer_id, interface=INTERFACES.EML)
            assert fromstring(layer) is not None

    # ...........................
    def test_get_raster_valid_json(self, client_generator):
        """Tests retrieving JSON for valid raster layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer_dict = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.JSON)
            lyr_url = env_layer_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(layer_id, interface=INTERFACES.JSON)
            assert isinstance(layer, dict)

    # ...........................
    def test_get_raster_valid_gtiff(self, client_generator):
        """Tests retrieving GTIFF for valid raster layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer_dict = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.JSON)
            lyr_url = env_layer_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            layer = cl.layer.get(layer_id, interface=INTERFACES.GTIFF)
            assert isinstance(layer, bytes)
            # TODO: Validate bytes with GDAL

    # ...........................
    def test_get_raster_invalid_interface(self, client_generator):
        """Tests retrieving an invalid interface for valid raster layer.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            env_layers = cl.env_layer.list()
            env_layer_id = env_layers[0]['id']
            env_layer_dict = cl.env_layer.get(
                env_layer_id, interface=INTERFACES.JSON)
            lyr_url = env_layer_dict['url']
            layer_id = lyr_url.split('/')[-1].strip()
            with pytest.raises(NotAcceptableError):
                cl.layer.get(layer_id, interface=INTERFACES.SHAPEFILE)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            lyrs = cl.layer.list()
            assert len(lyrs) >= 0

    # ...........................
    def test_list_with_bad_parameter_values(self, client_generator):
        """Tests list with invalid parameter values.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.layer.list(after_time='bad_value')
            assert len(layers) == 0

    # ...........................
    def test_list_with_parameters(self, client_generator):
        """Tests list with parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            layers = cl.layer.list()
            test_time = '{}T{}Z'.format(
                *layers[0]['modificationTime'].split(' '))
            all_count = cl.layer.count()
            layers_before = cl.layer.list(before_time=test_time)
            assert len(layers_before) < all_count
