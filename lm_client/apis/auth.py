"""Module containing authentication service calls
"""
import cookielib
import json
from urlparse import urlparse

from lm_client.common.api_service import ApiService

# .............................................................................
class AuthApiService(ApiService):
    """
    """
    # ...........................
    def login(self, user_id, passwd, raw=False):
        """
        """
        policy_server = urlparse(self.api_client.server).netloc
        policy = cookielib.DefaultCookiePolicy(
            allowed_domains=(policy_server,))
        self.cookie_jar = cookielib.LWPCookieJar(policy=policy)
        opener = urllib2.build_opener(
            urllib2.HTTPCookieProcessor(self.cookie_jar))
        urllib2.install_opener(opener)

        response = self.api_client.post(self,
            'api/v2/login', user_id=user_id, pword=passwd)
        if raw:
            return response
        else:
            return json.load(response)

    # ...........................
    def logout(self, raw=False):
        
        response = self.api_client.get(self, 'api/v2/logout')
        if raw:
            return response
        else:
            return json.load(response)
