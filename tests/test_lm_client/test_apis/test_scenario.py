"""Tests the scenario service end-point."""


# .............................................................................
class Test_scenario_api_service:
    """This class tests the scenario service."""
    # ...........................
    def test_count_no_parameters(self, client_generator):
        """Tests count without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            count = cl.scenario.count()
            assert count >= 0

    # ...........................
    def test_get_valid_json(self, client_generator):
        """Tests that scenario JSON can be retrieved.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            scenarios = cl.scenario.list()
            scenario_id = scenarios[0]['id']
            scenario = cl.scenario.get(scenario_id)
            assert isinstance(scenario, dict)

    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            scenarios = cl.scenario.list()
            assert len(scenarios) >= 0
