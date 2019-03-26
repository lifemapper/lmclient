"""Module containing authentication service calls
"""
import http.cookiejar
import json
from urlparse import urlparse

from lm_client.common.api_service import ApiService


# .............................................................................
class AuthApiService(ApiService):
    """
    """
    # ...........................
    def login(self, user_id, passwd):
        """
        """
        policy_server = urlparse(self.api_client.server).netloc
        policy = http.cookiejar.DefaultCookiePolicy(
            allowed_domains=(policy_server,))
        self.cookie_jar = http.cookiejar.LWPCookieJar(policy=policy)
        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cookie_jar))
        urllib2.install_opener(opener)

        response = self.api_client.post(
            'api/v2/login', user_id=user_id, pword=passwd)
        return response

    # ...........................
    def logout(self):

        response = self.api_client.get('api/v2/logout')
        return response
