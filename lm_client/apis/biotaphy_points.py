"""Service for accessing the Biotaphy points endpoint."""
import json

from lm_client.common.api_service import RestService


# .....................................................................................
class BiotaPhyPointsApiService(RestService):
    """Class for accessing the Biotaphy points endpoint."""
    end_point = 'api/v2/biotaphypoints'

    # ...........................
    def post(self, taxon_ids):
        """Get points for the provided taxon identifiers.

        Args:
            taxon_ids (list): A list of taxonomic identifiers to get points for.

        Returns:
            dict: A dictionary (JSON) of metadata about the points request.
        """
        return RestService.post(
            self,
            self.end_point,
            body=json.dumps(taxon_ids),
            headers={'Content-Type': 'application/json'}
        )
