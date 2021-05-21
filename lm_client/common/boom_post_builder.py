"""This module contains functions for building BOOM POSTs.

"BOOM POST" is a Lifemapper term for posting larger experiments at once.  These
experiments can include occurrence CSV files with multiple species as well as multiple
scenarios for SDM projection.  They can also include multi-species analyses in the
form of Presence Absence Matrix (PAM) statistics and metacommunity phylogenetics
analyses and any new multi-species analyses and/or statistics that we add in the
future.
"""
import json


# .....................................................................................
class BoomPostGenerator:  # pragma: no cover
    """Tool for generating BOOM posts."""
    # ................................
    def __init__(self, archive_name):
        """Construct the base generator.

        Args:
            archive_name (str): A name for this experiment.
        """
        self.archive_name = archive_name
        self.shapegrid = None
        self.intersect_parameters = None
        self.mcpa = None
        self.occurrence = None
        self.pam_stats = None
        self.scenario_package = None
        self.sdm = None
        self.tree = None

    # ................................
    def add_algorithm(self, algorithm_code, parameters=None):
        """Adds an algorithm to the configuration.

        Args:
            algorithm_code (str): The code for the algorithm being added.
            parameters (list of tuples): A list of algorithm parameter tuples where the
                first element is the parameter name and the second is the value.
        """
        if self.sdm is None:
            self.sdm = {}
        if 'algorithm' not in self.sdm.keys():
            self.sdm['algorithm'] = []
        parameters = {}
        if parameters is not None:
            for name, val in parameters:
                parameters[name] = val
        alg = {
            'code': algorithm_code,
            'parameters': parameters
        }
        self.sdm['algorithm'].append(alg)

    # ................................
    def add_hull_region_intersect_mask(self, region_layer_name, buffer):
        """Adds the hull region intersect masking method to the configuration.

        Args:
            region_layer_name (str): The region layer in the scenario to use for
                masking.
            buffer (number): A buffer distance in map units for the mask.
        """
        if self.sdm is None:
            self.sdm = {}
        self.sdm['hull_region_intersect_mask'] = {
            'buffer': buffer,
            'region': region_layer_name
        }

    # ................................
    def add_scenario_package(
        self,
        package_name,
        model_scenario_code=None,
        projection_scenario_codes=None
    ):
        """Adds scenario package to the post.

        Args:
            package_name (str): The nmae of the scenario package.
            model_scenario_code (str): The scenario code of the modeling climate
                scenario.
            projection_scenario_codes (list of str): A list of scenario codes for the
                projecting climate scenarios.
        """
        self.scenario_package = {
            'scenario_package_filename': package_name
        }
        if model_scenario_code is not None:
            self.scenario_package['model_scenario'] = {
                'scenario_code': model_scenario_code
            }
        if projection_scenario_codes is not None:
            self.scenario_package['projection_scenario'] = [
                {
                    'scenario_code': prj_code
                } for prj_code in projection_scenario_codes]

    # ................................
    def add_occurrence_sets(
        self,
        points_filename=None,
        delimiter=None,
        occurrence_ids=None,
        taxon_ids=None,
        taxon_names=None,
        point_count_min=None
    ):
        """Adds occurrence data to the post.

        Args:
            points_filename (str): A file containing occurrence data.
            delimiter (str): If using `points_filename`, this is the field delimiter.
            occurrence_ids (list of int): A list of occurrence set identifiers to use.
            taxon_ids (list of int): A list of GBIF taxon ids to use for sdms.
            taxon_names (list of str): A list fo taxonomic names to use for sdms.
            point_count_min (int): The minimum number of points required to create a
                model for an occurrence set.
        """
        # TODO: Document
        # TODO: Check if inputs are valid
        self.occurrence = {}
        if points_filename is not None:
            self.occurrence['points_filename'] = points_filename
            if delimiter is not None:
                self.occurrence['delimiter'] = delimiter
        elif occurrence_ids is not None:
            self.occurrence['occurrence_ids'] = occurrence_ids
        elif taxon_ids is not None:
            self.occurrence['taxon_ids'] = taxon_ids
        elif taxon_names is not None:
            self.occurrence['taxon_names'] = taxon_names
        if point_count_min is not None:
            self.occurrence['point_count_min'] = point_count_min

    # ................................
    def add_mcpa(self, hypothesis_package_name):
        """Adds MCPA configuration to the boom post.

        Args:
            hypothesis_package_name (str): The hypothesis package name to add to the
                experiment.
        """
        self.mcpa = {
            'compute_mcpa': 1,
            'hypotheses_package_name': hypothesis_package_name
        }

    # ................................
    def add_pam_stats(self):
        """Adds pam stats configuration to the boom post."""
        self.pam_stats = {
            'compute_pam_stats': 1
        }

    # ................................
    def add_shapegrid(self, shapegrid_id=None, name=None, epsg=None,
                      min_x=None, min_y=None, max_x=None, max_y=None,
                      resolution=None, cell_sides=None, map_units=None,
                      cutout=None):
        """Add a shapegrid configuration to the boom post.

        A shapegrid is a regularly spaced grid of polygonal cells that will be
        the "sites" for multi-species analyses.  They may either be square or
        hexagonal cells.

        Notes:
            Either the identifier for an existing shapegrid (shapegrid_id) or parameters
                for creating a new shapegrid (name, epsg, min_x, min_y, max_x, max_y,
                resolution, cell_sides, map_units) must be provided.

        Args:
            shapegrid_id (:obj:`int`, optional): The identifier of an existing
                shapegrid to use in the post.
            name (:obj:`str`, optional): A name for a new shapegrid.
            epsg (:obj:`int`, optional): The EPSG code for the map projection
                to use for this new shapegrid.
            min_x (:obj:`float`, optional): The minimum value of X for the new
                shapegrid, in map_units.
            min_y (:obj:`float`, optional): The minimum value of Y for the new
                shapegrid, in map_units.
            max_x (:obj:`float`, optional): The maximum value of X for the new
                shapegrid, in map_units.
            max_y (:obj:`float`, optional): The maximum value of Y for the new
                shapegrid, in map_units.
            resolution (:obj:`float`, optional): The size of each of the cells,
                in map_units, for the new shapegrid.
            cell_sides (:obj:`int`, optional): The number of sides for each
                cell in the new shapegrid.  4 - squares, 6 - hexagons.
            map_units (:obj:`str`, optional): The units for the map
                measurements of the new shapegrid, options are: feet, inches,
                kilometers, meters, miles, dd, ds.
            cutout (:obj:`str`, optional): A Well-Known Text string for a
                polygon to use as a "cut out" for the new shapegrid.  Any cells
                that are within this polygon will be removed from the final
                shapegrid.
        """
        self.shapegrid = {}
        if shapegrid_id is not None:
            self.shapegrid['id'] = shapegrid_id
        else:
            # TODO: Make sure parameters are present
            self.shapegrid['name'] = name
            self.shapegrid['epsg'] = epsg
            self.shapegrid['minx'] = min_x
            self.shapegrid['miny'] = min_y
            self.shapegrid['maxx'] = max_x
            self.shapegrid['maxy'] = max_y
            self.shapegrid['resolution'] = resolution
            self.shapegrid['cell_sides'] = cell_sides
            self.shapegrid['map_units'] = map_units
            if cutout is not None:
                self.shapegrid['cutout_wkt'] = cutout

    # ................................
    def add_intersect_parameters(
        self,
        min_presence,
        max_presence,
        value_name,
        min_percent
    ):
        """Adds intersect parameters for creating a PAM from SDMs or layers.

        Args:
            min_presence (int): The minimum value that should be considered
                "present".
            max_presence (int): The maximum value that should be considered
                "present".
            value_name (str): The layer value to use for presence / absence.
                Use 'pixel' for raster layers.
            min_percent (int): The minimum percentage of a shapegrid cell
                classified as present to consider the entire cell present.
        """
        self.intersect_parameters = {
            'min_presence': min_presence,
            'max_presence': max_presence,
            'value_name': value_name,
            'min_percent': min_percent
        }

    # ................................
    def generate_request(self):
        """Generates a request JSON string for BOOM POSTs.

        Returns:
            str: A stringified version of the JSON object for the request.
        """
        req = {
            'archive_name': self.archive_name
        }
        if self.intersect_parameters is not None \
                and self.shapegrid is not None:
            req['global_pam'] = {
                'shapegrid': self.shapegrid,
                'intersect_parameters': self.intersect_parameters
            }

        # MCPA
        if self.mcpa is not None:
            req['mcpa'] = self.mcpa

        # Occurrence
        if self.occurrence is not None:
            req['occurrence'] = self.occurrence

        # PAM stats
        if self.pam_stats is not None:
            req['pam_stats'] = self.pam_stats

        # Scenario package
        if self.scenario_package is not None:
            req['scenario_package'] = self.scenario_package

        # SDM
        if self.sdm is not None:
            req['sdm'] = self.sdm

        # Tree
        if self.tree is not None:
            req['tree'] = self.tree

        return json.dumps(req)
