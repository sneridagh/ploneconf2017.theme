# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from ploneconf2017.theme.testing import ploneconf2017_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that ploneconf2017.theme is properly installed."""

    layer = ploneconf2017_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ploneconf2017.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'ploneconf2017.theme'))

    def test_browserlayer(self):
        """Test that Iploneconf2017ThemeLayer is registered."""
        from ploneconf2017.theme.interfaces import (
            Iploneconf2017ThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(Iploneconf2017ThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ploneconf2017_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ploneconf2017.theme'])

    def test_product_uninstalled(self):
        """Test if ploneconf2017.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'ploneconf2017.theme'))

    def test_browserlayer_removed(self):
        """Test that Iploneconf2017ThemeLayer is removed."""
        from ploneconf2017.theme.interfaces import \
            Iploneconf2017ThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(Iploneconf2017ThemeLayer, utils.registered_layers())
