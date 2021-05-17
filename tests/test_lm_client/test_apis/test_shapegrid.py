"""Tests the shapegrid service end-point."""


# .............................................................................
class Test_shapegrid_api_service:
    """This class tests the shapegrid service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.shapegrid.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that shapegrid JSON can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            shapegrid_id = shapegrids[0]['id']
            shapegrid = cl.shapegrid.get(shapegrid_id)
            assert isinstance(shapegrid, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            shapegrids = cl.shapegrid.list()
            assert len(shapegrids) >= 0
