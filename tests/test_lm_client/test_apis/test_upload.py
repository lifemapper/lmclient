import json
import os
import random

import pytest

from lm_client.client.client import LmApiClient


# ...........................................................................
class Test_occurrence_upload(object):
    def test_occurrence_upload_valid(self, data_files):
        csv_filename, meta_filename = data_files.get_occ_uploads()
        assert os.path.exists(csv_filename)
        assert os.path.exists(meta_filename)

        cl = LmApiClient()
        with open(meta_filename) as meta_in:
            metadata = json.dumps(json.load(meta_in))
        response = cl.upload.occurrence(
            csv_filename, metadata, 'test_{}'.format(
                random.randint(0, 10000)))
        print(response)
        assert response

    def test_biogeographic_hypotheses_upload_valid(self, data_files):
        bg_filename = data_files.get_bg_uploads()
        assert os.path.exists(bg_filename)

        cl = LmApiClient()
        response = cl.upload.biogeographic_hypotheses(
            bg_filename, 'test_hypotheses_{}'.format(
                random.randint(0, 10000)))
        print(response)
        assert response

    def test_tree_upload_valid(self, data_files):
        tree_filename = data_files.get_tree_uploads()
        assert os.path.exists(tree_filename)

        cl = LmApiClient()
        response = cl.upload.tree(
            tree_filename, 'test_tree_{}'.format(random.randint(0, 10000)))
        print(response)
        assert response
