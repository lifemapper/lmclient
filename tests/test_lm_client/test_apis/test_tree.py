"""Tests the tree service end-point."""


# .............................................................................
class Test_tree_api_service:
    """This class tests the tree service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.tree.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that tree JSON can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            trees = cl.tree.list()
            tree_id = trees[0]['id']
            tree = cl.tree.get(tree_id)
            assert isinstance(tree, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            trees = cl.tree.list()
            assert len(trees) >= 0
