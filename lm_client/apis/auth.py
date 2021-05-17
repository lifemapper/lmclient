"""Module containing authentication service calls."""
import http.cookiejar as cookie_jar
from urllib.parse import urlparse
import urllib.request

from lm_client.common.api_service import ApiService


# .....................................................................................
class AuthApiService(ApiService):
    """Class wrapping the Lifemapper authentication service."""
    # ...........................
    def login(self, user_id, passwd):  # pragma: no cover
        """Log in to the Lifemapper server.

        Args:
            user_id (str): The user id to authenticate with.
            passwd (str): The password associated with the provided user.

        Returns:
            HTTP Response: An HTTP redirect response upon successful login.
        """
        policy_server = urlparse(self.api_client.server).netloc
        policy = cookie_jar.DefaultCookiePolicy(
            allowed_domains=(policy_server,))
        self.cookie_jar = cookie_jar.LWPCookieJar(policy=policy)
        opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(self.cookie_jar))
        urllib.request.install_opener(opener)

        response = self.api_client.post(
            'api/login', user_id=user_id, pword=passwd)
        return response

    # ...........................
    def logout(self):
        """Log out of the server.

        Returns:
            HTTP Response: A HTTP response containing headers from the server.
        """
        response = self.api_client.get('api/v2/logout')
        return response
