"""Test configuration fixtures.
"""
import glob
import os


import pytest

# .............................................................................
# .                                 Constants                                 .
# .............................................................................
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_DATA_PATH = os.path.join(THIS_DIR, 'data_dir')


# .............................................................................
class SampleDataFiles(object):
    """This class is used to retrieve sample data for the tests.

    Note:
        * For test files, the format should be something like:
            "(in)valid_{name}.{extension}".
    """
    def get_occ_uploads(self):
        csv_filename = os.path.join(SAMPLE_DATA_PATH, 'test_occurrence.csv')
        meta_filename = os.path.join(SAMPLE_DATA_PATH, 'test_occurrence.json')
        return csv_filename, meta_filename

# .............................................................................
@pytest.fixture(scope="session")
def data_files():
    """Gets test fixture used to retrieve sample data files.

    Returns:
        A `SampleDataFiles` object.
    """
    return SampleDataFiles()
