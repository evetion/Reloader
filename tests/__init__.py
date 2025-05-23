import sys

import coverage
from qgis.testing import unittest
from qgis.utils import iface


def run_all():
    try:
        cov = coverage.Coverage(config_file=".coveragerc")
        test_loader = unittest.defaultTestLoader
        test_suite = test_loader.discover(".", pattern="test_*.py")
        cov.start()
        result = unittest.TextTestRunner(verbosity=3, stream=sys.stdout).run(test_suite)
        cov.stop()
        cov.save()
        cov.xml_report(outfile="tests/coverage.xml")
        success = result.wasSuccessful()
    except Exception as e:
        print(f"Error running tests: {e}")
        success = False

    print(f"Reloader tests ok: {success}")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    iface.initializationCompleted.connect(run_all)
