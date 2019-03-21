"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class SolrRawApiService(RestService):
    """
    """
    end_point = 'api/v2/rawsolr'

    # ...........................
    def post(self, collection, query_string):
        """
        """
        return RestService.post(
            self, self.end_point,
            body=json.dumps(
                {'collection': collection, 'query_string': query_string}),
            headers={'Content-Type': 'application/json'})
