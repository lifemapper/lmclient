"""Tests for SDM BOOM jobs initiated by backend."""
import csv
import os
from random import randint, random

from lmclient.client.client import LmApiClient
import lmtest.base.test_base as test_base


# .....................................................................................
class BoomJobSubmissionTest(test_base.LmTest):
    """Test of job submission for SDM BOOM."""

    # .............................
    def __init__(
        self,
        user_id,
        passwd,
        server,
        config,
        wait_timeout,
        delay_time=0,
        delay_interval=3600,
    ):
        """Construct the simulated submission test.

        Args:
            user_id (str): The Lifemapper username to perform this test.
            passwd (str): The password of the specified Lifemapper test user.
            server (str): The base Lifemapper server URL to test against.
            config (dict): A dictionary of job submission parameters.
            wait_timeout (int): The number of seconds to wait for a job to complete
                before failing.
            delay_time (int): The number of seconds to wait before running the test.
            delay_interval (int): The number of seconds to wait between test runs.
        """
        test_base.LmTest.__init__(self, delay_time=delay_time)
        self.wait_timeout = wait_timeout
        self.user_id = user_id
        self.passwd = passwd
        self.server = server
        self.boom_config = config

        # Create a random value used for filenames
        rand_val = randint(0, 99999)
        self._replace_lookup = {
            'TEST_USER': user_id,
            'ARCHIVE_NAME': 'Auto_test-{}'.format(rand_val),
            'OCCURRENCE_FILENAME': 'Auto_test_occ-{}'.format(rand_val),
        }
        self.test_name = 'lmclient SDM BOOM Job test (user: {}, archive: {})'.format(
            user_id, self._replace_lookup['ARCHIVE_NAME']
        )
        self.client = LmApiClient(server=server)

    # .............................
    def __repr__(self):
        """Return a string representation of this instance.

        Returns:
            str: A string representation of this test object.
        """
        return self.test_name

    # .............................
    def _generate_random_occurrences(self, num_species, min_points, max_points):
        """Generate random points for this test.

        Args:
            num_species (int): Number of species to include in this run.
            min_points (int): Minimum number of points per species.
            max_points (int): Maximum number of points per species.

        Returns:
            tuple (str, dict, str): A tuple of csv file path, metadata dictionary,
                occurrence set name for the generated occurrence data.
        """
        csv_filename = os.path.join(
            self.user_dir, '{}.csv'.format(self._replace_lookup['OCCURRENCE_FILENAME'])
        )
        with open(csv_filename, mode='wt') as out_file:
            out_file.write('Species,Longitude,Latitude\n')
            for i in range(num_species):
                for _ in range(randint(min_points, max_points)):
                    out_file.write(
                        '{},{},{}\n'.format(
                            'Species {}'.format(i),
                            360.0 * random() - 180.0,
                            180.0 * random() - 90.0,
                        )
                    )
        point_meta = {
            '0': {'name': 'Species', 'role': 'taxaName', 'type': 'string'},
            '1': {'name': 'Longitude', 'role': 'longitude', 'type': 'real'},
            '2': {'name': 'Latitude', 'role': 'latitude', 'type': 'real'},
        }
        return (csv_filename, point_meta, self._replace_lookup['OCCURRENCE_FILENAME'])

    # .............................
    def _replace_dict_vals(self, val_dict):
        """Replace templated dictionary values recursively.

        Args:
            val_dict (dict): A dictionary to recurse through and replace values.
        """
        for k in val_dict.keys():
            if isinstance(val_dict[k], dict):
                self._replace_dict_vals(val_dict[k])
            else:
                val_dict[k] = self._replace_val(val_dict[k])

    # .............................
    def _generate_experiment_config(self):
        """Generate a SDM BOOM job configuration file."""
        self._replace_dict_vals(self.boom_config)

    # .............................
    def _replace_val(self, value):
        """Fill in any templated strings in value.

        Args:
            value (str): A string potentially containing a template value.

        Returns:
            str: A value with templates replaced.
        """
        parts = str(value).split('$')
        # Replace odd values with lookup replace values.
        for i in range(1, len(parts), 2):
            parts[i] = self._replace_lookup[parts[i]]
        return ''.join(parts)

    # .............................
    def run_test(self):
        """Run the test.

        Raises:
            LmTestFailure: Raised if the test fails.
        """
        num_species = 10
        min_points = 200
        max_points = 1000
        try:
            # Log in
            self.client.api.auth.login(self.user_id, self.passwd)

            # Create point file
            (
                points_filename,
                points_metadata,
                occurrences_name
            ) = self._generate_random_occurrences(num_species, min_points, max_points)

            # Post points
            self.client.api.upload.occurrence(
                points_filename, points_metadata, occurrences_name
            )

            # Create config file
            self._generate_experiment_config()
            # Post experiment request
            post_response = self.client.api.gridset.post(self.boom_config)

            # Get grideset ID
            gridset_id = post_response['id']

            # Add waiting test
            self.add_new_test(
                BoomWaitTest(
                    gridset_id,
                    self.user_id,
                    self.passwd,
                    self.server,
                    self.wait_timeout
                )
            )

            # Log out
            self.client.api.auth.logout()

        except Exception as err:
            raise test_base.LmTestFailure(
                'Failed to submit test job: {}'.format(err)
            ) from err


# .............................................................................
class BoomWaitTest(test_base.LmTest):
    """Waiting test for a gridset computations to complete."""

    # .............................
    def __init__(
        self,
        gridset_id,
        user_id,
        passwd,
        server,
        wait_timeout,
        delay_time=0,
        delay_interval=120
    ):
        """Construct the instance.

        Args:
            gridset_id (int): The identifier of the gridset to request.
            user_id (str): The Lifemapper username to perform this test.
            passwd (str): The password of the specified Lifemapper test user.
            server (str): The base Lifemapper server URL to test against.
            wait_timeout (int): The number of seconds to wait for a job to complete
                before failing.
            delay_time (int): The number of seconds to wait before running the test.
            delay_interval (int): The number of seconds to wait between test runs.
        """
        test_base.LmTest.__init__(self, delay_time=delay_time)
        self.user_id = user_id
        self.passwd = passwd
        self.server = server
        self.gridset_id = gridset_id
        self.wait_timeout = wait_timeout
        self.test_name = 'Waiting test for gridset id: {}'.format(self.gridset_id)
        self.delay_interval = delay_interval
        self.client = LmApiClient(server=server)

    # .............................
    def __repr__(self):
        """Return a string representation of this instance.

        Returns:
            str: A string representation of this test object.
        """
        return self.test_name

    # .............................
    def run_test(self):
        """Run the test.

        Raises:
            LmTestFailure: Raised if the test fails.
            Exception: Raised for now.
        """
        # Log in
        self.client.api.auth.login(self.user_id, self.passwd)

        # Check if gridset is finished
        gridset = self.client.api.gridset.get(self.gridset_id)

        # Log out
        self.client.api.auth.logout()

        # Check if the gridset is complete
        raise Exception(gridset)
        waiting = False

        # If still waiting, check that we should
        if waiting:
            if self.wait_timeout < 0:
                raise test_base.LmTestFailure(
                    'Wait timeout reached for gridset {}'.format(self.gridset_id)
                )
            # Still time? Add new test
            self.add_new_test(
                BoomWaitTest(
                    self.gridset_id,
                    self.user_id,
                    self.passwd,
                    self.server,
                    self.wait_timeout - self.delay_interval,
                    delay_time=self.delay_interval,
                    delay_interval=self.delay_interval,
                )
            )
        else:
            # Finished? Validate it
            self.add_new_test(
                BoomValidateTest(
                    self.gridset_id,
                    self.user_id,
                    self.passwd,
                    self.server
                )
            )


# .............................................................................
class BoomValidateTest(test_base.LmTest):
    """Gridset validation test."""

    # .............................
    def __init__(
        self,
        gridset_id,
        user_id,
        passwd,
        server,
        delay_time=0,
        delay_interval=60
    ):
        """Construct the instance.

        Args:
            gridset_id (int): The identifier of the gridset to request.
            user_id (str): The Lifemapper username to perform this test.
            passwd (str): The password of the specified Lifemapper test user.
            server (str): The base Lifemapper server URL to test against.
            delay_time (int): The number of seconds to wait before running the test.
            delay_interval (int): The number of seconds to wait between test runs.
        """
        test_base.LmTest.__init__(self, delay_time=delay_time)
        self.user_id = user_id
        self.passwd = passwd
        self.server = server
        self.gridset_id = gridset_id
        self.test_name = 'Gridset {} validation test'.format(self.gridset_id)
        self.client = LmApiClient(server=server)

    # .............................
    def __repr__(self):
        """Return a string representation of this instance.

        Returns:
            str: A string representation of this test object.
        """
        return self.test_name

    # .............................
    def run_test(self):
        """Run the test.

        Raises:
            LmTestFailure: Raised if there is a problem with one of the objects.
        """
        # Log in
        self.client.api.auth.login(self.user_id, self.passwd)

        # Get occurence sets
        occurrence_sets = self.client.api.occurrence.list(
            gridset_id=self.gridset_id,
            limit=1000,
            offset=0,
        )
        # Test occurrence sets
        for occ_atom in occurrence_sets:
            occ_id = occ_atom['id']
            occ_meta = self.client.api.occurrence.get(occ_id)
            occ_status = int(occ_meta['status'])
            # Fail if unknown error
            if occ_status == 1000:
                raise test_base.LmTestFailure(
                    'Unknown error for occurrence set {} from gridset {}'.format(
                        occ_id, self.gridset_id
                    )
                )
            # Fail if not complete
            if occ_status < 300:
                raise test_base.LmTestFailure(
                    'Occurrence set {} did not complete for gridset {}'.format(
                        occ_id, self.gridset_id
                    )
                )
            # If complete, retrieve it
            if occ_status == 300:
                occ_csv_resp = self.client.api.occurrence.get(occ_id, interface='csv')
                # Check content type to be sure it is csv
                if occ_csv_resp.header['Content-Type'].lower() == 'text/csv':
                    # Check that it looks like csv
                    try:
                        reader = csv.reader(occ_csv_resp.body)
                        _ = [rec for rec in reader]
                    except Exception as err:
                        raise test_base.LmTestFailure(
                            'Occurrence set csv seems wrong... {}'.format(err)
                        )
                else:
                    raise test_base.LmTestFailure(
                        'Incorrect content type for occurrence set {} csv: {}'.format(
                            occ_id, occ_csv_resp.header['Content-Type']
                        )
                    )

        # Get projections
        projections = self.client.api.sdm_project.list(
            gridset_id=self.gridset_id,
            limit=1000,
            offset=0,
        )
        # Test projections
        for prj_atom in projections:
            prj_id = prj_atom['id']
            prj_meta = self.client.api.sdm_project.get(prj_id)
            prj_status = int(prj_meta['status'])
            # Fail if unknown error
            if prj_status == 1000:
                raise test_base.LmTestFailure(
                    'Unknown error for projection {} from gridset {}'.format(
                        prj_id, self.gridset_id
                    )
                )
            # Fail if not complete
            if prj_status < 300:
                raise test_base.LmTestFailure(
                    'Projection {} did not complete for gridset {}'.format(
                        prj_id, self.gridset_id
                    )
                )
            # If complete, retrieve it
            if prj_status == 300:
                prj_gtiff_resp = self.client.api.sdm_project.get(
                    prj_id, interface='Gtiff'
                )
                # Make sure that the content type is image/tiff
                # Check content type to be sure it is ascii
                if prj_gtiff_resp.header['Content-Type'].lower() != 'image/tiff':
                    raise test_base.LmTestFailure(
                        'Incorrect content type for projection {} geotiff: {}'.format(
                            prj_id, prj_gtiff_resp.header['Content-Type']
                        )
                    )

        # Log out
        self.client.api.auth.logout()
