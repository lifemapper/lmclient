"""Tests the occurrence service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_occurrence_api_service(object):
    """This class tests the occurrence service.
    """
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.occurrence.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that occurrence JSON can be retrieved
        """
        with client_generator.get_client() as cl:
            occurrences = cl.occurrence.list()
            occurrence_id = occurrences[0]['id']
            occurrence = cl.occurrence.get(occurrence_id)
            assert isinstance(occurrence, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            occurrences = cl.occurrence.list()
            assert len(occurrences) >= 0
