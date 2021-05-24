"""Module containing the Lifemapper web service client."""
import requests

from lmclient.common.constants import API_SERVER
from lmclient.apis.auth import AuthApiService
from lmclient.apis.biotaphy_points import BiotaPhyPointsApiService
from lmclient.apis.env_layer import EnvLayerApiService
from lmclient.apis.gbif_parser import GbifNameParserApiService
from lmclient.apis.global_pam import GlobalPamApiService
from lmclient.apis.gridset import GridsetApiService
from lmclient.apis.hint import SpeciesHintApiService
from lmclient.apis.layer import LayerApiService
from lmclient.apis.occurrence import OccurrenceApiService
from lmclient.apis.ogc import OgcApiService
from lmclient.apis.open_tree import OpenTreeApiService
from lmclient.apis.raw_solr import SolrRawApiService
from lmclient.apis.scenario import ScenarioApiService
from lmclient.apis.scenario_package import ScenarioPackageApiService
from lmclient.apis.sdm_project import SdmProjectApiService
from lmclient.apis.shapegrid import ShapegridApiService
from lmclient.apis.snippet import SnippetApiService
from lmclient.apis.taxonomy import TaxonomyApiService
from lmclient.apis.upload import UploadApiService
from lmclient.apis.tree import TreeApiService


# .....................................................................................
class _Client:
    """Base client class for communicating with a server.

    Attributes:
        __version__ (str): The version of this client.
        UA_STRING (str): The User-Agent string this client sends to a server.
        server (str): The base URL for a desired server.
    """
    __version__ = '2.0.0'
    UA_STRING = ' '.join([
        'lmclient/{}'.format(__version__),
        '(Lifemapper Python Client Library;',
        'http://lifemapper.org; lifemapper@ku.edu)'])
    client_headers = {'User-Agent': UA_STRING}

    # ...........................
    def __init__(self, server):
        """Constructor.

        Args:
            server (str): The base URL for a desired server to use.
        """
        self.server = server
        self.session = requests.Session()

    # ...........................
    def _get_headers(self, request_headers):
        """Merges request headers with client default headers.

        Args:
            request_headers (:obj:`dict` or :obj:`None`): A dictionary of
                headers to be sent to the specific request.

        Returns:
            dict: A merged dictionary of request headers.
        """
        if request_headers is None:
            request_headers = {}
        for header_name in self.client_headers.keys():
            # Don't override existing headers
            if header_name not in request_headers.keys():
                request_headers[header_name] = self.client_headers[header_name]
        return request_headers

    # ...........................
    def _make_url(self, relative_url):
        """Assembles the full (base) URL for a request.

        Args:
            relative_url (str): The relative URL from the server root.

        Returns:
            str: A URL string
        """
        return '{}/{}'.format(self.server, relative_url)

    # ...........................
    def delete(self, relative_url, headers=None, **query_parameters):
        """Sends a HTTP DELETE request to a URL.

        Args:
            relative_url (str): The relative URL from the server root.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_parameters (dict): A dictionary of query parameters to be sent
                with the request.

        Returns:
            requests.models.Response - The response object generated from the
                request.
        """
        return self.session.delete(
            self._make_url(relative_url), headers=self._get_headers(headers),
            params=dict(query_parameters))

    # ...........................
    def get(self, relative_url, headers=None, **query_parameters):
        """Sends a HTTP GET request to a URL.

        Args:
            relative_url (str): The relative URL from the server root.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_parameters (dict): A dictionary of query parameters to be sent
                with the request.

        Returns:
            requests.models.Response - The response object generated from the
                request.
        """
        return self.session.get(
            self._make_url(relative_url), params=dict(query_parameters),
            headers=self._get_headers(headers))

    # ...........................
    def post(
        self,
        relative_url,
        files=None,
        headers=None,
        body=None,
        **query_parameters
    ):
        """Sends an HTTP POST request to a URL.

        Args:
            relative_url (str): The relative URL from the server root.
            files (:obj:`dict`, optional): Keys should be file query parameter
                names and values should be tuples of (file name, content,
                content-type (optional)).
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            body (object): Data to send as the data body of the request.
            **query_parameters (dict): A dictionary of query parameters to be sent
                with the request.

        Returns:
            requests.models.Response - The response object generated from the
                request.
        """
        if files is not None:
            return self.session.post(
                self._make_url(relative_url),
                headers=self._get_headers(headers), params=query_parameters,
                files=files)
        elif body is not None:
            return self.session.post(
                self._make_url(relative_url),
                headers=self._get_headers(headers), params=query_parameters,
                data=body)
        else:
            return self.session.post(
                self._make_url(relative_url),
                headers=self._get_headers(headers), data=query_parameters)


# .....................................................................................
class LmApiClient:
    """A Lifemapper API Client object used to make service requests.

    Attributes:
        auth (AuthApiService): Service end-point for authentication requests.
        biotaphy_points (BiotaPhyPointsApiService): Service end-point for
            querying the available data counts from iDigBio for a group of
            species.
        env_layer (EnvLayerApiService): Service end-point for environmental
            layer requests.
        gbif_parser (GbifNameParserApiService): Service end-point for searching
            for accepted taxon names for provided species names.
        global_pam (GlobalPamApiService): Service end-point for querying and
            subsetting global PAMs.
        gridset (GridsetApiService): Service end-point for making gridset
            related requests.
        hint (SpeciesHintApiService): Service end-point for searching for
            species with existing data on the server.
        layer (LayerApiService): Service end-point for making layer requests.
        occurrence (OccurrenceApiService): Service end-point for making
            occurrence set related requests.
        ogc (OgcApiService): Service end-point for making OGC requests to
            Lifemapper mapping services.
        open_tree (OpenTreeApiService): Service end-point for making requests
            to OpenTree APIs.
        raw_solr (SolrRawApiService): Service end-point for making raw Solr
            requests to the server.
        scenario (ScenarioApiService): Service end-point for scenario requests.
        scenario_package (ScenarioPackageApiService): Service end-point for
            scenario package requests.
        sdm_project (SdmProjectApiService): Service end-point for SDM
            projection requests.
        shapegrid (ShapegridApiService): Service end-point for shapegrid
            requests.
        snippet (SnippetApiService): Service end-point for snippet listings.
        taxonomy (TaxonomyApiService): Service end-point for taxonomy searches.
        tree (TreeApiService): Service end-point for tree requests.
        upload (UploadApiService): Service end-point for large file uploads.
    """
    # ...........................
    def __init__(self, server=API_SERVER):
        """Constructor for client instance.

        Args:
            server (str): The base URL of the API server.
        """
        self._client = _Client(server)

        self.auth = AuthApiService(self._client)
        self.biotaphy_points = BiotaPhyPointsApiService(self._client)
        self.env_layer = EnvLayerApiService(self._client)
        self.gbif_parser = GbifNameParserApiService(self._client)
        self.global_pam = GlobalPamApiService(self._client)
        self.gridset = GridsetApiService(self._client)
        self.hint = SpeciesHintApiService(self._client)
        self.layer = LayerApiService(self._client)
        self.occurrence = OccurrenceApiService(self._client)
        self.ogc = OgcApiService(self._client)
        self.open_tree = OpenTreeApiService(self._client)
        self.raw_solr = SolrRawApiService(self._client)
        self.scenario = ScenarioApiService(self._client)
        self.scenario_package = ScenarioPackageApiService(self._client)
        self.sdm_project = SdmProjectApiService(self._client)
        self.shapegrid = ShapegridApiService(self._client)
        self.snippet = SnippetApiService(self._client)
        self.taxonomy = TaxonomyApiService(self._client)
        self.tree = TreeApiService(self._client)
        self.upload = UploadApiService(self._client)
