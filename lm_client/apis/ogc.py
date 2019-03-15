"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class OgcApiService(RestService):
    """
    """
    end_point = 'api/v2/ogc'

    # ...........................
    def get(self, map_name, raw=False, bbox=None, bgcolor=None, color=None,
            coverage=None, crs=None, exceptions=None, height=None, layer=None,
            layers=None, point=None, request=None, format=None, service=None,
            sld=None, sld_body=None, srs=None, styles=None, time=None,
            transparent=None, version=None, width=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            self.end_point, raw=raw, map_name=map_name, bbox=bbox,
            bgcolor=bgcolor, color=color, coverage=coverage, crs=crs,
            exceptions=exceptions, height=height, layer=layer, layers=layers,
            point=point, request=request, format=format, service=service,
            sld=sld, sld_body=sld_body, srs=srs, styles=styles, time=time,
            transparent=transparent, version=version, width=width)
