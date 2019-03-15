"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class SpeciesHintApiService(RestService):
    """
    """
    end_point = 'api/v2/hint'

    # ...........................
    def list(self, search_string, raw=False, limit=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(self,
            '{}/{}'.format(self.end_point, search_string), raw=raw,
            limit=limit)
