"""Tests the gridset service end-point."""


# .............................................................................
class Test_gridset_api_service:
    """This class tests the gridset service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.gridset.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that gridset JSON can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            gridsets = cl.gridset.list()
            gridset_id = gridsets[0]['id']
            gridset = cl.gridset.get(gridset_id)
            assert isinstance(gridset, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            gridsets = cl.gridset.list()
            assert len(gridsets) >= 0
