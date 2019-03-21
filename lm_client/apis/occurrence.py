"""Module containing functions for using the Occurrence service
"""

from lm_client.common.api_service import RestService


# .............................................................................
class OccurrenceApiService(RestService):
    """
    """
    end_point = 'api/v2/occurrence/'

    # ...........................
    def count(self, after_status=None, after_time=None, before_status=None,
              before_time=None, display_name=None, epsg_code=None,
              gridset_id=None, minimum_number_of_points=None, squid=None,
              status=None, user=None):
        """Counts the number of occurrence sets matching the provided criteria.

        Args:
            after_status (:obj:`int`, optional): Only return occurrence sets
                that have a status value greater than this number.
            after_time (:obj:`str`, optional): Only return occurrence sets
                modified after this time (in ISO-8601 format).
            before_status (:obj:`int`, optional): Only return occurrence sets
                that have a status value less than this number.
            before_time (:obj:`str`, optional): Only return occurrence sets
                modified before this time (in ISO-8601 format).
            display_name (:obj:`str`, optional): Only return occurrence sets
                that have this display name.
            epsg_code (:obj:`int`, optional): Only return occurrence sets that
                have this EPSG code.
            gridset_id (:obj:`int`, optional): Only return occurrence sets that
                are part of the gridset with this ID.
            minimum_number_of_points (:obj:`int`, optional): Only return
                occurrence sets that have at least this many points.
            squid (:obj:`str`, optional): Only return occurrence sets that have
                this squid (hash value for species identifier).
            status (:obj:`int`, optional): Only return occurrence sets that
                have this status.
            user (:obj:`str`, optional): If 'public', return public occurrence
                sets.  If 'anon', return anonymous occurrence sets.  If None,
                return the user's occurrence sets.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point),
            after_status=after_status, after_time=after_time,
            before_status=before_status, before_time=before_time,
            display_name=display_name, epsg_code=epsg_code,
            gridset_id=gridset_id,
            minimum_number_of_points=minimum_number_of_points, squid=squid,
            status=status, user=user)

    # ...........................
    def delete(self, occurrence_id):
        """Attempts to delete the occurrence set specified by occurrence_id.
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, occurrence_id))

    # ...........................
    def get(self, occurrence_id, interface=None):
        """Attempts to retrieve the occurrence set specified by the ID.

        Args:
            occurrence_id (int): The ID number of the occurrence set to
                retrieve.
            interface (:obj:`str`, optional): If provided, request the response
                in this interface.
        """
        return RestService.get(
            self, '{}{}'.format(self.end_point, occurrence_id),
            interface=interface)

    # ...........................
    def list(self, after_status=None, after_time=None, before_status=None,
             before_time=None, display_name=None, epsg_code=None,
             gridset_id=None, limit=None, minimum_number_of_points=None,
             offset=None, squid=None, status=None, user=None):
        """Lists occurrence sets matching the provided criteria.

        Args:
            after_status (:obj:`int`, optional): Only return occurrence sets
                that have a status value greater than this number.
            after_time (:obj:`str`, optional): Only return occurrence sets
                modified after this time (in ISO-8601 format).
            before_status (:obj:`int`, optional): Only return occurrence sets
                that have a status value less than this number.
            before_time (:obj:`str`, optional): Only return occurrence sets
                modified before this time (in ISO-8601 format).
            display_name (:obj:`str`, optional): Only return occurrence sets
                that have this display name.
            epsg_code (:obj:`int`, optional): Only return occurrence sets that
                have this EPSG code.
            gridset_id (:obj:`int`, optional): Only return occurrence sets that
                are part of the gridset with this ID.
            limit (:obj:`int`, optional): Only return this number of occurrence
                sets.
            minimum_number_of_points (:obj:`int`, optional): Only return
                occurrence sets that have at least this many points.
            offset (:obj:`int`, optional): Offset the occurrence sets returned
                by this number.
            squid (:obj:`str`, optional): Only return occurrence sets that have
                this squid (hash value for species identifier).
            status (:obj:`int`, optional): Only return occurrence sets that
                have this status.
            user (:obj:`str`, optional): If 'public', return public occurrence
                sets.  If 'anon', return anonymous occurrence sets.  If None,
                return the user's occurrence sets.
        """
        return RestService.list(
            self, self.end_point, after_status=after_status,
            after_time=after_time, before_status=before_status,
            before_time=before_time, display_name=display_name,
            epsg_code=epsg_code, gridset_id=gridset_id, limit=limit,
            minimum_number_of_points=minimum_number_of_points, offset=offset,
            squid=squid, status=status, user=user)
