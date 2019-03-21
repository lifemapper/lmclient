"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class SpeciesHintApiService(RestService):
    """
    """
    end_point = 'api/v2/hint'

    # ...........................
    def list(self, search_string, limit=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, '{}/{}'.format(self.end_point, search_string),
            limit=limit)
