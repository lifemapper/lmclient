"""Module containing a class for accessing the layer end-point.
"""


from lm_client.common.api_service import RestService


# .............................................................................
class LayerApiService(RestService):
    """Class for accessing the layer service end-point.
    """
    end_point = 'api/v2/layer'

    # ...........................
    def count(self, after_time=None, before_time=None, epsg_code=None,
              squid=None):
        """Counts layers matching the specified criteria.

        Args:
            after_time (:obj:`str`, optional): Matching layers are modified
                after this time specified in ISO-8601 format.
            before_time (:obj:`str`, optional): Matching layers are modified
                before this time specified in ISO-8601 format.
            epsg_code (:obj:`int`, optional): Matching layers will have the map
                projection specified by this EPSG code.
            squid (:obj:`str`, optional): Matching layers will have this hash-
                based species identifier.

        Returns:
            int - The number of matching layers.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            before_time=before_time, epsg_code=epsg_code, squid=squid)

    # ...........................
    def get(self, layer_id, interface=None):
        """Attempts to get a layer

        Args:
            layer_id (int): The identifier of the layer to be retrieved.
            interface (:obj:`str`, optional): The format in which to return the
                layer.  Valid formats are eml, json and either gtiff or
                shapefile.

        Raises:
            BadRequestError: Raised if the layer id provided is invalid.
            ForbiddenError: Raised if the client user does not have permission
                to access the specified layer.
            NotAcceptableError: Raised if the layer cannot be returned in the
                specified format.
            NotFoundError: Raised if the specified layer was not found on the
                server.
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, layer_id),
            interface=interface)

    # ...........................
    def list(self, after_time=None, before_time=None, epsg_code=None,
             limit=None, offset=None, squid=None):
        """Gets a list of layers matching the specified criteria.

        Args:
            after_time (:obj:`str`, optional): Matching layers are modified
                after this time specified in ISO-8601 format.
            before_time (:obj:`str`, optional): Matching layers are modified
                before this time specified in ISO-8601 format.
            epsg_code (:obj:`int`, optional): Matching layers will have the map
                projection specified by this EPSG code.
            limit (:obj:`int`, optional): Return, at most, this many layers.
            offset (:obj:`int`, optional): Offset the returned layers by this
                amount.  Useful for paging.
            squid (:obj:`str`, optional): Matching layers will have this hash-
                based species identifier.

        Returns:
            list of dicts - A list of layer dictionary objects with metadata
                about each one.  The response format is JSON.
        """
        return RestService.list(
            self, self.end_point, after_time=after_time,
            before_time=before_time, epsg_code=epsg_code, squid=squid,
            limit=limit, offset=offset)
