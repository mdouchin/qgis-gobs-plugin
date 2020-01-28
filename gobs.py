# -*- coding: utf-8 -*-

"""
/***************************************************************************
 Gobs
                                 A QGIS plugin
 This plugin provides tools to store and manage spatial and time data in a standardized way
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-02-15
        copyright            : (C) 2019 by 3liz
        email                : info@3liz.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = '3liz'
__date__ = '2019-02-15'
__copyright__ = '(C) 2019 by 3liz'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import (
    QgsProcessingAlgorithm,
    QgsApplication,
    QgsSettings
)
from qgis.PyQt.QtCore import (
    Qt,
    QTranslator,
    QCoreApplication
)
from .processing.provider import GobsProvider
from .gobs_dockwidget import GobsDockWidget
from .processing.algorithms.tools import resources_path

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class GobsPlugin(object):

    def __init__(self, iface):
        self.provider = None
        self.dock = None
        self.iface = iface

        try:
            locale = QgsSettings().value('locale/userLocale', 'en')[0:2]
        except AttributeError:
            locale = 'en'
        locale_path = resources_path('i18n', '{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

    def initProcessing(self):
        """Load the Processing provider. QGIS 3.8."""
        self.provider = GobsProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)


    def initGui(self):
        self.initProcessing()
        self.dock = GobsDockWidget(self.iface)
        self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dock)


    def unload(self):
        self.iface.removeDockWidget(self.dock)
        self.dock.deleteLater()

        QgsApplication.processingRegistry().removeProvider(self.provider)
