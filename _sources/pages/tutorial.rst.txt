========
Tutorial
========

This tutorial provides some examples for performing basic tasks using the
Lifemapper service APIs via the client library.

.. toctree::
    :maxdepth: 1
    :caption: Contents:

----

Create a client instance and authenticate
=========================================
The first task you will need to perform is to create an instance and you will
most likely want to authenticate.

  ::

    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')

----

Upload Data
===========
For experiments using your own data, you will first need to upload those data
objects.  See `upload docs <../source/lm_client.apis.html#module-lm_client.apis.upload>`_.

Upload biogeographic hypotheses
-------------------------------
Biogeographic hypotheses are a collection of shapefiles representing historical
biogeography that may potentially effect distribution of species.  These
uploads should be zipped together into one file and each hypothesis should have
an additional JSON metadata file describing the hypothesis that has the same
name as the other files for the shapefile but with a .json extension.  The file
should be in the format::

    {
        “description” : “A description of the hypothesis”,
        “author” : “The author of the shapefile”,
        “title” : “A title of this hypothesis”,
        “citation” : “A citation if applicable”,
        “bbox” : [min x, min y, max x, max y]
    }


::

    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> cl.upload.biogeographic_hypotheses(hypothesis_zip_filename, 'my_hypotheses')


Upload occurrence data
----------------------
Occurrence data uploads are single CSV files with occurrence points for one or
more species.  The occurrences for each species should be grouped together in
contiguous lines.  Along with the CSV file, JSON metadata describing it should
be uploaded as well.  This metadata file should be in the following format
(found at: http://lifemapper.github.io/api.html?url=/assets/yaml/lmV2.yml#/definitions/OccurrenceMetadata::
    {
        "field" : [
            {
                "key" : "string", # The original name in the CSV header, or column index (zero-based)
                "shortName" : "10charname", # Short name for the field, 10 characters or less
                "fieldType" : "type" # Type of the field (integer, real, string)
            }
        ],
        "role" : {
            "groupBy" : "taxon", # Field used to group data
            "latitude" : "lat", # Field representing latitude
            "longitude" : "long", # Field representing longitude
            "taxaName" : "taxon", # Field with taxon information
            "uniqueId" : "id"  # Field representing unique id for each occurrence
        },
        "delimiter" : "," # Delimiter between fields in each line
    }


::

    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> cl.upload.occurrence(my_occurrence_csv_filename, occ_metadata_json_filename, 'my_occ_data')


Upload a phylogenetic tree
--------------------------
For many multi-species analyses, you will need a phylogenetic tree.  This call
allows you to upload a tree that you have locally.  Note that there are other
options for retrieving a phylogenetic tree from Open Tree of Life in your
experiment.  Trees should be in Newick, Nexus, or PhyloXML format.

::

    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> cl.upload.tree(my_tree_filename, 'my_tree_name')

----

Get a SDM projection map
========================
If you generate SDMs but do not plan on downloading the entire output package
or if you want to just show singular maps, you can use the OGC service endpoint
to retrieve a map.

::

    >>> prj_id = 1234
    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> prj_obj = cl.sdm_project.get(prj_id)
    >>> map_image = cl.ogc.get(prj_obj.map.mapName, bbox=prj.spatialRaster.bbox, color='ff0000', height=200, width=400, request='GetMap', format='image/png', version='1.1.0', layer=prj_obj.map.layerName, srs='EPSG:4326', service='WMS')

----

List completed SDM projections
==============================
You may want to retrieve a list of all SDM projections that have been computed
(status = 300).  You can use the sdm_projects list service to get those objects
for additional processing.

::

    >>> from lm_client.client.client import LmApiClient
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> completed_prjs = cl.sdm_project.list(status=300)

----

Submit a new experiment
=======================
One of the primary functions of the client library is to enable experiment
submission.  These experiments can vary quite a bit and for this example we
will upload an occurrence set, biogeographic hypotheses, and a tree and ask
that multi-species statistics, including MCPA, be generated.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> TAXA = ['Quercus ajoensis', 'Quercus alba', 'Quercus aliena', 'Quercus arizonica', 'Quercus austrina']
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> scn_package_id = cl.scenario_package.list(limit=1).id
    >>> scn_package_name = cl.scenario_package.get(scn_package_id).name
    >>> bpg = BoomPostGenerator('my_exp')
    >>> bpg.add_algorithm('ATT_MAXENT')
    >>> bpg.add_scenario_package(scn_package_name)
    >>> bpg.add_occurrence_sets(taxon_names=TAXA)
    >>> bpg.add_pam_stats()
    >>> bpg.add_shapegrid(name='my_grid', epsg=4326, min_x=-180, min_y=-90, max_x=180, max_y=90, resolution=1, cell_sides=4, map_units='dd')
    >>> bpg.add_intersect_parameters(10, 255, 'pixel', 25)
    >>> my_gs = cl.gridset.post(bpg.generate_request())

----

Download output package
=======================
After experiment submission and computation, you will probably want to retrieve
the generated package of outputs.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> gridset_id = 1234
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> gs_pkg = cl.gridset.get(gridset_id, interface='package')

----

Get accepted taxon ids from GBIF
================================
If you want to retrieve an Open Tree of Life tree, you will need to have
accepted GBIF taxonomy identifiers for the species to be included.  You can use
the service to get those.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> TAXA = ['Quercus ajoensis', 'Quercus alba', 'Quercus aliena', 'Quercus arizonica', 'Quercus austrina']
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> taxon_ids = cl.gbif_parser.post(TAXA)

----

Get an Open Tree of Life tree
=============================
If you have species data and want to run multi-species analyses that include
phylogenetic analyses, but you don't have a phylogenetic tree, you can retrieve
one from Open Tree of Life.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> TAXA = ['Quercus ajoensis', 'Quercus alba', 'Quercus aliena', 'Quercus arizonica', 'Quercus austrina']
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> taxon_ids = cl.gbif_parser.post(TAXA)
    >>> tree = cl.open_tree.post(taxon_ids)

----

Find Global PAM matches
=======================
If you wish to create a subset of a global PAM, you will likely want to first
see what that subset would include before performing the subset operation.  To
do that, you can see which entries match your specified query parameters.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> matches = cl.global_pam.list_matches(algorithm_code='ATT_MAXENT', gridset_id=123, taxon_genus='Quercus')

----

Subset a Global PAM
===================
Once you know which parameters you would like to use to subset the global PAM,
you can send a subset request to create a new gridset with data matching those
query parameters.

::

    >>> from lm_client.client.client import LmApiClient
    >>> from lm_client.common.boom_post_builder import BoomPostGenerator
    >>> cl = LmApiClient()
    >>> cl.auth.login('my_user', 'my_password')
    >>> my_gs = cl.global_pam.post_subset('my_subset', algorithm_code='ATT_MAXENT', gridset_id=123, taxon_genus='Quercus')

----
