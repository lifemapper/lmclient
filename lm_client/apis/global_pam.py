"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class GlobalPamApiService(RestService):
    """
    """
    end_point = 'api/v2/globalpam'

    # ...........................
    def get_facets(self):
        """Attempts to get

        Args:
        """
        return RestService.get(self, '{}/gridset'.format(self.end_point))

    # ...........................
    def list_matches(self, algorithm_code=None, bbox=None,
                     display_name=None, gridset_id=None,
                     model_scenario_code=None, point_max=None, point_min=None,
                     prj_scen_code=None, squid=None, taxon_kingdom=None,
                     taxon_phylum=None, taxon_class=None, taxon_order=None,
                     taxon_family=None, taxon_genus=None, taxon_species=None):
        """Gets a list

        Args:
        """
        return RestService.list(
            self, self.end_point, algorithm_code=algorithm_code, bbox=bbox,
            display_name=display_name, gridset_id=gridset_id,
            model_scenario_code=model_scenario_code, point_max=point_max,
            point_min=point_min, prj_scen_code=prj_scen_code, squid=squid,
            taxon_kingdom=taxon_kingdom, taxon_phylum=taxon_phylum,
            taxon_class=taxon_class, taxon_order=taxon_order,
            taxon_family=taxon_family, taxon_genus=taxon_genus,
            taxon_species=taxon_species)

    # ...........................
    def post_subset(self, archive_name, gridset_id, algorithm_code=None,
                    bbox=None, display_name=None, model_scenario_code=None,
                    point_max=None, point_min=None, prj_scen_code=None,
                    squid=None, taxon_kingdom=None, taxon_phylum=None,
                    taxon_class=None, taxon_order=None, taxon_family=None,
                    taxon_genus=None, taxon_species=None):
        """
        """
        return RestService.post(
            self, self.end_point, headers={'Content-Type': 'application/json'},
            archive_name=archive_name, gridset_id=gridset_id,
            algorithm_code=algorithm_code, bbox=bbox,
            display_name=display_name, model_scenario_code=model_scenario_code,
            point_max=point_max, point_min=point_min,
            prj_scen_code=prj_scen_code, squid=squid,
            taxon_kingdom=taxon_kingdom, taxon_phylum=taxon_phylum,
            taxon_class=taxon_class, taxon_order=taxon_order,
            taxon_family=taxon_family, taxon_genus=taxon_genus,
            taxon_species=taxon_species)
