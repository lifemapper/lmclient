"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class LayerApiService(RestService):
    """
    """
    end_point = 'api/v2/layer'

    # ...........................
    def count(self, after_time=None, before_time=None, epsg_code=None,
              squid=None):
        """Counts

        Args:
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            before_time=before_time, epsg_code=epsg_code, squid=squid)

    # ...........................
    def delete(self, layer_id):
        """Attempts to delete

        Args:
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, layer_id))

    # ...........................
    def get(self, layer_id, interface=None):
        """Attempts to get

        Args:
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, layer_id),
            interface=interface)

    # ...........................
    def list(self, after_time=None, before_time=None, epsg_code=None,
             limit=None, offset=None, squid=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, self.end_point, after_time=after_time,
            before_time=before_time, epsg_code=epsg_code, squid=squid,
            limit=limit, offset=offset)

    # ...........................
    def post(self, layer_content, layer_type, epsg_code, layer_name,
             env_layer_type_id=None, additional_metadata=None, val_units=None,
             env_code=None, gcm_code=None, alt_pred_code=None, date_code=None):
        """
        """
        return RestService.post(
            self, self.end_point, body=layer_content,
            headers={'Content-Type': 'application/json'},
            layer_type=layer_type, epsg_code=epsg_code, layer_name=layer_name,
            env_layer_type_id=env_layer_type_id,
            additional_metadata=additional_metadata, val_units=val_units,
            env_code=env_code, gcm_code=gcm_code, alt_pred_code=alt_pred_code,
            date_code=date_code)
