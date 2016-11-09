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

from AboutDialog.AboutDialog import AboutDialog
from UpstreamDownstreamDialog import UpstreamDownstreamDialog
from SetupDialog import SetupDialog


class REC2Plugin(QObject):
    def __init__(self, iface):
        QObject.__init__(self)
        self.iface = iface
        self.pluginDir = os.path.dirname(__file__)

    def initGui(self):
        self.actionSetup = QAction("Setup", self)
        self.actionSep1 = QAction("", self)
        self.actionUpstreamDownstream = QAction("Upstream/Downstream search", self)
        self.actionSep2 = QAction("", self)
        self.actionAbout = QAction("About", self)

        self.actionSep1.setSeparator(True)
        self.actionSep2.setSeparator(True)

        self.actionSetup.triggered.connect(self.__showSetupDialog)
        self.actionUpstreamDownstream.triggered.connect(self.__showUpstreamDownstreamDialog)
        self.actionAbout.triggered.connect(self.__showAboutDialog)

        self.menu = QMenu("REC2")
        self.menu.addAction(self.actionSetup)
        self.menu.addAction(self.actionSep1)
        self.menu.addAction(self.actionUpstreamDownstream)
        self.menu.addAction(self.actionSep2)
        self.menu.addAction(self.actionAbout)
        self.iface.mainWindow().menuBar().addMenu(self.menu)

        self.actionGroup = QActionGroup(self)
        self.actionGroup.addAction(self.actionUpstreamDownstream)
        self.actionGroup.setEnabled(False)

        self.iface.projectRead.connect(self.__onProjectRead)
        self.iface.newProjectCreated.connect(self.__onProjectCreated)

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
            self.nearbyObservationsDialog.deleteLater()
        except:
            pass

    def __showSetupDialog(self):
        setupDialog = SetupDialog(self.iface.mainWindow())
        if setupDialog.exec_() != QDialog.Accepted:
            return

        self.iface.newProject(True)
        # If new project was not created
        if QgsProject.instance().isDirty():
            return

        self.iface.mainWindow().setCursor(Qt.BusyCursor)

        self.recLayer = QgsRasterLayer("url=%s&crs=EPSG:2193&format=image/png" % setupDialog.getRecLayerURL(), setupDialog.getRecLayerTitle(), "wms")

        if not self.recLayer.isValid():
            self.iface.mainWindow().unsetCursor()
            QMessageBox.warning(self.iface.mainWindow(), "Invalid layer", "The REC network layer is invalid. Cannot continue.")
            return

        QgsMapLayerRegistry.instance().addMapLayers([self.recLayer])

        # TODO: There is a race condition, this is called before QGIS
        # internally sets the extent to the extent of all loaded layers, and
        # hence does not work...
        # if self.basLayer.isValid():
        #     self.iface.mapCanvas().setExtent(self.basLayer.extent())
        #     self.iface.mapCanvas().refresh()

        self.actionGroup.setEnabled(True)

        self.iface.mainWindow().unsetCursor()
        QgsProject.instance().writeEntry("fishdb", "recLayer", self.recLayer.id())

    def __onProjectCreated(self):
        self.actionGroup.setEnabled(False)

    def __onProjectRead(self):
        reg = QgsMapLayerRegistry.instance()
        self.recLayer = reg.mapLayer(QgsProject.instance().readEntry("fishdb", "recLayer", "")[0])
        self.actionGroup.setEnabled((self.recLayer != None and self.recLayer.isValid()))

    def __showUpstreamDownstreamDialog(self):
        try:
            self.upstreamDownstreamDialog.deleteLater()
        except:
            pass
        self.upstreamDownstreamDialog = UpstreamDownstreamDialog(self.iface, self.recLayer, self.iface.mainWindow())
        self.upstreamDownstreamDialog.show()

    def __showAboutDialog(self):
        AboutDialog(self.pluginDir, self.iface.mainWindow()).exec_()
