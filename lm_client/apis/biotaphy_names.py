"""Module containing functions for using the biotaphy names service end-point
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class BiotaPhyNamesApiService(RestService):
    """
    """
    end_point = 'api/v2/biotaphynames'

    # ...........................
    def post(self, names_list, raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw, body=json.dumps(names_list),
            headers={'Content-Type' : 'application/json'})
