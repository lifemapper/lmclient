"""Tests the sdm_project service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_sdm_project_api_service(object):
    """This class tests the sdm projections service.
    """
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.sdm_project.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that projection JSON can be retrieved
        """
        with client_generator.get_client() as cl:
            prjs = cl.sdm_project.list()
            prj_id = prjs[0]['id']
            prj = cl.sdm_project.get(prj_id)
            assert isinstance(prj, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            prjs = cl.sdm_project.list()
            assert len(prjs) >= 0
