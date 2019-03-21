"""This module contains functions for getting taxonomy hints
"""


from lm_client.common.api_service import RestService


# .............................................................................
class TaxonomyApiService(RestService):
    """
    """
    end_point = 'api/v2/taxonomy'

    # ...........................
    def list(self, canonical_name=None, limit=None, scientific_name=None,
             squid=None, taxon_class=None, taxon_family=None, taxon_genus=None,
             taxon_key=None, taxon_kingdom=None, taxon_order=None,
             taxon_phylum=None, user=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, self.end_point, canonical_name=canonical_name, limit=limit,
            scientific_name=scientific_name, squid=squid,
            taxon_class=taxon_class, taxon_family=taxon_family,
            taxon_genus=taxon_genus, taxon_key=taxon_key,
            taxon_kingdom=taxon_kingdom, taxon_order=taxon_order,
            taxon_phylum=taxon_phylum, user=user)
