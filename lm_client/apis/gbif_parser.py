"""Wrapper for the GBIF names parser service
"""
import json

from lm_client.common.api_service import RestService


# .............................................................................
class GbifNameParserApiService(RestService):
    """Wrapper class for the GBIF names parser service.
    """
    end_point = 'api/v2/gbifparser'

    # ...........................
    def post(self, names_list):
        """Retrieve GBIF taxon ids and accepted names for a species list.


        Args:
            names_list (:obj:list of :obj:str): A list of species names for
                which to retrieve accepted names and taxon ids.

        Returns:
            List of :obj:dict objects containing 'taxon_id', 'search_name',
                and 'accepted_name' keys for each species.
        """
        return RestService.post(
            self, self.end_point, data=json.dumps(names_list),
            headers={'Content-Type': 'application/json'})
