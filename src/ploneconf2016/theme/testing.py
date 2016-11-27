# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf2016.theme


class Ploneconf2016ThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf2016.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf2016.theme:default')


PLONECONF2016_THEME_FIXTURE = Ploneconf2016ThemeLayer()


PLONECONF2016_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONECONF2016_THEME_FIXTURE,),
    name='Ploneconf2016ThemeLayer:IntegrationTesting'
)


PLONECONF2016_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONECONF2016_THEME_FIXTURE,),
    name='Ploneconf2016ThemeLayer:FunctionalTesting'
)


PLONECONF2016_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONECONF2016_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Ploneconf2016ThemeLayer:AcceptanceTesting'
)
