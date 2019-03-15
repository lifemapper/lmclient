"""
"""


from lm_client.common.api_service import RestService


# .............................................................................
class GridsetApiService(RestService):
    """
    """
    end_point = 'api/v2/gridset'

    # ...........................
    def count(self, raw=False, after_time=None, before_time=None,
              epsg_code=None, meta_string=None, shapegrid_id=None):
        """Counts

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.count(self,
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            meta_string=meta_string, shapegrid_id=shapegrid_id,
            before_time=before_time, epsg_code=epsg_code)

    # ...........................
    def delete(self, gridset_id, raw=False):
        """Attempts to delete a gridset

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.delete(self,
            '{}/{}'.format(self.end_point, gridset_id), raw=raw)

    # ...........................
    def delete_tree(self, gridset_id, raw=False):
        """Attempts to delete a gridset's tree

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.delete(self,
            '{}/{}/tree'.format(self.end_point, gridset_id), raw=raw)

    # ...........................
    def get(self, gridset_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}'.format(self.end_point, gridset_id), raw=raw,
            interface=interface)

    # ...........................
    def get_hypotheses(self, gridset_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}/biogeo'.format(self.end_point, gridset_id), raw=raw,
            interface=interface)

    # ...........................
    def get_tree(self, gridset_id, raw=False, interface=None):
        """Attempts to get

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}/{}/tree'.format(self.end_point, gridset_id), raw=raw,
            interface=interface)

    # ...........................
    def list(self, raw=False, after_time=None, before_time=None,
             epsg_code=None, limit=None, meta_string=None, offset=None,
             shapegrid_id=None):
        """Gets a list

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object from the request.  If False, load into JSON.
        """
        return RestService.list(
            self, self.end_point, raw=raw, after_time=after_time,
            before_time=before_time, epsg_code=epsg_code, limit=limit,
            meta_string=meta_string, offset=offset, shapegrid_id=shapegrid_id)

    # ...........................
    def post(self, boom_post_json, raw=False):
        """
        """
        return RestService.post(self,
            self.end_point, raw=raw, body=boom_post_json,
            headers={'Content-Type' : 'application/json'})

    # ...........................
    def post_analyses(self, gridset_id, do_calc=None, do_mcpa=None,
                      num_permutations=None, raw=False):
        return RestService.post(self,
            '{}/{}/analysis'.format(self.end_point, gridset_id), raw=raw,
            do_calc=do_calc, do_mcpa=do_mcpa,
            num_permutations=num_permutations)

    # ...........................
    def post_tree(self, gridset_id, tree_id=None, tree_content=None,
                  tree_schema=None, raw=False):
        return RestService.post(self,
            '{}/{}/tree'.format(self.end_point, gridset_id), raw=raw,
            body=tree_content, tree_schema=tree_schema, tree_id=tree_id)
