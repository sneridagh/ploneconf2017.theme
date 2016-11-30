# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ploneconf2017.theme


class ploneconf2017ThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ploneconf2017.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ploneconf2017.theme:default')


ploneconf2017_THEME_FIXTURE = ploneconf2017ThemeLayer()


ploneconf2017_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ploneconf2017_THEME_FIXTURE,),
    name='ploneconf2017ThemeLayer:IntegrationTesting'
)


ploneconf2017_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ploneconf2017_THEME_FIXTURE,),
    name='ploneconf2017ThemeLayer:FunctionalTesting'
)


ploneconf2017_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ploneconf2017_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ploneconf2017ThemeLayer:AcceptanceTesting'
)
