"""This module contains exceptions that the client may throw
"""
from lm_client.common.constants import HttpStatus


# .............................................................................
class HttpError(Exception):
    """Base class for HTTP Errors
    """
    code = None
    url = None

    # ...........................
    def __init__(self, url):
        err_msg = 'HTTP Error: {} ({}) for {}'.format(
            self.code, self.message, url)
        super(Exception, self).__init__(err_msg)
        self.url = url


# .............................................................................
class BadRequestError(HttpError):
    """Exception thrown when there is a problem with the request provided
    """
    code = HttpStatus.BAD_REQUEST
    message = 'Bad Request'


# .............................................................................
class ConflictError(HttpError):
    """Exception thrown when there is a conflict posting data

    Note:
        * This often occurs if a file with the same name already exists
    """
    code = HttpStatus.CONFLICT
    message = 'Conflict'


# .............................................................................
class ForbiddenError(HttpError):
    """Exception thrown when the user does not have access to an object
    """
    code = HttpStatus.FORBIDDEN
    message = 'Forbidden'


# .............................................................................
class NotFoundError(Exception):
    """Exception thrown when the requested object was not found
    """
    code = HttpStatus.NOT_FOUND
    message = 'Not found'


# .............................................................................
def raise_http_exception(response):
    """Look at the status_code of the response and throw the proper exception
    """
    if response.status_code == HttpStatus.BAD_REQUEST:
        raise BadRequestError(response.url)
    elif response.status_code == HttpStatus.FORBIDDEN:
        raise ForbiddenError(response.url)
    elif response.status_code == HttpStatus.NOT_FOUND:
        raise NotFoundError(response.url)
