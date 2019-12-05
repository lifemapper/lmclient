"""Wrapper for the BiotaPhy point count web service.
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class BiotaPhyPointsApiService(RestService):
    """BiotaPhy point count web service wrapper.
    """
    end_point = 'api/v2/biotaphypoints'

    # ...........................
    def post(self, taxon_ids):
        """Retrieve iDigbio point counts for a list of taxon ids.

        Args:
            taxon_ids (:obj:list of :obj:int): A list of taxon ids.

        Returns:
            list of dicts:
                A list of dictionary objects with 'taxon_id' and 'count' keys.
        """
        return RestService.post(
            self, self.end_point, data=json.dumps(taxon_ids),
            headers={'Content-Type': 'application/json'})
