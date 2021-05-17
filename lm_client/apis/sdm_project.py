"""SDM Projection service wrapper."""
from lm_client.common.api_service import RestService


# .....................................................................................
class SdmProjectApiService(RestService):
    """Wrapper class for the Lifemapper SDM Projection service."""
    end_point = 'api/v2/sdmproject'

    # ...........................
    def count(
        self,
        after_status=None,
        after_time=None,
        algorithm_code=None,
        before_status=None,
        before_time=None,
        display_name=None,
        epsg_code=None,
        model_scenario_code=None,
        occurrence_set_id=None,
        projection_scenario_code=None,
        scenario_id=None,
        status=None,
        gridset_id=None
    ):
        """Counts projections matching the provided criteria.

        Args:
            after_status (int): Count projections with a status greater than this.
            after_time (str): Count projections modified after this time.
            algorithm_code (str): Count projections built with this algorithm.
            before_status (int): Count projections with a status less than this.
            before_time (str): Count projections modified before this time.
            display_name (str): Count projections with this display name.
            epsg_code (int): Count projections using this map projection.
            model_scenario_code (str): Count projections built from this model.
            occurrence_set_id (int): Count projections built from this occurrence set.
            projection_scenario_code (str): Count projections using this scenario.
            scenario_id (int): Count projections using this scenario identifier.
            status (int): Count projections with this exact status.
            gridset_id (int): Count projections in this gridset.

        Returns:
            int: The number of projections matching the criteria.
        """
        return RestService.count(
            self,
            '{}/count'.format(self.end_point),
            after_status=after_status,
            after_time=after_time,
            algorithm_code=algorithm_code,
            before_status=before_status,
            before_time=before_time,
            display_name=display_name,
            epsg_code=epsg_code,
            model_scenario_code=model_scenario_code,
            occurrence_set_id=occurrence_set_id,
            projection_scenario_code=projection_scenario_code,
            scenario_id=scenario_id,
            status=status,
            gridset_id=gridset_id
        )

    # ...........................
    def delete(self, sdmproject_id):
        """Attempts to delete a projection.

        Args:
            sdmproject_id (int): The identifier of the projection to delete.

        Returns:
            HTTP Response: An HTTP response indicating success.
        """
        return RestService.delete(self, '{}/{}'.format(self.end_point, sdmproject_id))

    # ...........................
    def get(self, sdmproject_id, interface=None):
        """Attempts to get a projection.

        Args:
            sdmproject_id (int): The identifier of the projection to retrieve.
            interface (str): The format to return the projection as.

        Returns:
            str: XML projection metadata.
            dict: A JSON dictionary of projection metadata.
            bytes: Binary projection data as a GeoTIFF.
        """
        return RestService.get(
            self,
            '{}/{}'.format(self.end_point, sdmproject_id),
            interface=interface
        )

    # ...........................
    def list(
        self,
        after_status=None,
        after_time=None,
        algorithm_code=None,
        before_status=None,
        before_time=None,
        display_name=None,
        epsg_code=None,
        limit=None,
        model_scenario_code=None,
        occurrence_set_id=None,
        offset=None,
        projection_scenario_code=None,
        scenario_id=None,
        status=None,
        gridset_id=None
    ):
        """Gets a list of projections matching the provided criteria.

        Args:
            after_status (int): Return projections with a status greater than this.
            after_time (str): Return projections modified after this time.
            algorithm_code (str): Return projections built with this algorithm.
            before_status (int): Return projections with a status less than this.
            before_time (str): Return projections modified before this time.
            display_name (str): Return projections with this display name.
            epsg_code (int): Return projections using this map projection.
            limit (int): The maximum number of projections to return.
            model_scenario_code (str): Return projections built from this model.
            occurrence_set_id (int): Return projections built from this occurrence set.
            offset (int): Start returned projections after this offset.
            projection_scenario_code (str): Return projections using this scenario.
            scenario_id (int): Return projections using this scenario identifier.
            status (int): Return projections with this exact status.
            gridset_id (int): Return projections in this gridset.

        Returns:
            list of dict: A list of JSON dictionary metadata for matching scenarios.
        """
        return RestService.list(
            self,
            self.end_point,
            after_time=after_time,
            scenario_id=scenario_id,
            before_time=before_time,
            limit=limit,
            offset=offset,
            after_status=after_status,
            algorithm_code=algorithm_code,
            before_status=before_status,
            display_name=display_name,
            epsg_code=epsg_code,
            model_scenario_code=model_scenario_code,
            status=status,
            occurrence_set_id=occurrence_set_id,
            projection_scenario_code=projection_scenario_code,
            gridset_id=gridset_id
        )

    # ...........................
    def post(self, boom_post_json):
        """Post a new experiment.

        Args:
            boom_post_json (dict): A dictionary of BOOM parameters for submitting an
                experiment.

        Returns:
            HTTP Response: An indication of success of the experiment post.
        """
        return RestService.post(
            self,
            self.end_point,
            body=boom_post_json,
            headers={'Content-Type': 'application/json'}
        )
