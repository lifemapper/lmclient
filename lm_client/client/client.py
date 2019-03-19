"""Module containing the Lifemapper web service client

Todo:
    * Singleton?
    * Save session?
    * Acceptable versions?
"""
import requests
#import urllib
#import urllib2

from lm_client.apis.auth import AuthApiService
from lm_client.apis.biotaphy_names import BiotaPhyNamesApiService
from lm_client.apis.biotaphy_points import BiotaPhyPointsApiService
from lm_client.apis.env_layer import EnvLayerApiService
from lm_client.apis.gbif_parser import GbifNameParserApiService
from lm_client.apis.global_pam import GlobalPamApiService
from lm_client.apis.gridset import GridsetApiService
from lm_client.apis.hint import SpeciesHintApiService
from lm_client.apis.layer import LayerApiService
from lm_client.apis.occurrence import OccurrenceApiService
from lm_client.apis.ogc import OgcApiService
from lm_client.apis.open_tree import OpenTreeApiService
from lm_client.apis.raw_solr import SolrRawApiService
from lm_client.apis.scenario import ScenarioApiService
from lm_client.apis.scenario_package import ScenarioPackageApiService
from lm_client.apis.sdm_project import SdmProjectApiService
from lm_client.apis.shapegrid import ShapegridApiService
from lm_client.apis.snippet import SnippetApiService
from lm_client.apis.taxonomy import TaxonomyApiService
from lm_client.apis.upload import UploadApiService
from lm_client.apis.tree import TreeApiService
from lm_client.common.constants import HTTPMethod

# .............................................................................
class _Client(object):
    """Base client class for communicating with a server.

    Attributes:
        __version__ (str): The version of this client.
        UA_STRING (str): The User-Agent string this client sends to a server.
        server (str): The base URL for a desired server.
    """
    __version__ = '4.0.0'
    UA_STRING = ' '.join([
        'lm_client/{}'.format(__version__),
        '(Lifemapper Python Client Library;',
        'http://lifemapper.org; lifemapper@ku.edu)'])

    # ...........................
    def __init__(self, server):
        """Constructor.

        Args:
            server (str): The base URL for a desired server to use.
        """
        self.server = server
    
    # ...........................
    def _get_url(self, relative_url, query_parameter_str=None):
        """Gets a full URL for a request.

        relative_url (str): A relative URL (after server root).
        query_parameter_str (:obj:`str`, optional): If provided, this is the
            query parameter portion of the URL (after the '?').

        Returns:
            str: A URL string for a request.
        """
        url = '{}/{}'.format(self.server, relative_url)

        if query_parameter_str is not None:
            url = '{}?{}'.format(url, query_parameter_str)

        return url

    # ...........................
    def _make_url(self, relative_url):
        return '{}/{}'.format(self.server, relative_url)
    
#     # ...........................
#     def _make_request(self, relative_url, method=HTTPMethod.GET, body=None,
#                      headers=None, **query_parameters):
#         """Submits a request to the server and returns an open file-like object
# 
#         Args:
#             relative_url (str): The relative URL (after the server root) for
#                 this request.
#             method (:obj:`HTTPMethod`, optional): The HTTP method to use for
#                 this request (default is 'GET').
#             body (:obj:`str`, optional): If provided, this will be the body of
#                 the request.
#             headers (:obj:`dict` or :obj:`None`): If not None, this should be
#                 a dictionary of headers.
#             query_parameters (dict): Any additional optional parameters set to
#                 this function will be wrapped as query parameters for the
#                 request.
# 
#         Returns:
#             An open file-like object representing the response from the server.
#         """
#         payload = dict(query_parameters)
#         if headers is None:
#             headers = {}
#         
#         try:
#             # Get a list of all non-None query parameters
#             q_params = [
#                 (k, v) for (k, v) in dict(
#                     query_parameters).items() if v is not None]
#             url_params = urllib.urlencode(q_params)
#     
#             if body is not None and len(
#                 q_params) > 0 and method == HTTPMethod.POST:
#     
#                 body = url_params
#                 url = self._get_url(relative_url)
#             else:
#                 url = self._get_url(relative_url, query_parameter_str=url_params)
#     
#             if headers is None:
#                 headers = {}
#     
#             req = urllib2.Request(url, data=body, headers=headers)
#             print req.__dict__
#             req.get_method = lambda: method.upper()
#     
#             return urllib2.urlopen(req)
#         except Exception as e:
#             print('The failed URL was: {}'.format(url))
#             print('Error: {}'.format(e))
#             print('{}'.format(e.__dict__))
#             raise e

    # ...........................
    def delete(self, relative_url, headers=None):
        return requests.delete(self._make_url(relative_url), headers=headers)

    # ...........................
    def get(self, relative_url, headers=None, **query_parameters):
        return requests.get(
            self._make_url(relative_url), params=dict(query_parameters),
            headers=headers)

    # ...........................
    def post(self, relative_url, files=None, headers=None, **query_parameters):
        """
        Files should be 'name' : (file name, content, header (optional))
        """
        print('in client post')
        print(str(query_parameters))
        if files is not None:
            return requests.post(
                self._make_url(relative_url), headers=headers,
                params=query_parameters, files=files)
        else:
            return requests.post(
                self._make_url(relative_url), headers=headers,
                data=query_parameters)

    # ...........................
    # put

# .............................................................................
class LmApiClient(object):
    """A Lifemapper API Client object used to make service requests.
    """
    def __init__(self):
        self._client = _Client('http://notyeti-193.lifemapper.org')
        
        self.auth = AuthApiService(self._client)
        self.biotaphy_names = BiotaPhyNamesApiService(self._client)
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
