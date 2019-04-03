"""Tests the snippet service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_snippet_api_service(object):
    """This class tests the snippet service.
    """
    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            snippets = cl.snippet.list()
            assert len(snippets) >= 0
