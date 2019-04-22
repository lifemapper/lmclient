"""Tests the taxonomy service end-point
"""
import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_taxonomy_api_service(object):
    """This class tests the taxonomy service.
    """
    # ...........................
    def test_list_no_parameters(self, client_generator):
        """Tests list without providing any parameters.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            taxs = cl.taxonomy.list()
            assert len(taxs) >= 0

    # ...........................
    def test_drill_down(self, client_generator):
        """Tests list by drilling down using first entry for data.

        Args:
            client_generator (ClientGetter): Object used to get a client.
        """
        with client_generator.get_client() as cl:
            taxs = cl.taxonomy.list()
            assert len(taxs) > 0
            test_taxon = taxs[0]
            t_kingdom = test_taxon['taxon_kingdom']
            t_phylum = test_taxon['taxon_phylum']
            t_class = test_taxon['taxon_class']
            t_order = test_taxon['taxon_order']
            t_family = test_taxon['taxon_family']
            t_genus = test_taxon['taxon_genus']
            sp_name = test_taxon['scientific_name']

            kingdom_list = cl.taxonomy.list(taxon_kingdom=t_kingdom)
            assert len(kingdom_list) <= len(taxs)
            phylum_list = cl.taxonomy.list(
                taxon_kingdom=t_kingdom, taxon_phylum=t_phylum)
            assert len(phylum_list) <= len(kingdom_list)
            class_list = cl.taxonomy.list(
                taxon_kingdom=t_kingdom, taxon_phylum=t_phylum,
                taxon_class=t_class)
            assert len(class_list) <= len(phylum_list)
            order_list = cl.taxonomy.list(
                taxon_kingdom=t_kingdom, taxon_phylum=t_phylum,
                taxon_class=t_class, taxon_order=t_order)
            assert len(order_list) <= len(class_list)
            family_list = cl.taxonomy.list(
                taxon_kingdom=t_kingdom, taxon_phylum=t_phylum,
                taxon_class=t_class, taxon_order=t_order,
                taxon_family=t_family)
            assert len(family_list) <= len(order_list)
            genus_list = cl.taxonomy.list(
                taxon_kingdom=t_kingdom, taxon_phylum=t_phylum,
                taxon_class=t_class, taxon_order=t_order,
                taxon_family=t_family, taxon_genus=t_genus)
            assert len(genus_list) <= len(family_list)
            # species_list = cl.taxonomy.list(
            #    taxon_kingdom=t_kingdom, taxon_phylum=t_phylum,
            #    taxon_class=t_class, taxon_order=t_order,
            #    taxon_family=t_family, taxon_genus=t_genus,
            #    scientific_name=sp_name)
            # assert len(species_list) <= len(genus_list)
            # Check that there is at least the one original record
            # assert len(species_list) >= 1
            assert len(genus_list) >= 1
