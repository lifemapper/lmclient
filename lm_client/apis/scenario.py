"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class ScenarioApiService(RestService):
    """
    """
    end_point = 'api/v2/scenario'

    # ...........................
    def count(self, after_time=None, alt_pred_code=None, before_time=None,
              date_code=None, epsg_code=None, gcm_code=None):
        """Counts

        Args:
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, gcm_code=gcm_code)

    # ...........................
    def delete(self, scenario_id):
        """Attempts to delete

        Args:
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, scenario_id))

    # ...........................
    def get(self, scenario_id, interface=None):
        """Attempts to get

        Args:
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, scenario_id),
            interface=interface)

    # ...........................
    def list(self, after_time=None, alt_pred_code=None, before_time=None,
             date_code=None, epsg_code=None, gcm_code=None, limit=None,
             offset=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, self.end_point, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, gcm_code=gcm_code,
            limit=limit, offset=offset)

    # ...........................
    def post(self, scenario_json):
        """
        """
        return RestService.post(
            self, self.end_point, body=scenario_json,
            headers={'Content-Type': 'application/json'})
