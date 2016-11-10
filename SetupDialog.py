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
from qgis.core import *
from qgis.gui import *
from ui_SetupDialog import Ui_SetupDialog

import json
import os


class SetupDialog(QDialog, Ui_SetupDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        self.__setupUrlCombo(self.comboBoxRecWMS, self.toolButtonRecWMSAdd, self.toolButtonRecWMSRemove, "Rec")

        self.buttonBox.button(QDialogButtonBox.RestoreDefaults).clicked.connect(self.__restoreDefaults)

    def getAllRecLayerUrls(self):
        combo = self.comboBoxRecWMS
        return [combo.itemText(i) for i in range(0, combo.count())]

    def getRecLayerURL(self):
        return self.comboBoxRecWMS.currentText()

    def getRecLayerTitle(self):
        return self.lineEditRecTitle.text()

    def __setupUrlCombo(self, combo, addBtn, removeBtn, settingskey):
        # Entries which are already present are default entries
        for i in range(0, combo.count()):
            combo.setItemData(i, True)

        # Add user-added entries
        entries = QSettings().value("FishDBPlugin/%s/Items" % settingskey)
        if entries:
            for entry in entries:
                combo.addItem(entry, False)

        # Remove button
        removeBtn.setVisible(False)
        combo.currentIndexChanged.connect(
            lambda: removeBtn.setVisible(not combo.itemData(combo.currentIndex())))
        removeBtn.clicked.connect(
            lambda: combo.removeItem(combo.currentIndex()))

        # Add button
        addBtn.clicked.connect(lambda: self.__addUrl(combo))

        # Line-edit sensitivity
        combo.currentIndexChanged.connect(
            lambda: combo.lineEdit().setReadOnly(combo.currentIndex() < 0 or combo.itemData(combo.currentIndex())))
        combo.lineEdit().textChanged.connect(
            lambda: self.__updateUrl(combo))

        # Set current index
        active = QSettings().value("FishDBPlugin/%s/Default" % settingskey)
        combo.setCurrentIndex(-1)
        if combo.count() > 0:
            if active >= 0 and active < combo.count():
                combo.setCurrentIndex(active)
            else:
                combo.setCurrentIndex(0)

        # Store default
        combo.currentIndexChanged.connect(
            lambda: QSettings().setValue("FishDBPlugin/%s/Default" % settingskey, combo.currentIndex()))

    def __addUrl(self, combo):
        (url, success) = QInputDialog.getText(self, "Add URL", "URL:")
        if url:
            combo.addItem(url, False)
            combo.setCurrentIndex(combo.count() - 1)

    def __updateUrl(self, combo):
        if not combo.lineEdit().isReadOnly():
            combo.setItemText(combo.currentIndex(), combo.lineEdit().text())

    def __restoreDefaults(self):
        self.comboBoxRecWMS.setCurrentIndex(0)
        self.lineEditRecTitle.setText("NIWA REC v2.0")
