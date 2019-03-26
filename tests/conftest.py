"""Test configuration fixtures.
"""
from contextlib import contextmanager
import glob
import os


import pytest
from lm_client.client.client import LmApiClient


# .............................................................................
# .                                 Constants                                 .
# .............................................................................
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DATA_PATH = os.path.join(THIS_DIR, 'data_dir')


# .............................................................................
class ClientGetter(object):
    """Helper class to get a client
    """
    def __init__(self, user, passwd):
        """Constructor
        """
        self.user = user
        self.passwd = passwd
    
    @contextmanager
    def get_client(self):
        cl = LmApiClient()
        if self.user is not None and self.passwd is not None:
            cl.auth.login(self.user, self.passwd)
        yield cl
        cl.auth.logout()


# .............................................................................
class SampleDataFiles(object):
    """This class is used to retrieve sample data for the tests.

    Note:
        * For test files, the format should be something like:
            "(in)valid_{name}.{extension}".
    """
    def get_bg_uploads(self):
        bg_filename = os.path.join(SAMPLE_DATA_PATH, 'test_biogeo.zip')
        return bg_filename

    def get_occ_uploads(self):
        csv_filename = os.path.join(SAMPLE_DATA_PATH, 'test_occurrence.csv')
        meta_filename = os.path.join(SAMPLE_DATA_PATH, 'test_occurrence.json')
        return csv_filename, meta_filename

    def get_tree_uploads(self):
        tree_filename = os.path.join(SAMPLE_DATA_PATH, 'test_tree.tre')
        return tree_filename

# .............................................................................
@pytest.fixture(scope='session')
def data_files():
    """Gets test fixture used to retrieve sample data files.

    Returns:
        A `SampleDataFiles` object.
    """
    return SampleDataFiles()

# .............................................................................
@pytest.fixture
#def get_client_generators(config_file):
def get_client_generators():
    client_generators = [ClientGetter(None, None)]
    # Read config file for user and password combinations
    config_file = None
    if config_file is not None:
        with open(config_file) as in_file:
            # Add client getters
            for line in in_file:
                usr, pwd = line.strip().split(' ')
                client_generators.append(ClientGetter(usr, pwd))
    return client_generators

# .............................................................................
def pytest_addoption(parser):
    """Adds a command line option to pytest
    """
    parser.addoption('--config_file', type=str, default=None,
                     help='Configuration file containing test users')

# .............................................................................
def pytest_generate_tests(metafunc):
    """Fill in client_generator fixtures when generating tests
    """
    if 'client_generator' in metafunc.fixturenames:
        metafunc.parametrize(
            'client_generator', get_client_generators())
                #metafunc.config.getoption('config_file')))

