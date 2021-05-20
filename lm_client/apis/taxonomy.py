"""This module contains functions for getting taxonomy hints."""
from lm_client.common.api_service import RestService


# .............................................................................
class TaxonomyApiService(RestService):
    """Class for accessing the taxonomy hint endpoint."""
    end_point = 'api/v2/taxonomy'

    # ...........................
    def list(self, canonical_name=None, limit=None, scientific_name=None,
             squid=None, taxon_class=None, taxon_family=None, taxon_genus=None,
             taxon_key=None, taxon_kingdom=None, taxon_order=None,
             taxon_phylum=None, user=None):
        """Gets a list of taxonomy matches.

        Args:
            canonical_name (:obj:`str`, optional): Return matches that have this
                canonical name.
            limit (:obj:`int`, optional): The maximum number of matches to return with
                this request.
            scientific_name (:obj:`str`, optional): Return matches with this scientific
                name.
            squid (:obj:`str`, optional): Return matches that have this hashed-based
                species identifier.
            taxon_class (:obj:`str`, optional): Return matches that have this taxonomic
                class.
            taxon_family (:obj:`str`, optional): Return matches that have this
                taxonomic family.
            taxon_genus (:obj:`str`, optional): Return matches that belong to this
                genus.
            taxon_key (:obj:`int`, optional): Return matches for this GBIF taxonomic
                key.
            taxon_kingdom (:obj:`str`, optional): Return matches that belong to this
                taxonomic kingdom.
            taxon_order (:obj:`str`, optional): Return matches belonging to this
                taxonomic order.
            taxon_phylum (:obj:`str`, optional): Return matches belonging to this
                phylum.
            user (:obj:`str`, optional): Return matches for this user.

        Returns:
            List of dict: A list of taxonomy dictionaries matching the provided
                parameters
        """
        return RestService.list(
            self,
            self.end_point,
            canonical_name=canonical_name,
            limit=limit,
            scientific_name=scientific_name,
            squid=squid,
            taxon_class=taxon_class,
            taxon_family=taxon_family,
            taxon_genus=taxon_genus,
            taxon_key=taxon_key,
            taxon_kingdom=taxon_kingdom,
            taxon_order=taxon_order,
            taxon_phylum=taxon_phylum,
            user=user
        )
