# -*- coding: utf-8 -*-
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    copyright            : (C) 2015 by Sandro Mani / Sourcepole AG
#    email                : smani@sourcepole.ch

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtXml import *
from qgis.core import *
from qgis.gui import *
import os
import json
from UpstreamDownstreamDialog import UpstreamDownstreamDialog
from SetupDialog import SetupDialog
import resources


class REC2Plugin(QObject):
    def __init__(self, iface):
        QObject.__init__(self)
        self.iface = iface
        self.pluginDir = os.path.dirname(__file__)
        self.toolbar = self.iface.addToolBar(u'Rec2')
        self.toolbar.setObjectName(u'Rec2')

    def initGui(self):
        self.actionUpstreamDownstream = QAction(QIcon(':/plugins/rec2/icons/icon.png'), "NIWA Rec2", self)
        self.actionUpstreamDownstream.triggered.connect(self.__showUpstreamDownstreamDialog)

        self.iface.newProjectCreated.connect(self.__onProjectCreated)
        self.toolbar.addAction(self.actionUpstreamDownstream)
        self.iface.addPluginToWebMenu("Rec2",  self.actionUpstreamDownstream)

        # When reloading plugin, attempt to use currently loaded project
        self.__onProjectRead()

    def unload(self):
        try:
            self.menu.deleteLater()
        except:
            pass
        try:
            self.upstreamDownstreamDialog.deleteLater()
        except:
            pass
        try:
            self.toolbar.deleteLater()
        except:
            pass


    def __onProjectRead(self):
        reg = QgsMapLayerRegistry.instance()
        self.recLayer = reg.mapLayer(QgsProject.instance().readEntry("fishdb", "recLayer", "")[0])

    def __showUpstreamDownstreamDialog(self):
        try:
            self.upstreamDownstreamDialog.deleteLater()
        except:
            pass
        self.upstreamDownstreamDialog = UpstreamDownstreamDialog(self.iface, self.recLayer, self.iface.mainWindow())
        self.upstreamDownstreamDialog.show()
