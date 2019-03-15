"""Module containing functions for using the tree service endpoint
"""

from lm_client.common.api_service import RestService

# .............................................................................
class TreeApiService(RestService):
    """This class is used for working with the tree service end-point
    """
    end_point = 'api/v2/tree/'

    # ...........................
    def count(self, raw=False, after_time=None, before_time=None,
              has_branch_lengths=None, is_binary=None, is_ultrametric=None,
              meta_string=None, name=None, user=None):
        """Counts the number of trees matching the provided criteria.

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object.  If False, load into JSON.
            after_time (:obj:`str`, optional): Only trees modified after this
                time (in ISO-8601 format).
            before_time (:obj:`str`, optional): Only return trees modified
                before this time (in ISO-8601 format).
            has_branch_lengths (:obj:`bool`, optional): Return trees that have
                or do not have branch lengths.
            is_binary (:obj:`bool`, optional): Return trees that are or are not
                binary.
            is_ultrametric (:obj:`bool`, optional): Return trees that are or
                are not ultrametric.
            meta_string (:obj:`str`, optional): Return trees with this metadata
                string attached to them.
            name (:obj:`str`, optional): Return trees that have this name.
            user (:obj:`str`, optional): If 'public', return public trees.  If
                'anon', return anonymous trees.  If None, return the user's
                trees.
        """
        return RestService.count(self,
            '{}/count'.format(self.end_point), raw=raw, after_time=after_time,
            before_time=before_time, has_branch_lengths=has_branch_lengths,
            is_binary=is_binary, is_ultrametric=is_ultrametric,
            meta_string=meta_string, name=name, user=user)
    
    # ...........................
    def delete(self, tree_id, raw=False):
        """Attempts to delete the tree specified by tree_id.
        """
        return RestService.delete(self,
            '{}/{}'.format(self.end_point, tree_id), raw=raw)

    # ...........................
    def get(self, tree_id, interface=None, raw=False):
        """Attempts to retrieve the tree specified by the ID.

        Args:
            tree (int): The ID number of the tree to retrieve.
            interface (:obj:`str`, optional): If provided, request the response
                in this interface.
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object.  If False, load into JSON.
        """
        return RestService.get(self,
            '{}{}'.format(self.end_point, tree_id), interface=interface,
            raw=raw)
    
    # ...........................
    def list(self, raw=False, after_time=None, before_time=None,
              has_branch_lengths=None, is_binary=None, is_ultrametric=None,
              limit=None, meta_string=None, name=None, offset=None, user=None):
        """Lists occurrence sets matching the provided criteria.

        Args:
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object.  If False, load into JSON.
            after_time (:obj:`str`, optional): Only trees modified after this
                time (in ISO-8601 format).
            before_time (:obj:`str`, optional): Only return trees modified
                before this time (in ISO-8601 format).
            has_branch_lengths (:obj:`bool`, optional): Return trees that have
                or do not have branch lengths.
            is_binary (:obj:`bool`, optional): Return trees that are or are not
                binary.
            is_ultrametric (:obj:`bool`, optional): Return trees that are or
                are not ultrametric.
            limit (:obj:`int`, optional): Return up to this number of trees.
            meta_string (:obj:`str`, optional): Return trees with this metadata
                string attached to them.
            name (:obj:`str`, optional): Return trees that have this name.
            offset (:obj:`int`, optional): Offset the list of returned trees by
                this number.
            user (:obj:`str`, optional): If 'public', return public trees.  If
                'anon', return anonymous trees.  If None, return the user's
                trees.
        """
        return RestService.list(self,
            self.end_point, raw=raw, after_time=after_time,
            before_time=before_time, has_branch_lengths=has_branch_lengths,
            is_binary=is_binary, is_ultrametric=is_ultrametric,
            limit=limit, meta_string=meta_string, name=name, offset=offset,
            user=user)
    
    # ...........................
    def post(self, filename_or_flo, name, schema, raw=False):
        """Attempt to POST a new tree to the service end-point

        Args:
            filename_or_flo (str or file-like object): A filename or file-like
                object containing the tree data.
            name (str): A name for this new tree.
            schema (str): The tree schema (newick, nexus, nexml).
            raw (:obj:`bool`, optional): If True, return the raw response
                file-like object.  If False, load into JSON.
        """
        try:
            body = filename_or_flo.read()
        except:  # Try opening the file
            with open(filename_or_flo) as in_file:
                body = in_file.read()
        return RestService.post(self,
            self.end_point, raw=raw, body=body, name=name, schema=schema)
