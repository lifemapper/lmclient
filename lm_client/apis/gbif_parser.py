"""Service wrapping the GBIF name parser."""
import json

from lm_client.common.api_service import RestService


# .....................................................................................
class GbifNameParserApiService(RestService):
    """Service wrapping the Lifemapper GBIF name parser endpoint."""
    end_point = 'api/v2/gbifparser'

    # ...........................
    def post(self, names_list):
        """Submit a request to get accepted names from a provided list of names.

        Args:
            names_list (list of str): A list of names to get the GBIF accepted names
                for, if they are available.

        Returns:
            dict: A dictionary (JSON) of name translation information.
        """
        return RestService.post(
            self,
            self.end_point,
            body=json.dumps(names_list),
            headers={'Content-Type': 'application/json'}
        )
