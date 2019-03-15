"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class EnvLayerApiService(RestService):
    """
    """
    end_point = 'api/v2/envlayer'

    # ...........................
    def count(self, raw=False, after_time=None, alt_pred_code=None,
              before_time=None, date_code=None, epsg_code=None, env_code=None,
              env_type_id=None, gcm_code=None, scenario_id=None):
        """Counts

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.count(self,
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, env_code=env_code,
            env_type_id=env_type_id, gcm_code=gcm_code,
            scenario_id=scenario_id)

    # ...........................
    def delete(self, env_layer_id, raw=False):
        """Attempts to delete

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.delete(self,
            '{}/{}'.format(self.end_point, env_layer_id), raw=raw)

    # ...........................
    def get(self, env_layer_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}'.format(self.end_point, env_layer_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, alt_pred_code=None,
             before_time=None, date_code=None, epsg_code=None, env_code=None,
             env_type_id=None, gcm_code=None, scenario_id=None, limit=None,
             offset=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(self,
            self.end_point, raw=raw, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, env_code=env_code,
            env_type_id=env_type_id, gcm_code=gcm_code,
            scenario_id=scenario_id, limit=limit, offset=offset)

    # ...........................
    def post(self, layer_content, layer_type, epsg_code, layer_name,
             env_layer_type_id=None, additional_metadata=None, val_units=None,
             env_code=None, gcm_code=None, alt_pred_code=None, date_code=None,
             raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw, body=layer_content,
            headers={'Content-Type' : 'application/json'},
            layer_type=layer_type, epsg_code=epsg_code, layer_name=layer_name,
            env_layer_type_id=env_layer_type_id,
            additional_metadata=additional_metadata, val_units=val_units,
            env_code=env_code, gcm_code=gcm_code, alt_pred_code=alt_pred_code,
            date_code=date_code)
