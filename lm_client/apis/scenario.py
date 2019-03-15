"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class ScenarioApiService(RestService):
    """
    """
    end_point = 'api/v2/scenario'

    # ...........................
    def count(self, raw=False, after_time=None, alt_pred_code=None,
              before_time=None, date_code=None, epsg_code=None, gcm_code=None):
        """Counts

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.count(self, 
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, gcm_code=gcm_code)

    # ...........................
    def delete(self, scenario_id, raw=False):
        """Attempts to delete

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.delete(self, 
            '{}/{}'.format(self.end_point, scenario_id), raw=raw)

    # ...........................
    def get(self, scenario_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self, 
            '{}/{}'.format(self.end_point, scenario_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, alt_pred_code=None,
             before_time=None, date_code=None, epsg_code=None, gcm_code=None,
             limit=None, offset=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(self,
            self.end_point, raw=raw, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, gcm_code=gcm_code,
            limit=limit, offset=offset)

    # ...........................
    def post(self, scenario_json, raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw, body=scenario_json,
            headers={'Content-Type' : 'application/json'})
