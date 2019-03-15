"""
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class GbifNameParserApiService(RestService):
    """
    """
    end_point = 'api/v2/gbifparser'

    # ...........................
    def post(self, names_list, raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw, body=json.dumps(names_list),
            headers={'Content-Type' : 'application/json'})
