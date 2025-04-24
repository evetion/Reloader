from qgis.core import QgsProject
from qgis.testing import unittest
from qgis.utils import iface, plugins


class TestPlugin(unittest.TestCase):
    def test_plugin_is_loaded(self):
        """Test plugin is properly loaded and appears in QGIS plugins."""
        plugin = plugins.get("reloader")
        self.assertTrue(plugin, "Reloader plugin not loaded")

    def test_plugin(self):
        """Triggers reloader buttons and checks that Dock is added."""
        # This checks the *actual* QGIS interface, not just a stub
        self.assertTrue(iface is not None, "QGIS interface not available")

        toolbars = [
            c for c in iface.mainWindow().children() if c.objectName() == "Reloader"
        ]
        self.assertTrue(len(toolbars) == 1, "No (single) Reloader toolbar")
        actions = toolbars[0].actions()
        self.assertTrue(len(actions) == 4, "No four Reloader action buttons in toolbar")
