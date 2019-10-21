"""Module containing a class for retrieving OGC maps from Lifemapper.

Lifemapper provides an OGC end-point that can be used to retrieve data and maps
for multiple Lifemapper objects.

See: https://www.opengeospatial.org/standards/wms

See: https://www.opengeospatial.org/standards/wcs
"""


from lm_client.common.api_service import RestService


# .............................................................................
class OgcApiService(RestService):
    """Class for accessing Lifemapper OGC services.
    """
    end_point = 'api/v2/ogc'

    # ...........................
    def get(self, map_name, bbox=None, bgcolor=None, color=None, coverage=None,
            crs=None, exceptions=None, height=None, layer=None, layers=None,
            request=None, format=None, service=None, sld=None, sld_body=None,
            srs=None, styles=None, time=None, transparent=None, version=None,
            width=None):
        """Attempts to get a map or coverage matching the provided parameters.

        Args:
            map_name (str): The name of the map file that contains the data to
                be retrieved.  This can be found in the map.mapName value of
                the related Lifemapper object's JSON interface.
            bbox (str): The bounding box of the region to be returned in the
                format: minx,miny,maxx,maxy.
            bgcolor (str): Hexadecimal RGB color for the background of the map
                response (if WMS).
            color: The color to use for the data in the response image (if WMS).
            coverage (str): The data coverage to retrieve, this should be the
                same value as the Lifemapper spatial object's map.layerName
                attribute.
            crs (str): The coordinate reference system for the map or data
                response.
            exceptions (str): The format in which exceptions are to be reported
                (default is XML).
            height (int): The height, in pixels, of the response WMS map.
            layer (str): The layer in a map file to be retrieved.  This can be
                found in a Lifemapper spatial object's map.layerName attribute.
            layers (str): A comma-separated list of layers to retrieve from a
                map file.  These layers will be stacked and returned as a
                single image.
            request (str): The request operation name to perform.
            format (str): The desired response format MIME-Type.
            service (str): The OGC service to use (WCS | WMS).
            sld (str): A URL referencing a StyledLayerDescriptor XML file which
                controls or enhances map layers and styling.
            sld_body (str): A URL-encoded StyledLayerDescriptor XML document
                which controls or enhances map layers and styling.
            srs (str): The spatial reference system for the map output.  'crs'
                for version 1.3.0.
            styles (str): A list of styles for the response.
            time (str): A time or time range for map requests.
            transparent (str): Boolean indicating if the background of the map
                should be transparent (TRUE | FALSE).
            version (str): Teh version of the service to use.
            width (int): The width, in pixels, of the response WMS map.

        Returns:
            bytes - Image or data from OGC W*S end-point.
        """
        return RestService.get(
            self, self.end_point, map_name=map_name, bbox=bbox,
            bgcolor=bgcolor, color=color, coverage=coverage, crs=crs,
            exceptions=exceptions, height=height, layer=layer, layers=layers,
            point=point, request=request, format=format, service=service,
            sld=sld, sld_body=sld_body, srs=srs, styles=styles, time=time,
            transparent=transparent, version=version, width=width)
