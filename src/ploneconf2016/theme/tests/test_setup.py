# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ploneconf2016.theme.testing import PLONECONF2016_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf2016.theme is properly installed."""

    layer = PLONECONF2016_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf2016.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf2016.theme'))

    def test_browserlayer(self):
        """Test that IPloneconf2016ThemeLayer is registered."""
        from ploneconf2016.theme.interfaces import (
            IPloneconf2016ThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(IPloneconf2016ThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONECONF2016_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneconf2016.theme'])

    def test_product_uninstalled(self):
        """Test if ploneconf2016.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf2016.theme'))

    def test_browserlayer_removed(self):
        """Test that IPloneconf2016ThemeLayer is removed."""
        from ploneconf2016.theme.interfaces import \
            IPloneconf2016ThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPloneconf2016ThemeLayer, utils.registered_layers())
