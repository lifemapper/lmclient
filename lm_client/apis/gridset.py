"""Wrapper for Lifemapper Gridset endpoint."""
from lm_client.common.api_service import RestService


# .....................................................................................
class GridsetApiService(RestService):
    """Class wrapping the Lifemapper Gridset service endpoint."""
    end_point = 'api/v2/gridset'

    # ...........................
    def count(
        self,
        after_time=None,
        before_time=None,
        epsg_code=None,
        meta_string=None,
        shapegrid_id=None
    ):
        """Counts gridsets matching the provided criteria.

        Args:
            after_time (str): Count gridsets modified after this time.
            before_time (str): Count gridsets modified before this time.
            epsg_code (int): The integer representing the map projection EPSG code for
                the gridsets to count.
            meta_string (str): Metadata string to use to count gridsets.
            shapegrid_id (int): Count gridsets built from the shapegrid with this
                identifier.

        Returns:
            int: The number of gridsets matching the provided criteria.
        """
        return RestService.count(
            self, '{}/count'.format(self.end_point), after_time=after_time,
            meta_string=meta_string, shapegrid_id=shapegrid_id,
            before_time=before_time, epsg_code=epsg_code)

    # ...........................
    def delete(self, gridset_id):
        """Attempts to delete a gridset.

        Args:
            gridset_id (int): The identifier for the gridset to delete.

        Returns:
            HTTP Response: Confirmation or failure response associated with the delete
                request.
        """
        return RestService.delete(
            self, '{}/{}'.format(self.end_point, gridset_id))

    # ...........................
    def delete_tree(self, gridset_id):
        """Attempts to delete a gridset's tree.

        Args:
            gridset_id (int): The identifier of the tree to delete.

        Returns:
            HTTP Response: An indication from the server if the delete was successful.
        """
        return RestService.delete(
            self,
            '{}/{}/tree'.format(self.end_point, gridset_id)
        )

    # ...........................
    def get(self, gridset_id, interface=None):
        """Attempts to get a gridset.

        Args:
            gridset_id (int): The identifier of the gridset to retrieve.
            interface (str): The format interface the gridset should be returned as.

        Returns:
            xml string: Returned if the interface is 'xml'
            dict: A JSON dictionary of gridset metadata.
        """
        return RestService.get(
            self,
            '{}/{}'.format(self.end_point, gridset_id),
            interface=interface
        )

    # ...........................
    def get_hypotheses(self, gridset_id, interface=None):
        """Attempts to get biogeographic hypotheses for the gridset.

        Args:
            gridset_id (int): The identifier of the gridset to retrieve hypotheses.
            interface (str): The format interface the gridset hypotheses should be
                returned as.

        Returns:
            xml string: Returned if the interface is 'xml'
            dict: A JSON dictionary of gridset hypotheses metadata.
        """
        return RestService.get(
            self, '{}/{}/biogeo'.format(self.end_point, gridset_id),
            interface=interface)

    # ...........................
    def get_tree(self, gridset_id, interface=None):
        """Attempts to get a tree for the specified gridset.

        Args:
            gridset_id (int): The identifier of the gridset to retrieve tree.
            interface (str): The format interface to return the gridset tree.


        Returns:
            str: A tree formatted as newick or nexus, specified by the interface
                parameter.
        """
        return RestService.get(
            self, '{}/{}/tree'.format(self.end_point, gridset_id),
            interface=interface)

    # ...........................
    def list(
        self,
        after_time=None,
        before_time=None,
        epsg_code=None,
        limit=None,
        meta_string=None,
        offset=None,
        shapegrid_id=None
    ):
        """Gets a list of gridsets matching the provided criteria.

        Args:
            after_time (str): Count gridsets modified after this time.
            before_time (str): Count gridsets modified before this time.
            epsg_code (int): The integer representing the map projection EPSG code for
                the gridsets to count.
            limit (int): The maximum number of records to return in this request.
            meta_string (str): Metadata string to use to count gridsets.
            offset (int): Start returned records after this offset (used for paging).
            shapegrid_id (int): Count gridsets built from the shapegrid with this
                identifier.

        Returns:
            list of dict: A list of JSON dictionaries for matching gridset metadata.
        """
        return RestService.list(
            self,
            self.end_point,
            after_time=after_time,
            before_time=before_time,
            epsg_code=epsg_code,
            limit=limit,
            meta_string=meta_string,
            offset=offset,
            shapegrid_id=shapegrid_id
        )

    # ...........................
    def post(self, boom_post_json):
        """POST a new gridset creation request.

        Args:
            boom_post_json (dict): A JSON dictionary of gridset parameters.

        Returns:
            HTTP Response: A success indication as an HTTP response status.
        """
        return RestService.post(
            self,
            self.end_point,
            body=boom_post_json,
            headers={'Content-Type': 'application/json'}
        )

    # ...........................
    def post_analyses(
        self,
        gridset_id,
        do_calc=None,
        do_mcpa=None,
        num_permutations=None
    ):
        """Request computational analyses to be run on a gridset.

        Args:
            gridset_id (int): The identifier of the gridset to use.
            do_calc (int): Zero or one indicating if RAD stats should be computed.
            do_mcpa (int): Zero or one indicating if MCPA should be computed.
            num_permutations (int): The number of permutations to create when creating
                an null model.

        Returns:
            HTTP Response: An HTTP status response indicating if the request was
                successfully received.
        """
        return RestService.post(
            self,
            '{}/{}/analysis'.format(self.end_point, gridset_id),
            do_calc=do_calc,
            do_mcpa=do_mcpa,
            num_permutations=num_permutations
        )

    # ...........................
    def post_tree(
        self,
        gridset_id,
        tree_id=None,
        tree_content=None,
        tree_schema=None
    ):
        """POST a tree to be added to the specified gridset.

        Args:
            gridset_id (int): The identifier of the gridset to add the tree to.
            tree_id (int): If the tree already exists on the server, just specify it's
                identifier.
            tree_content (str): The content of the tree if it does not already exist.
            tree_schema (str): The schema of the tree content to post.

        Returns:
            HTTP Response: An HTTP status response indicating if the request was
                successfully received.
        """
        return RestService.post(
            self,
            '{}/{}/tree'.format(self.end_point, gridset_id),
            body=tree_content,
            tree_schema=tree_schema,
            tree_id=tree_id
        )
