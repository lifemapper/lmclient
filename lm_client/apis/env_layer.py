"""Module containing a class for accessing the environmental layer end-point.
"""


from lm_client.common.api_service import RestService


# .............................................................................
class EnvLayerApiService(RestService):
    """Class for accessing the environmental layer service end-point.
    """
    end_point = 'api/v2/envlayer'

    # ...........................
    def count(self, after_time=None, alt_pred_code=None, before_time=None,
              date_code=None, epsg_code=None, env_code=None, env_type_id=None,
              gcm_code=None, scenario_id=None):
        """Counts environmental layers matching the specified criteria.

        Args:
            after_time (:obj:`str`, optional): Matching environmental layers
                are modified after this time specified in ISO-8601 format.
            alt_pred_code (:obj:`str`, optional): Matching environmental layers
                must have this alternate prediction code.
            before_time (:obj:`str`, optional): Matching environmental layers
                are modified before this time specified in ISO-8601 format.
            date_code (:obj:`str`, optional): Matching environmental layers
                will have this date code.
            epsg_code (:obj:`int`, optional): Matching environmental layers
                will have the map projection specified by this EPSG code.
            env_code (:obj:`str`, optional): Matching environmental layers
                will have this environment code.
            env_type_id (:obj:`str`, optional): Matching environmental layers
                will have this environmental layer type identifier.
            gcm_code (:obj:`str`, optional): Matching environmental layers
                will have this GCM code.
            scenario_id (:obj:`int`, optional): Matching environmental layers
                will belong to the Lifemapper scenario specified by this
                identifier.

        Returns:
            int - The number of matching environmental layers.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, env_code=env_code,
            env_type_id=env_type_id, gcm_code=gcm_code,
            scenario_id=scenario_id)

    # ...........................
    def get(self, env_layer_id, interface=None):
        """Attempts to get an environmental layer

        Args:
            env_layer_id (int): The identifier of the environmental layer to be
                retrieved.
            interface (:obj:`str`, optional): The format in which to return the
                environmental layer.  Valid formats are eml, gtiff and json.

        Raises:
            BadRequestError: Raised if the environmental layer id provided is
                invalid.
            ForbiddenError: Raised if the client user does not have permission
                to access the specified environmental layer.
            NotAcceptableError: Raised if the environmental layer cannot be
                returned in the specified format.
            NotFoundError: Raised if the specified environmental layer was not
                found on the server.

        Returns:
            dict - Returned if JSON interface is selected.
            bytes - Returned if GTIFF interface is selected.
            xml string - Returned if the EML interface is selected.
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, env_layer_id),
            interface=interface)

    # ...........................
    def list(self, after_time=None, alt_pred_code=None,
             before_time=None, date_code=None, epsg_code=None, env_code=None,
             env_type_id=None, gcm_code=None, scenario_id=None, limit=None,
             offset=None):
        """Gets a list of environmental layers matching the specified criteria.

        Args:
            after_time (:obj:`str`, optional): Matching environmental layers
                are modified after this time specified in ISO-8601 format.
            alt_pred_code (:obj:`str`, optional): Matching environmental layers
                must have this alternate prediction code.
            before_time (:obj:`str`, optional): Matching environmental layers
                are modified before this time specified in ISO-8601 format.
            date_code (:obj:`str`, optional): Matching environmental layers
                will have this date code.
            epsg_code (:obj:`int`, optional): Matching environmental layers
                will have the map projection specified by this EPSG code.
            env_code (:obj:`str`, optional): Matching environmental layers
                will have this environment code.
            env_type_id (:obj:`str`, optional): Matching environmental layers
                will have this environmental layer type identifier.
            gcm_code (:obj:`str`, optional): Matching environmental layers
                will have this GCM code.
            scenario_id (:obj:`int`, optional): Matching environmental layers
                will belong to the Lifemapper scenario specified by this
                identifier.
            limit (:obj:`int`, optional): Return, at most, this many
                environmental layers.
            offset (:obj:`int`, optional): Offset the returned environmental
                layers by this amount.  Useful for paging.

        Returns:
            list of dicts - A list of environmental layer dictionary objects
                with metadata about each one.  The response format is JSON.
        """
        return RestService.list(
            self, self.end_point, after_time=after_time,
            alt_pred_code=alt_pred_code, before_time=before_time,
            date_code=date_code, epsg_code=epsg_code, env_code=env_code,
            env_type_id=env_type_id, gcm_code=gcm_code,
            scenario_id=scenario_id, limit=limit, offset=offset)
