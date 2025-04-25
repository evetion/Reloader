import os
import signal
import sys

import coverage
from qgis.core import QgsApplication
from qgis.testing import unittest


def run_all():
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover(".", pattern="test_*.py")

    cov = coverage.Coverage(config_file=".coveragerc")
    cov.start()
    try:
        result = unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)
        success = result.wasSuccessful()

        cov.stop()
        cov.save()
        cov.xml_report(outfile="tests/coverage.xml")
    except Exception as e:
        print(f"Error running tests: {e}")
        success = False

    app = QgsApplication.instance()
    os.kill(app.applicationPid(), signal.SIGTERM)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    run_all()
