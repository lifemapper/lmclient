"""Wrapper for the Lifemapper scenario package endpoint."""
from lm_client.common.api_service import RestService


# .....................................................................................
class ScenarioPackageApiService(RestService):
    """Wrapper class for the scenario package endpoint."""
    end_point = 'api/v2/scenpackage'

    # ...........................
    def count(self, after_time=None, before_time=None, scenario_id=None):
        """Counts scenario packages matching the criteria.

        Args:
            after_time (str): Count scenario packages modified after this time.
            before_time (str): Count scenario packages modified before this time.
            scenario_id (int): Count scenario packages containing this scenario.

        Returns:
            int: The number of matching scenario packages.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            before_time=before_time, scenario_id=scenario_id)

    # ...........................
    def get(self, scenario_package_id, interface=None):
        """Attempts to get a scenario package.

        Args:
            scenario_package_id (int): The identifier of the scenario package to
                retrieve.
            interface (str): The format to retrieve the scenario package in.

        Returns:
            str: XML string of scenario package metadata.
            dict: JSON dictionary of scenario package metadata.
        """
        return RestService.get(
            self,
            '{}/{}'.format(self.end_point, scenario_package_id),
            interface=interface
        )

    # ...........................
    def list(
        self,
        after_time=None,
        before_time=None,
        limit=None,
        offset=None,
        scenario_id=None
    ):
        """Gets a list of scenario package matching the provided criteria.

        Args:
            after_time (str): Return scenario packages modified after this time.
            before_time (str): Return scenario packages modified before this time.
            limit (int): The maximum number of scenario packages to return.
            offset (int): Offset the returned scenario packages by this amount.
            scenario_id (int): Return scenario packages containing this scenario.

        Returns:
            list of dict: A list of JSON dictionaries of scenario package metadata for
                the matching scenario packages.
        """
        return RestService.list(
            self,
            self.end_point,
            after_time=after_time,
            scenario_id=scenario_id,
            before_time=before_time,
            limit=limit,
            offset=offset
        )
