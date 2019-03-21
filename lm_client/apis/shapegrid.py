"""This module interacts with the shapegrid end-point

Shapegrids are vector layers where each feature represents a site.  These are
the same sites that are used for Presence Absence Matrices, PAMs, as well as
encoded climate data and biogeographic hypotheses.  Lifemapper generated
shapegrids are regularly spaced rectangular or hexagonal cells that form a
grid.  The grid generally covers an area specified by a bounding box, but may
also have some cells removed in a "cutout" operation so that the remaining
cells cover the desired area of interest.
"""


from lm_client.common.api_service import RestService


# .............................................................................
class ShapegridApiService(RestService):
    """This class is responsible for interactions with shapegrid end-point

    Todo: Document valid GET interfaces for Shapegrids
    """
    end_point = 'api/v2/shapegrid'

    # ...........................
    def count(self, raw=False, after_time=None, before_time=None,
              cell_sides=None, cell_size=None, epsg_code=None):
        """Counts shapegrids matching the provided criteria

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            after_time (:obj:`str`, optional): Count shapegrids modified after
                this time (in ISO-8601 format).
            before_time (:obj:`str`, optional): Count shapegrids modified
                before this time (in ISO-8601 format).
            cell_sides (:obj:`int`, optional): Count shapegrids that have cells
                with the specified number of sides
                (4 - rectangles, 6 - hexagons).
            cell_size (:obj:`float`, optional): Count shapegrids with the
                specified cell size (resolution).
            epsg_code (:obj:`int`, optional): Count shapegrids that were
                created using the specified spatial projection represented by
                the EPSG code.

        Returns:
            int - The number of shapegrids matching the provided criteria.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), raw=raw,
            after_time=after_time, before_time=before_time,
            cell_sides=cell_sides, cell_size=cell_size, epsg_code=epsg_code)

    # ...........................
    def delete(self, shapegrid_id, raw=False):
        """Attempts to delete a shapegrid

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            shapegrid_id (int): The database identifier of the shapegrid to
                attempt to delete.

        Todo: Fill in returns for shapegrid delete
        Todo: Add documentation for exceptions from shapegrid delete
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, shapegrid_id), raw=raw)

    # ...........................
    def get(self, shapegrid_id, raw=False, interface=None):
        """Attempts to get a shapegrid

        Args:
            shapegrid_id (int): The database identifier of the shapegrid to
                attempt to retrieve.
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            interface (:obj:`str`, optional): The requested interface, or
                format, for the shapegrid to be returned as.  Valid options
                are: EML, JSON (default), GeoJSON, and SHAPEFILE.

        Todo: Add documentation for return options for shapegrid GET
        Todo: Add documentation for exceptions from shapegrid GET
        """
        return RestService.get(
            self, '{}/{}'.format(self.end_point, shapegrid_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, before_time=None,
             cell_sides=None, cell_size=None, epsg_code=None, limit=None,
             offset=None):
        """Gets a list of shapegrids matching the provided criteria

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
            after_time (:obj:`str`, optional): Return shapegrids modified after
                this time (in ISO-8601 format).
            before_time (:obj:`str`, optional): Return shapegrids modified
                before this time (in ISO-8601 format).
            cell_sides (:obj:`int`, optional): Return shapegrids that have
                cells with the specified number of sides
                (4 - rectangles, 6 - hexagons).
            cell_size (:obj:`float`, optional): Return shapegrids with the
                specified cell size (resolution).
            epsg_code (:obj:`int`, optional): Return shapegrids that were
                created using the specified spatial projection represented by
                the EPSG code.
            limit (:obj:`int`, optional): Return this number of shapegrids.
            offset (:obj:`int`, optional): Offset the shapegrids returned by
                this number.  Use along with limit to implement paging.

        Return:
            list of shapegrid metadata - Returns a list of shapegrids matching
                the provided criteria.
        """
        return RestService.list(
            self, self.end_point, raw=raw, after_time=after_time,
            before_time=before_time, cell_sides=cell_sides,
            cell_size=cell_size, epsg_code=epsg_code, limit=limit,
            offset=offset)

    # ...........................
    def post(self, name, epsg_code, cell_sides, cell_size, map_units, bbox,
             cutout=None, raw=False):
        """Posts a new shapegrid to the server.

        Args:
            name (str): A name for this shapegrid.
            epsg_code (int): An EPSG code representing the map projection to
                use when defining this shapegrid.
            cell_sides (int): The number of sides each cell in the shapegrid
                should have.  Use 4 for rectangular cells and 6 for hexagonal
                cells.
            cell_size (float): The size of each side of each cell in the
                shapegrid (in map_units).
            map_units (str): The units for the cell_sizes of the map.  Examples
                are:
                    dd - decimal degrees
                    m - meters
                    ft - feet
            bbox (tuple): Bounding box tuple for this shapegrid in the form
                (minimum x, maximum x, minimum y, maximum y).
            cutout (:obj:`str`, optional): An area of the shapegrid to "cut
                out", meaning to remove cells that fall within that area.  This
                should be specified as Well-Known Text.
            raw (:obj:`bool`, optional): If Ture, return the raw response
                file-like object from the request.  If False, load into JSON.

        Returns:
            dict - A JSON dictionary of metadata about the newly posted
                shapegrid.

        Todo: Add documentation about failure responses
        """
        return RestService.post(
            self, self.end_point, raw=raw,
            headers={'Content-Type': 'application/json'}, name=name,
            epsg_code=epsg_code, cell_sides=cell_sides, cell_size=cell_size,
            map_units=map_units, bbox=bbox, cutout=cutout)
