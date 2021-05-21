"""Tools wrapping the Lifemapper climate scenarios endpoint."""
from lmclient.common.api_service import RestService


# .....................................................................................
class ScenarioApiService(RestService):
    """Class wrapping the climate scenario endpoint."""
    end_point = 'api/v2/scenario'

    # ...........................
    def count(
        self,
        after_time=None,
        alt_pred_code=None,
        before_time=None,
        date_code=None,
        epsg_code=None,
        gcm_code=None
    ):
        """Counts scenarios matching the provided criteria.

        Args:
            after_time (str): Count scenarios modified after this time.
            alt_pred_code (str): Count scenarios containing this alternate prediction
                code.
            before_time (str): Count scenarios modified before this time.
            date_code (str): Count scenarios with this date code.
            epsg_code (int): Count scenarios using this map projection EPSG code.
            gcm_code (str): Count scenario using this GCM code.

        Returns:
            int: The number of scenarios matching the criteria.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, gcm_code=gcm_code
        )

    # ...........................
    def delete(self, scenario_id):
        """Attempts to delete a scenario.

        Args:
            scenario_id (int): The identifier of the scenario to delete.

        Returns:
            HTTP Response: An HTTP status message indicating success.
        """
        return RestService.delete(self, '{}/{}'.format(self.end_point, scenario_id))

    # ...........................
    def get(self, scenario_id, interface=None):
        """Attempts to get a scenario.

        Args:
            scenario_id (int): The identifier of the scenario to retrieve.
            interface (str): The format to return the scenario in.

        Returns:
            str: XML metadata for the scenario.
            dict: JSON dictionary of scenario metadata.
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, scenario_id),
            interface=interface
        )

    # ...........................
    def list(
        self,
        after_time=None,
        alt_pred_code=None,
        before_time=None,
        date_code=None,
        epsg_code=None,
        gcm_code=None,
        limit=None,
        offset=None
    ):
        """Gets a list of scenarios matching the provided criteria.

        Args:
            after_time (str): List scenarios modified after this time.
            alt_pred_code (str): List scenarios containing this alternate prediction
                code.
            before_time (str): List scenarios modified before this time.
            date_code (str): List scenarios with this date code.
            epsg_code (int): List scenarios using this map projection EPSG code.
            gcm_code (str): List scenario using this GCM code.
            limit (int): The maximum number of scenarios to return.
            offset (int): Offset the scenarios returned by this number.

        Returns:
            list of dict: A list of JSON dictionaries of metadata for matching
                scenarios.
        """
        return RestService.list(
            self,
            self.end_point,
            after_time=after_time,
            alt_pred_code=alt_pred_code,
            before_time=before_time,
            date_code=date_code,
            epsg_code=epsg_code,
            gcm_code=gcm_code,
            limit=limit,
            offset=offset
        )

    # ...........................
    def post(self, scenario_json):
        """Post a new scenario to the server.

        Args:
            scenario_json (dict): A JSON dictionary of scenario metadata.

        Returns:
            dict: A JSON dictionary of scenario metadata.
        """
        return RestService.post(
            self, self.end_point, body=scenario_json,
            headers={'Content-Type': 'application/json'}
        )
