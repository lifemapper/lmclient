"""Tests the scenario_package service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_scenario_package_api_service(object):
    """This class tests the scenario_package service.
    """
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.scenario_package.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that scenario_package JSON can be retrieved
        """
        with client_generator.get_client() as cl:
            scenario_packages = cl.scenario_package.list()
            scenario_package_id = scenario_packages[0]['id']
            scenario_package = cl.scenario_package.get(scenario_package_id)
            assert isinstance(scenario_package, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            scenario_packages = cl.scenario_package.list()
            assert len(scenario_packages) >= 0
