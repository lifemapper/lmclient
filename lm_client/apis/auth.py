"""Module containing authentication service calls
"""
from lm_client.common.api_service import ApiService


# .............................................................................
class AuthApiService(ApiService):
    """
    """
    # ...........................
    def login(self, user_id, passwd):  # pragma: no cover
        """
        """
        response = self.api_client.post(
            'api/login', user_id=user_id, pword=passwd)
        return response

    # ...........................
    def logout(self):

        response = self.api_client.get('api/logout')
        return response
