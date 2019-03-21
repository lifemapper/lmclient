"""Module containing functions for uploading data services
"""
import os

from lm_client.common.api_service import RestService


# .............................................................................
class UploadApiService(RestService):
    """
    """
    end_point = 'api/v2/upload'

    # ...........................
    def biogeographic_hypotheses(self, filename, package_name):
        if os.path.exists(filename):
            return RestService.post(
                self, self.end_point,
                files={
                    'file': (
                        filename, open(filename, 'rb'), 'application/zip')},
                file_name=package_name, upload_type='biogeo')

    # ...........................
    def occurrence(self, filename, metadata, data_name):
        if os.path.exists(filename):
            return RestService.post(
                self, self.end_point,
                files={
                    'file': (filename, open(filename, 'rb'), 'text/csv')},
                file_name=data_name, upload_type='occurrence',
                metadata=metadata)

    # ...........................
    def tree(self, filename, tree_name):
        if os.path.exists(filename):
            return RestService.post(
                self, self.end_point,
                files={'file': (filename, open(filename, 'rb'))},
                file_name=tree_name, upload_type='tree')
