"""Module containing functions for uploading data services
"""

from lm_client.common.api_service import RestService

# .............................................................................
class UploadApiService(RestService):
    """
    """
    end_point = 'api/v2/upload'
    
    # ...........................
    def occurrence(self, filename_or_flo, metadata, data_name, raw=False):
        if os.path.exists(filename_or_flo):
            filename_or_flo = open(filename_or_flo)
        return RestService.post(
            self.end_point, body=filename_or_flo, file_name=data_name,
            upload_type='occurrence', metadata=metadata, raw=raw)
        