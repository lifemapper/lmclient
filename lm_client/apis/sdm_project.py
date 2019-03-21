"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class SdmProjectApiService(RestService):
    """
    """
    end_point = 'api/v2/sdmproject'

    # ...........................
    def count(self, after_status=None, after_time=None,
              algorithm_code=None, before_status=None, before_time=None,
              display_name=None, epsg_code=None, model_scenario_code=None,
              occurrence_set_id=None, projection_scenario_code=None,
              scenario_id=None, status=None, gridset_id=None):
        """Counts

        Args:
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_status=after_status,
            after_time=after_time, algorithm_code=algorithm_code,
            before_status=before_status, before_time=before_time,
            display_name=display_name, epsg_code=epsg_code,
            model_scenario_code=model_scenario_code,
            occurrence_set_id=occurrence_set_id,
            projection_scenario_code=projection_scenario_code,
            scenario_id=scenario_id, status=status, gridset_id=gridset_id)

    # ...........................
    def delete(self, sdmproject_id):
        """Attempts to delete

        Args:
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, _id))

    # ...........................
    def get(self, sdmproject_id, interface=None):
        """Attempts to get

        Args:
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, sdmproject_id),
            interface=interface)

    # ...........................
    def list(self, after_status=None, after_time=None, algorithm_code=None,
             before_status=None, before_time=None, display_name=None,
             epsg_code=None, limit=None, model_scenario_code=None,
             occurrence_set_id=None, offset=None,
             projection_scenario_code=None, scenario_id=None, status=None,
             gridset_id=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, self.end_point, after_time=after_time,
            scenario_id=scenario_id, before_time=before_time, limit=limit,
            offset=offset, after_status=after_status,
            algorithm_code=algorithm_code, before_status=before_status,
            display_name=display_name, epsg_code=epsg_code,
            model_scenario_code=model_scenario_code, status=status,
            occurrence_set_id=occurrence_set_id,
            projection_scenario_code=projection_scenario_code,
            gridset_id=gridset_id)

    # ...........................
    def post(self, boom_post_json):
        """
        """
        return RestService.post(
            self, self.end_point, body=boom_post_json,
            headers={'Content-Type': 'application/json'})
