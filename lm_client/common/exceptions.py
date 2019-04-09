"""This module contains exceptions that the client may throw
"""
from lm_client.common.constants import HttpStatus


# .............................................................................
class _HttpError(Exception):
    """Base class for HTTP Errors
    """
    code = None
    message = None
    url = None

    # ...........................
    def __init__(self, url):
        """Constructor.

        Note:
            * Should not be instantiated directly
        """
        if self.__class__ == _HttpError:
            raise RuntimeError(
                '_HttpError class should not be instantiated directly')
        err_msg = 'HTTP Error: {} ({}) for {}'.format(
            self.code, self.message, url)
        super(Exception, self).__init__(err_msg)
        self.url = url


# .............................................................................
class BadRequestError(_HttpError):
    """Exception thrown when there is a problem with the request provided.
    """
    code = HttpStatus.BAD_REQUEST
    message = 'Bad Request'


# .............................................................................
class ConflictError(_HttpError):
    """Exception thrown when there is a conflict posting data.

    Note:
        * This often occurs if a file with the same name already exists
    """
    code = HttpStatus.CONFLICT
    message = 'Conflict'


# .............................................................................
class ForbiddenError(_HttpError):
    """Exception thrown when the user does not have access to an object.
    """
    code = HttpStatus.FORBIDDEN
    message = 'Forbidden'


# .............................................................................
class InternalServerError(_HttpError):
    """Exception thrown when the server experiences an error during a request.
    """
    code = HttpStatus.INTERNAL_SERVER_ERROR
    message = 'Internal Server Error'


# .............................................................................
class MethodNotAllowedError(_HttpError):
    """Exception thrown when the requested HTTP method is not allowed.
    """
    code = HttpStatus.METHOD_NOT_ALLOWED
    message = 'Method not allowed'


# .............................................................................
class NotAcceptableError(_HttpError):
    """Exception thrown when cannot format in desired interface.
    """
    code = HttpStatus.NOT_ACCEPTABLE
    message = 'No acceptable format available'


# .............................................................................
class NotFoundError(_HttpError):
    """Exception thrown when the requested object was not found.
    """
    code = HttpStatus.NOT_FOUND
    message = 'Not found'


# .............................................................................
class ServiceUnavailableError(_HttpError):
    """Exception thrown when the requested service is unavailable.
    """
    code = HttpStatus.SERVICE_UNAVAILABLE
    message = 'Service Unavailable'


# .............................................................................
def raise_http_exception(response):
    """Look at the status_code of the response and throw the proper exception.
    """
    if response.status_code == HttpStatus.BAD_REQUEST:
        raise BadRequestError(response.url)
    elif response.status_code == HttpStatus.CONFLICT:
        raise ConflictError(response.url)
    elif response.status_code == HttpStatus.FORBIDDEN:
        raise ForbiddenError(response.url)
    elif response.status_code == HttpStatus.INTERNAL_SERVER_ERROR:
        raise InternalServerError(response.url)
    elif response.status_code == HttpStatus.METHOD_NOT_ALLOWED:
        raise MethodNotAllowedError(response.url)
    elif response.status_code == HttpStatus.NOT_ACCEPTABLE:
        raise NotAcceptableError(response.url)
    elif response.status_code == HttpStatus.NOT_FOUND:
        raise NotFoundError(response.url)
    elif response.status_code == HttpStatus.SERVICE_UNAVAILABLE:
        raise ServiceUnavailableError(response.url)
    elif response.status_code >= 500:
        raise Exception(
            'Unhandled service failure: {} - {}'.format(
                response.status_code, response.url))
    elif response.status_code >= 400:
        raise Exception(
            'Unhandled request failure: {} - {}'.format(
                response.status_code, response.url))
