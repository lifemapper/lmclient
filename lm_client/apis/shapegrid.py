"""This module interacts with the shapegrid end-point
"""


from lm_client.common.api_service import RestService


# .............................................................................
class ShapegridApiService(RestService):
    """
    """
    end_point = 'api/v2/shapegrid'

    # ...........................
    def count(self, raw=False, after_time=None, before_time=None,
              cell_sides=None, cell_size=None, epsg_code=None):
        """Counts

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.count(self,
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            before_time=before_time, cell_sides=cell_sides,
            cell_size=cell_size, epsg_code=epsg_code)

    # ...........................
    def delete(self, shapegrid_id, raw=False):
        """Attempts to delete

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.delete(self,
            '{}/{}'.format(self.end_point, shapegrid_id), raw=raw)

    # ...........................
    def get(self, shapegrid_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}'.format(self.end_point, shapegrid_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, before_time=None,
             cell_sides=None, cell_size=None, epsg_code=None, limit=None,
             offset=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(self,
            self.end_point, raw=raw, after_time=after_time,
            before_time=before_time, cell_sides=cell_sides,
            cell_size=cell_size, epsg_code=epsg_code, limit=limit,
            offset=offset)

    # ...........................
    def post(self, name, epsg_code, cell_sides, cell_size, map_units, bbox,
             cutout=None, raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw,
            headers={'Content-Type' : 'application/json'}, name=name,
            epsg_code=epsg_code, cell_sides=cell_sides, cell_size=cell_size,
            map_units=map_units, bbox=bbox, cutout=cutout)
