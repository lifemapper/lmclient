"""Module containing constants for the Lifemapper API Client
"""


# .............................................................................
class HttpStatus:
    """Constants class for HTTP 1.1 Status Codes

    Note:
        * HTTP 1.1 Status Codes as defined by
            http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
    """
    # Informational 1xx
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101

    # Successful 2xx
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206

    # Redirectional 3xx
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 204
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307

    # Client Error 4xx
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUEST_RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417

    # Server Error 5xx
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505


# .............................................................................
class INTERFACES(object):
    """Class containing constants for available service format interfaces
    """
    CSV = 'csv'
    EML = 'eml'
    GEO_JSON = 'geojson'
    GTIFF = 'gtiff'
    JSON = 'json'
    KML = 'kml'
    NEWICK = 'newick'
    NEXUS = 'nexus'
    PACKAGE = 'package'
    PROGRESS = 'progress'
    SHAPEFILE = 'shapefile'

    # ...........................
    @staticmethod
    def binary_interfaces():
        """Returns a list of interfaces that have binary content
        """
        return [INTERFACES.GTIFF, INTERFACES.PACKAGE, INTERFACES.SHAPEFILE]

    # ...........................
    @staticmethod
    def json_interfaces():
        """Returns a list of interfaces that can be processed as JSON
        """
        return [INTERFACES.GEO_JSON, INTERFACES.JSON, INTERFACES.PROGRESS]

    # ...........................
    @staticmethod
    def text_interfaces():
        """Returns a list of interfaces that are text
        """
        return [
            INTERFACES.CSV, INTERFACES.EML, INTERFACES.GEO_JSON,
            INTERFACES.JSON, INTERFACES.KML, INTERFACES.NEWICK,
            INTERFACES.NEXUS, INTERFACES.PROGRESS]
