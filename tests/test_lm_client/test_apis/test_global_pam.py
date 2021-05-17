"""Tests the global_pam service end-point."""


# .....................................................................................
class Test_global_pam_api_service(object):
    """This class tests the global_pam service."""
    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            global_pams = cl.global_pam.list_matches()
            assert len(global_pams) >= 0
