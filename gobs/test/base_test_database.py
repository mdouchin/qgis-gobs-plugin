"""Base class for tests using a database."""

import os
import time

import psycopg2

from qgis.core import Qgis, QgsApplication
from qgis.testing import unittest

if Qgis.QGIS_VERSION_INT >= 30800:
    from qgis import processing
else:
    import processing

from ..processing.provider import GobsProvider as ProcessingProvider
from ..qgis_plugin_tools.tools.logger_processing import (
    LoggerProcessingFeedBack,
)

__copyright__ = "Copyright 2020, 3Liz"
__license__ = "GPL version 3"
__email__ = "info@3liz.org"
__revision__ = "$Format:%H$"


class DatabaseTestCase(unittest.TestCase):

    """Base class for tests using a database with data."""

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.cursor = None
        self.connection = None
        self.provider = None
        self.add_data = True

    def setUp(self) -> None:
        self.connection = psycopg2.connect(
            user="docker", password="docker", host="db", port="5432", database="gis"
        )
        self.cursor = self.connection.cursor()

        self.provider = ProcessingProvider()
        registry = QgsApplication.processingRegistry()
        if not registry.providerById(self.provider.id()):
            registry.addProvider(self.provider)

        self.feedback = LoggerProcessingFeedBack()

        params = {
            "CONNECTION_NAME": "test",
            "OVERRIDE": True,
            "ADD_TEST_DATA": self.add_data,
        }
        processing.run(
            "{}:create_database_structure".format(self.provider.id()),
            params,
            feedback=None,
        )

        # Setup the database connection_name
        os.environ['GOBS_CONNECTION_NAME'] = 'test'

        super().setUp()

    def tearDown(self) -> None:
        del self.cursor
        del self.connection
        del os.environ['GOBS_CONNECTION_NAME']
        time.sleep(1)
        super().tearDown()


class DatabaseWithoutDataTestCase(DatabaseTestCase):

    def __init__(self, methodName="runTest"):
        super().__init__(methodName)
        self.add_data = False
