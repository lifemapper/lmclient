"""Module containing base class for API service calls
"""
import json

from lm_client.common.constants import INTERFACES

def format_object(response, interface):
    """
    Todo: Actually determine how to format
    """
    return response.json()

# .............................................................................
class ApiService(object):
    """Base class for API calls
    """
    def __init__(self, api_client):
        self.api_client = api_client

# .............................................................................
class RestService(ApiService):
    """Base class for RESTful API calls
    """
    # ...........................
    def count(self, count_url, raw=False, headers=None, **query_params):
        """Counts the number of objects matching the provided parameters.

        Args:
            count_url (str): A relative URL for counting objects.
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters to be used
                as criteria for counting.
        """
        response = self.api_client.get(
            count_url, headers=headers, **query_params)
        if raw:
            return response
        else:
            return response.json()['count']

    # ...........................
    def delete(self, obj_url, raw=False, headers=None, **query_params):
        response = self.api_client.delete(
            obj_url, headers=headers, **query_params)
        if raw:
            return response
        else:
            return response.json()

    # ...........................
    def get(self, obj_url, raw=False, interface=INTERFACES.JSON,
            headers=None, **query_params):
        """Gets the object in the format specified by 'interface'.

        Args:
            obj_url (str): The relative URL to the object.
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, attempt to
                process the response.
            interface (:obj:`INTERFACES`, optional): The interface format to
                request for the object.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters that may
                be used in object retrieval.
        """
        if interface is not None:
            obj_url = '{}/{}'.format(obj_url, interface)
        response = self.api_client.get(
            obj_url, headers=headers, **query_params)
        if raw:
            return response
        else:
            return format_object(response, interface)

    # ...........................
    def list(self, list_url, raw=False, headers=None, **query_params):
        """Lists the number of objects matching the provided parameters.

        Args:
            list_url (str): A relative URL for listing objects.
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters to be used
                as criteria for listing.
        """
        response = self.api_client.get(
            list_url, headers=headers, **query_params)
        if raw:
            return response
        else:
            return response.json()

    # ...........................
    def post(self, post_url, raw=False, files=None, headers=None,
             **query_params):
        """
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
        """
        print('api service')
        print(query_params)
        response = self.api_client.post(
            post_url, files=files, headers=headers, **query_params)
        if raw:
            return response
        else:
            return response.json()
