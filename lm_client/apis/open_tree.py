"""Wrapper for the Lifemapper Open Tree service wrapper.
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class OpenTreeApiService(RestService):
    """Service wrapper for the Lifemapper Open Tree service wrapper.
    """
    end_point = 'api/v2/opentree'

    # ...........................
    def post(self, taxon_ids):
        """Retrieves open tree information for a list of taxon ids.
        """
        return RestService.post(
            self, self.end_point, data=json.dumps(taxon_ids),
            headers={'Content-Type': 'application/json'})
