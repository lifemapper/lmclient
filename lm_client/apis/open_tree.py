"""API access for Lifemapper Open Tree of Life connection."""
import json

from lm_client.common.api_service import RestService


# .....................................................................................
class OpenTreeApiService(RestService):
    """Class for accessing the Open Tree endpoint exposed by Lifemapper."""
    end_point = 'api/v2/opentree'

    # ...........................
    def post(self, taxon_ids):
        """Submit a POST request to the Open Tree endpoint to get a tree from ids.

        Args:
            taxon_ids (list): A list of taxonomic identifiers established by GBIF.

        Returns:
            dict: A JSON dictionary of Open Tree response data.
        """
        return RestService.post(
            self,
            self.end_point,
            body=json.dumps(taxon_ids),
            headers={'Content-Type': 'application/json'}
        )
