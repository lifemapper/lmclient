"""Access the Lifemapper Raw Solr endpoint."""
import json

from lm_client.common.api_service import RestService


# .....................................................................................
class SolrRawApiService(RestService):
    """Class providing access to the Lifemapper Raw Solr endpoint."""
    end_point = 'api/v2/rawsolr'

    # ...........................
    def post(self, collection, query_string):
        """Submit a POST request to the Raw Solr endpoint.

        Args:
            collection (str): The Lifemapper Solr connection to connect to.
            query_string (str): The Solr query string to pass along.

        Returns:
            dict: A dictionary of Solr related content.
        """
        return RestService.post(
            self,
            self.end_point,
            body=json.dumps(
                {'collection': collection, 'query_string': query_string}
            ),
            headers={'Content-Type': 'application/json'})
