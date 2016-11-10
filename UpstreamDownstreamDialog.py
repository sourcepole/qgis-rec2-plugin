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
from PyQt4.QtNetwork import *
from qgis.core import *
from qgis.gui import *
import re
from ui_UpstreamDownstreamDialog import Ui_UpstreamDownstreamDialog
from SetupDialog import SetupDialog


DOWNSTREAM_URL = "http://gs.niwa.co.nz/niwa/wms?viewparams=hydroid:%s&layers=rec2_trace_downstream&styles=&IgnoreGetMapUrl=1"
UPSTREAM_URL = "http://gs.niwa.co.nz/niwa/wms?viewparams=hydroid:%s&layers=rec2_trace_upstream&styles=&IgnoreGetMapUrl=1"


class PointSelectTool(QgsMapTool):

    pointSelected = pyqtSignal(QgsPoint)

    def __init__(self, iface):
        QgsMapTool.__init__(self, iface.mapCanvas())
        self.iface = iface

    def canvasReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            p = self.iface.mapCanvas().getCoordinateTransform().toMapCoordinates(e.pos())
            self.pointSelected.emit(p)


class UpstreamDownstreamDialog(QDialog, Ui_UpstreamDownstreamDialog):
    def __init__(self, iface, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.pushButtonSetup = self.buttonBox.addButton(self.tr("Setup"), QDialogButtonBox.ActionRole)
        self.iface = iface
        self.recLayer = None
        setupDialog = SetupDialog(self.iface.mainWindow())

        reg = QgsMapLayerRegistry.instance()
        for layer in QgsMapLayerRegistry.instance().mapLayers().values():
            if(layer.source() == "url=%s&crs=EPSG:2193&format=image/png" % setupDialog.getRecLayerURL()):
                self.recLayer = reg.mapLayer(layer.id())

        self.selectTool = PointSelectTool(self.iface)
        self.selectTool.pointSelected.connect(
            lambda p: self.lineEditPosition.setText("%f %f" % (p.x(), p.y())))

        self.lineEditPosition.setValidator(QRegExpValidator(QRegExp("^([-+]?[0-9]*\.?[0-9]+)\s+([-+]?[0-9]*\.?[0-9]+)$")))
        self.lineEditPosition.textChanged.connect(
            lambda: self.pushButtonSearchDownstream.setEnabled(self.lineEditPosition.hasAcceptableInput()))
        self.lineEditPosition.textChanged.connect(
            lambda: self.pushButtonSearchUpstream.setEnabled(self.lineEditPosition.hasAcceptableInput()))

        self.toolButtonSelectPosition.setIcon(QIcon(":/images/themes/default/mActionSelect.svg"))
        self.toolButtonSelectPosition.clicked.connect(
            lambda: self.iface.mapCanvas().setMapTool(self.selectTool))

        self.pushButtonSearchDownstream.clicked.connect(
            lambda: self.__addLayer(DOWNSTREAM_URL, "Downstream"))
        self.pushButtonSearchUpstream.clicked.connect(
            lambda: self.__addLayer(UPSTREAM_URL, "Upstream"))

        self.pushButtonSetup.clicked.connect(self.__showSetupDialog)
        self.toolButtonSelectPosition.setEnabled(self.recLayer is not None)

        QgsMapLayerRegistry.instance().layerWillBeRemoved.connect(self.__checkLayerRemoved)

    def __checkLayerRemoved(self, layerid):
        layer = QgsMapLayerRegistry.instance().mapLayer(layerid)
        if layer == self.recLayer:
            self.recLayer = None
            self.toolButtonSelectPosition.setEnabled(False)
            self.lineEditPosition.setText("")

    def __showSetupDialog(self):
            setupDialog = SetupDialog(self.iface.mainWindow())
            if setupDialog.exec_() != QDialog.Accepted:
                return

            if self.recLayer is not None:
                result = QMessageBox.question(self, 'Replace Layer?', "There seems to already be a REC layer in the project. Are you sure you wish to overwrite it?", QMessageBox.No | QMessageBox.Yes)
                if result == QMessageBox.No:
                    return
                QgsMapLayerRegistry.instance().removeMapLayer(self.recLayer.id())

            # Sets Coordinate System
            layers = self.iface.legendInterface().layers()
            if(layers):
                self.iface.mapCanvas().setCrsTransformEnabled(True)
                self.iface.mapCanvas().setDestinationCrs(QgsCoordinateReferenceSystem(2193, QgsCoordinateReferenceSystem.EpsgCrsId))

            self.iface.mainWindow().setCursor(Qt.BusyCursor)

            self.recLayer = QgsRasterLayer("url=%s&crs=EPSG:2193&format=image/png" % setupDialog.getRecLayerURL(), setupDialog.getRecLayerTitle(), "wms")

            if self.recLayer is None:
                self.iface.mainWindow().unsetCursor()
                QMessageBox.warning(self.iface.mainWindow(), "Invalid layer", "The REC network layer is invalid. Cannot continue.")
                return

            QgsMapLayerRegistry.instance().addMapLayers([self.recLayer])

            self.iface.mainWindow().unsetCursor()
            self.toolButtonSelectPosition.setEnabled(True)

    def __addLayer(self, url, title):

        if self.recLayer is None:
            return

        r = self.lineEditPosition.validator().regExp()
        p = QgsPoint(float(r.cap(1)), float(r.cap(2)))
        p = self.iface.mapCanvas().mapSettings().mapToLayerCoordinates(self.recLayer, p)
        viewWidth = self.iface.mapCanvas().extent().width()
        viewHeight = self.iface.mapCanvas().extent().height()
        extent = QgsRectangle(p.x() - 0.5 * viewWidth, p.y() - 0.5 * viewHeight,
                              p.x() + 0.5 * viewWidth, p.y() + 0.5 * viewHeight)
        width = viewWidth / self.iface.mapCanvas().mapUnitsPerPixel()
        height = viewHeight / self.iface.mapCanvas().mapUnitsPerPixel()

        res = self.recLayer.dataProvider().identify(p, QgsRaster.IdentifyFormatText, extent, width, height)
        try:
            hydroid = re.search(r"hydroid\s*=\s*(\d+)", res.results()[0]).group(1)
        except:
            QMessageBox.warning(self, "No Reach", "Could not find any reach at the specified location.")
            return

        layer = QgsRasterLayer("url=%s&crs=EPSG:2193&format=image/png"
                               % (url % hydroid), "%s %s" % (title, hydroid), "wms")
        QgsMapLayerRegistry.instance().addMapLayer(layer)
