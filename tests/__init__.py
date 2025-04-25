import os
import signal
import sys

import coverage
from qgis.core import QgsApplication
from qgis.testing import unittest
from qgis.utils import iface


def run_all():
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover(".", pattern="test_*.py")

    cov = coverage.Coverage(config_file=".coveragerc")
    cov.start()
    try:
        result = unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)
        cov.stop()
        cov.save()
        cov.xml_report(outfile="tests/coverage.xml")
        success = result.wasSuccessful()
        print(result)
        print(success)
    except Exception as e:
        print(f"Error running tests: {e}")
        success = False

    app = QgsApplication.instance()
    os.kill(app.applicationPid(), signal.SIGTERM)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    iface.initializationCompleted.connect(run_all)
