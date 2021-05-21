"""Module containing base class for API service calls."""
from lmclient.common.constants import INTERFACES
from lmclient.common.exceptions import raise_http_exception


# .....................................................................................
def format_object(response, interface):
    """Formats an object based on the interface provided.

    Args:
        response (requests.models.Response): A response object returned from a request.
        interface (str): An interface string that should be matched against
            those in the INTERFACES constants class.

    Raises:
        Exception: If the interface is unknown, an Exception is raised.

    Returns:
        dict: If the interface is a JSON interface, the response is encoded as a JSON
            dictionary object.
        str: If the interface is a text interface, the response is returned as text.
        bytes: If the interface is a binary interface, the response is returned as
            bytes.
    """
    if interface is None or interface.lower() in INTERFACES.json_interfaces():
        return response.json()
    elif interface.lower() in INTERFACES.text_interfaces():
        return response.text
    elif interface.lower() in INTERFACES.binary_interfaces():
        return response.content
    else:
        raise Exception('Unknown interface: {}'.format(interface))


# .....................................................................................
class ApiService(object):
    """Base class for API calls.

    Attributes:
        api_client (_Client): A client object used to make requests to a server.
    """
    # ...........................
    def __init__(self, api_client):
        """Constructor.

        Args:
            api_client (_Client): A client object to be used to make requests
                to a server.
        """
        self.api_client = api_client


# .....................................................................................
class RestService(ApiService):
    """Base class for RESTful API calls."""
    # ...........................
    def count(self, count_url, headers=None, **query_params):
        """Counts the number of objects matching the provided parameters.

        Args:
            count_url (str): A relative URL for counting objects.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters to be used
                as criteria for counting.

        Returns:
            int: The number of objects matching the specified criteria
        """
        response = self.api_client.get(
            count_url, headers=headers, **query_params)
        raise_http_exception(response)
        return format_object(response, INTERFACES.JSON)['count']

    # ...........................
    def delete(self, obj_url, headers=None, **query_params):
        """Sends a delete request to the specified URL.

        Args:
            obj_url (str): A relative URL for the object in question.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters to be sent
                along with the request.
        """
        response = self.api_client.delete(obj_url, headers=headers, **query_params)

        raise_http_exception(response)

    # ...........................
    def get(self, obj_url, interface=INTERFACES.JSON, headers=None, **query_params):
        """Gets the object in the format specified by 'interface'.

        Args:
            obj_url (str): The relative URL to the object.
            interface (:obj:`INTERFACES`, optional): The interface format to
                request for the object.
            headers (:obj:`dict`, optional): Any headers to be sent to the
                request.
            **query_params (dict): A dictionary of query parameters that may
                be used in object retrieval.

        Returns:
            dict: If the interface is a JSON interface, the response is
                encoded as a JSON dictionary object.
            str: If the interface is a text interface, the response is
                returned as text.
            bytes: If the interface is a binary interface, the response is
                returned as bytes.
        """
        if interface is not None:
            obj_url = '{}/{}'.format(obj_url, interface)
        response = self.api_client.get(
            obj_url, headers=headers, **query_params)
        raise_http_exception(response)
        return format_object(response, interface)

    # ...........................
    def list(self, list_url, headers=None, **query_params):
        """Lists the number of objects matching the provided parameters.

        Args:
            list_url (str): A relative URL for listing objects.
            headers (:obj:`dict`, optional): Any headers to be sent to the request.
            **query_params (dict): A dictionary of query parameters to be used as
                criteria for listing.

        Returns:
            list of dict: The list of matching objects is returned as a list of
                dictionaries.
        """
        response = self.api_client.get(list_url, headers=headers, **query_params)
        raise_http_exception(response)
        return format_object(response, INTERFACES.JSON)

    # ...........................
    def post(self, post_url, files=None, headers=None, **query_params):
        """Submits a POST request to the server.

        Args:
            post_url (str): A relative URL where the POST request will be made.
            files (:obj:`dict`, optional): A dictionary with file query parameter name
                keys and tuple values with (file name, open file-like object or string,
                and optionally a mime-type for the file).
            headers (:obj:`dict`, optional): Any headers to be sent to the request.
            **query_params (dict): A dictionary of query parameters to be sent with
                the POST request.

        Returns:
            dict: A JSON dictionary returned from the POST request
        """
        response = self.api_client.post(
            post_url, files=files, headers=headers, **query_params
        )
        raise_http_exception(response)
        return format_object(response, INTERFACES.JSON)
