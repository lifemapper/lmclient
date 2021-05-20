"""Wrapper for the Lifemapper Global PAM endpoint."""
from lm_client.common.api_service import RestService


# .....................................................................................
class GlobalPamApiService(RestService):
    """Class wrapping the Lifemapper Global PAM service endpoint."""
    end_point = 'api/v2/globalpam'

    # ...........................
    def get_facets(self):
        """Attempts to get Global PAM facets.

        Returns:
            list of dict: A list of facets for the gridset.
        """
        return RestService.get(self, '{}/gridset'.format(self.end_point))

    # ...........................
    def list_matches(
        self,
        algorithm_code=None,
        bbox=None,
        display_name=None,
        gridset_id=None,
        model_scenario_code=None,
        point_max=None,
        point_min=None,
        prj_scen_code=None,
        squid=None,
        taxon_kingdom=None,
        taxon_phylum=None,
        taxon_class=None,
        taxon_order=None,
        taxon_family=None,
        taxon_genus=None,
        taxon_species=None
    ):
        """Gets a list of PAVs matching the provided parameters (subset dry run).

        Args:
            algorithm_code (str): The code of the modeling algorithm the PAVs should
                have been built from.
            bbox (tuple of number): A (min x, min y, max x, max y) bounding box to
                subset to.
            display_name (str): Match on this display name.
            gridset_id (int): The identifier of the gridset containing the PAVs.
            model_scenario_code (str): The scenario code of the PAV's model.
            point_max (int): The maximum number of points the PAV should be built from.
            point_min (int): The minimum number of points the PAV should be built from.
            prj_scen_code (str): A projection scenario code to match on.
            squid (str): A Lifemapper species identifier to match on.
            taxon_kingdom (str): A taxonomic kingdom to match on.
            taxon_phylum (str): A taxonomic phylum to match on.
            taxon_class (str): A taxonomic class to match on.
            taxon_order (str): A taxonomic order to match on.
            taxon_family (str): A family to match on.
            taxon_genus (str): A genus name to match on.
            taxon_species (str): A species name to match on.

        Returns:
            list of dict: A JSON list of matching PAV objects.
        """
        return RestService.list(
            self,
            self.end_point,
            algorithm_code=algorithm_code,
            bbox=bbox,
            display_name=display_name,
            gridset_id=gridset_id,
            model_scenario_code=model_scenario_code,
            point_max=point_max,
            point_min=point_min,
            prj_scen_code=prj_scen_code, squid=squid,
            taxon_kingdom=taxon_kingdom,
            taxon_phylum=taxon_phylum,
            taxon_class=taxon_class,
            taxon_order=taxon_order,
            taxon_family=taxon_family,
            taxon_genus=taxon_genus,
            taxon_species=taxon_species
        )

    # ...........................
    def post_subset(
        self,
        archive_name,
        gridset_id,
        algorithm_code=None,
        bbox=None,
        display_name=None,
        model_scenario_code=None,
        point_max=None,
        point_min=None,
        prj_scen_code=None,
        squid=None,
        taxon_kingdom=None,
        taxon_phylum=None,
        taxon_class=None,
        taxon_order=None,
        taxon_family=None,
        taxon_genus=None,
        taxon_species=None
    ):
        """Create a new subset using the query parameters to select PAVs.

        Args:
            archive_name (str): The name of the new subset archive.
            algorithm_code (str): The code of the modeling algorithm the PAVs should
                have been built from.
            bbox (tuple of number): A (min x, min y, max x, max y) bounding box to
                subset to.
            display_name (str): Match on this display name.
            gridset_id (int): The identifier of the gridset containing the PAVs.
            model_scenario_code (str): The scenario code of the PAV's model.
            point_max (int): The maximum number of points the PAV should be built from.
            point_min (int): The minimum number of points the PAV should be built from.
            prj_scen_code (str): A projection scenario code to match on.
            squid (str): A Lifemapper species identifier to match on.
            taxon_kingdom (str): A taxonomic kingdom to match on.
            taxon_phylum (str): A taxonomic phylum to match on.
            taxon_class (str): A taxonomic class to match on.
            taxon_order (str): A taxonomic order to match on.
            taxon_family (str): A family to match on.
            taxon_genus (str): A genus name to match on.
            taxon_species (str): A species name to match on.

        Returns:
            list of dict: A JSON list of matching PAV objects.
        """
        return RestService.post(
            self,
            self.end_point,
            headers={'Content-Type': 'application/json'},
            archive_name=archive_name,
            gridset_id=gridset_id,
            algorithm_code=algorithm_code,
            bbox=bbox,
            display_name=display_name,
            model_scenario_code=model_scenario_code,
            point_max=point_max,
            point_min=point_min,
            prj_scen_code=prj_scen_code,
            squid=squid,
            taxon_kingdom=taxon_kingdom,
            taxon_phylum=taxon_phylum,
            taxon_class=taxon_class,
            taxon_order=taxon_order,
            taxon_family=taxon_family,
            taxon_genus=taxon_genus,
            taxon_species=taxon_species
        )
