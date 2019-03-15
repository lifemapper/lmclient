"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class ScenarioPackageApiService(RestService):
    """
    """
    end_point = 'api/v2/scenpackage'

    # ...........................
    def count(self, raw=False, after_time=None, before_time=None,
              scenario_id=None):
        """Counts

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.count(self,
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            before_time=before_time, scenario_id=scenario_id)

    # ...........................
    def get(self, scenario_package_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}'.format(self.end_point, scenario_package_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, before_time=None, limit=None,
             offset=None, scenario_id=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(
            self, self.end_point, raw=raw, after_time=after_time,
            scenario_id=scenario_id, before_time=before_time,  limit=limit,
            offset=offset)
