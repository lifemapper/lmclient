"""Wrapper around the Lifemapper occurrence set hint service."""
from lm_client.common.api_service import RestService


# .....................................................................................
class SpeciesHintApiService(RestService):
    """Class wrapping the Lifemapper hint service."""
    end_point = 'api/v2/hint'

    # ...........................
    def list(self, search_string, limit=None):
        """Gets a list of specie hint matches.

        Args:
            search_string (str): A partial string to match species names against.
            limit (int): The maximum number of results to return.

        Returns:
            list of strings: List of matching species.
        """
        return RestService.list(
            self,
            '{}/{}'.format(self.end_point, search_string),
            limit=limit
        )
