"""Module containing functions for uploading data services."""
import json
import os

from lmclient.common.api_service import RestService


# .....................................................................................
class UploadApiService(RestService):
    """Upload service wrapper class."""
    end_point = 'api/v2/upload'

    # ...........................
    def biogeographic_hypotheses(self, filename, package_name):
        """Upload a zip file of biogeographic hypotheses.

        Args:
            filename (str): The file path to the hypothesis zip file to upload.
            package_name (str): A name for this newly uploaded hypotheses zip file.

        Returns:
            HTTP Response: An indication of success.
        """
        if os.path.exists(filename):
            return RestService.post(
                self,
                self.end_point,
                files={'file': (filename, open(filename, 'rb'), 'application/zip')},
                file_name=package_name,
                upload_type='biogeo'
            )

    # ...........................
    def occurrence(self, filename, metadata, data_name):
        """Upload a zip file of occurrence data.

        Args:
            filename (str): The file path to the occurrence zip file to upload.
            metadata (dict): Metadata about the structure of the occurrence data file.
            data_name (str): A name for the newly uploaded occurrence file.

        Returns:
            HTTP Response: An indication of success.
        """
        # If metadata is a dictionary, encode for posting
        if isinstance(metadata, dict):
            metadata = json.dumps(metadata)
        if os.path.exists(filename):
            return RestService.post(
                self,
                self.end_point,
                files={'file': (filename, open(filename, 'rb'), 'text/csv')},
                file_name=data_name,
                upload_type='occurrence',
                metadata=metadata
            )

    # ...........................
    def tree(self, filename, tree_name):
        """Upload a tree file.

        Args:
            filename (str): The file path to the tree to upload.
            tree_name (str): The name of the newly uploaded tree.

        Returns:
            HTTP Response: An indication of success.
        """
        if os.path.exists(filename):
            return RestService.post(
                self,
                self.end_point,
                files={'file': (filename, open(filename, 'rb'))},
                file_name=tree_name,
                upload_type='tree'
            )
