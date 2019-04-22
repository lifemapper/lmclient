"""Test module for constants
"""
from lm_client.common.constants import HttpStatus, INTERFACES


# .............................................................................
class Test_HttpStatus(object):
    """Test the HttpStatus constant class.
    """
    # ...........................
    def test_constant_types(self):
        """Tests that all constant values integers
        """
        for att in dir(HttpStatus):
            if not att.startswith('_'):
                val = getattr(HttpStatus(), att)
                assert isinstance(val, int)


# .............................................................................
class Test_INTERFACES(object):
    """Test the INTERFACES constant class.
    """
    # ...........................
    def test_constant_types(self):
        """Tests that all constant values are lower-case strings.
        """
        for interface in INTERFACES.binary_interfaces():
            assert interface == interface.lower()
        for interface in INTERFACES.json_interfaces():
            assert interface == interface.lower()
        for interface in INTERFACES.text_interfaces():
            assert interface == interface.lower()
