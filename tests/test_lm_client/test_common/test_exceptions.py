"""This module tests the exceptions module."""
import pytest

from lmclient.common.constants import HttpStatus
import lmclient.common.exceptions as client_exceptions


# .....................................................................................
class DummyResponse:
    """This class is for testing and does not do anything."""
    # ...........................
    def __init__(self, status_code, url):
        """Sets the object's status code.

        Args:
            status_code (int): Status code for the dummy response.
            url (str): A url associated with the dummy response.
        """
        self.status_code = status_code
        self.url = url


# .....................................................................................
class Test_HttpError:
    """This class tests the _HttpError exception class."""
    # ...........................
    def test_constructor(self):
        """Tests that the constructor fails when called directly.

        The _HttpError class is a parent class and should not be instantiated
        directly.
        """
        with pytest.raises(RuntimeError):
            client_exceptions._HttpError('test_url')


# .....................................................................................
class Test_BadRequestError:
    """This class tests the BadRequestError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.BadRequestError(test_url)
        assert e.code == client_exceptions.BadRequestError.code
        assert e.message == client_exceptions.BadRequestError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .....................................................................................
class Test_ConflictError:
    """This class tests the ConflictError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.ConflictError(test_url)
        assert e.code == client_exceptions.ConflictError.code
        assert e.message == client_exceptions.ConflictError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# ....................................................................................
class Test_ForbiddenError:
    """This class tests the ForbiddenError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.ForbiddenError(test_url)
        assert e.code == client_exceptions.ForbiddenError.code
        assert e.message == client_exceptions.ForbiddenError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .....................................................................................
class Test_InternalServerError:
    """This class tests the InternalServerError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.InternalServerError(test_url)
        assert e.code == client_exceptions.InternalServerError.code
        assert e.message == client_exceptions.InternalServerError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .....................................................................................
class Test_MethodNotAllowedError:
    """This class tests the MethodNotAllowedError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.MethodNotAllowedError(test_url)
        assert e.code == client_exceptions.MethodNotAllowedError.code
        assert e.message == client_exceptions.MethodNotAllowedError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .....................................................................................
class Test_NotAcceptableError:
    """This class tests the NotAcceptableError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.NotAcceptableError(test_url)
        assert e.code == client_exceptions.NotAcceptableError.code
        assert e.message == client_exceptions.NotAcceptableError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .............................................................................
class Test_NotFoundError:
    """This class tests the NotFoundError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.NotFoundError(test_url)
        assert e.code == client_exceptions.NotFoundError.code
        assert e.message == client_exceptions.NotFoundError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .............................................................................
class Test_ServiceUnavailableError:
    """This class tests the ServiceUnavailableError exception class."""
    # ...........................
    def test_constructor(self):
        """Test error instance instantiation."""
        test_url = 'http://fake.url.com'
        e = client_exceptions.ServiceUnavailableError(test_url)
        assert e.code == client_exceptions.ServiceUnavailableError.code
        assert e.message == client_exceptions.ServiceUnavailableError.message
        assert e.url == test_url
        assert str(e) == 'HTTP Error: {} ({}) for {}'.format(
            e.code, e.message, e.url)


# .....................................................................................
class Test_raise_http_exception:
    """This class tests the raise_http_exception method."""
    # ...........................
    def test_bad_request_error(self):
        """Test that a bad request error is thrown when appropriate."""
        resp = DummyResponse(HttpStatus.BAD_REQUEST, 'http://someurl.com')
        with pytest.raises(client_exceptions.BadRequestError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_conflict_error(self):
        """Test that a conflict error is thrown when appropriate."""
        resp = DummyResponse(HttpStatus.CONFLICT, 'http://someurl.com')
        with pytest.raises(client_exceptions.ConflictError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_forbidden_error(self):
        """Test that a forbidden error is thrown when appropriate."""
        resp = DummyResponse(HttpStatus.FORBIDDEN, 'http://someurl.com')
        with pytest.raises(client_exceptions.ForbiddenError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_internal_server_error(self):
        """Test that an internal server error is thrown when appropriate."""
        resp = DummyResponse(
            HttpStatus.INTERNAL_SERVER_ERROR, 'http://someurl.com')
        with pytest.raises(client_exceptions.InternalServerError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_method_not_allowed_error(self):
        """Test that a method not allowed error is thrown when appropriate."""
        resp = DummyResponse(
            HttpStatus.METHOD_NOT_ALLOWED, 'http://someurl.com')
        with pytest.raises(client_exceptions.MethodNotAllowedError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_not_acceptable_error(self):
        """Test that a not acceptable error is thrown when appropriate."""
        resp = DummyResponse(HttpStatus.NOT_ACCEPTABLE, 'http://someurl.com')
        with pytest.raises(client_exceptions.NotAcceptableError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_not_found_error(self):
        """Test that a not found error is thrown when appropriate."""
        resp = DummyResponse(HttpStatus.NOT_FOUND, 'http://someurl.com')
        with pytest.raises(client_exceptions.NotFoundError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_service_unavailable_error(self):
        """Test that a service unavailable error is thrown when appropriate."""
        resp = DummyResponse(
            HttpStatus.SERVICE_UNAVAILABLE, 'http://someurl.com')
        with pytest.raises(client_exceptions.ServiceUnavailableError):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_uncaught_request_error(self):
        """Test that an uncaught user request error still raises an exception."""
        resp = DummyResponse(499, 'http://someurl.com')
        with pytest.raises(Exception):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_uncaught_server_error(self):
        """Test that an uncaught server error still raises an exception."""
        resp = DummyResponse(599, 'http://someurl.com')
        with pytest.raises(Exception):
            client_exceptions.raise_http_exception(resp)

    # ...........................
    def test_no_error(self):
        """Test that a successful response passes through."""
        resp = DummyResponse(HttpStatus.OK, 'http://someurl.com')
        assert client_exceptions.raise_http_exception(resp) is None
