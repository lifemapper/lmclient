"""Tests the env_layer service end-point
"""
import json
import os
import random

import pytest

from lm_client.client.client import LmApiClient


# .............................................................................
class Test_env_layer_api_service_anon(object):
    """This class anonymously tests the environmental layers service
    """
    # ...........................
    def test_count_no_parameters(self):
        """Tests count without providing any parameters
        """
        cl = LmApiClient()
        env_layer_count = cl.env_layer.count()
        assert env_layer_count >= 0

    # ...........................
    def test_count_with_bad_parameter_values(self):
        """Tests count with invalid parameter values
        """
        cl = LmApiClient()
        env_layer_count = cl.env_layer.count(after_time='bad_value')
        assert env_layer_count == 0

    # ...........................
    def test_count_with_parameters(self):
        """Tests count with parameters
        """
        pass
