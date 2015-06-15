# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_SetupDialog.ui'
#
# Created: Mon Jun 15 17:37:33 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SetupDialog(object):
    def setupUi(self, SetupDialog):
        SetupDialog.setObjectName(_fromUtf8("SetupDialog"))
        SetupDialog.resize(573, 138)
        self.verticalLayout = QtGui.QVBoxLayout(SetupDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBoxRec = QtGui.QGroupBox(SetupDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxRec.sizePolicy().hasHeightForWidth())
        self.groupBoxRec.setSizePolicy(sizePolicy)
        self.groupBoxRec.setObjectName(_fromUtf8("groupBoxRec"))
        self.gridLayout = QtGui.QGridLayout(self.groupBoxRec)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBoxRecWMS = QtGui.QComboBox(self.groupBoxRec)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxRecWMS.sizePolicy().hasHeightForWidth())
        self.comboBoxRecWMS.setSizePolicy(sizePolicy)
        self.comboBoxRecWMS.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxRecWMS.setEditable(True)
        self.comboBoxRecWMS.setObjectName(_fromUtf8("comboBoxRecWMS"))
        self.comboBoxRecWMS.addItem(_fromUtf8(""))
        self.comboBoxRecWMS.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxRecWMS, 0, 1, 1, 1)
        self.labelRecTitle = QtGui.QLabel(self.groupBoxRec)
        self.labelRecTitle.setObjectName(_fromUtf8("labelRecTitle"))
        self.gridLayout.addWidget(self.labelRecTitle, 1, 0, 1, 1)
        self.toolButtonRecWMSRemove = QtGui.QToolButton(self.groupBoxRec)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/themes/default/mActionRemove.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonRecWMSRemove.setIcon(icon)
        self.toolButtonRecWMSRemove.setObjectName(_fromUtf8("toolButtonRecWMSRemove"))
        self.gridLayout.addWidget(self.toolButtonRecWMSRemove, 0, 2, 1, 1)
        self.labelRecWMS = QtGui.QLabel(self.groupBoxRec)
        self.labelRecWMS.setObjectName(_fromUtf8("labelRecWMS"))
        self.gridLayout.addWidget(self.labelRecWMS, 0, 0, 1, 1)
        self.toolButtonRecWMSAdd = QtGui.QToolButton(self.groupBoxRec)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/themes/default/mActionAdd.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButtonRecWMSAdd.setIcon(icon1)
        self.toolButtonRecWMSAdd.setObjectName(_fromUtf8("toolButtonRecWMSAdd"))
        self.gridLayout.addWidget(self.toolButtonRecWMSAdd, 0, 3, 1, 1)
        self.lineEditRecTitle = QtGui.QLineEdit(self.groupBoxRec)
        self.lineEditRecTitle.setObjectName(_fromUtf8("lineEditRecTitle"))
        self.gridLayout.addWidget(self.lineEditRecTitle, 1, 1, 1, 3)
        self.verticalLayout.addWidget(self.groupBoxRec)
        self.buttonBox = QtGui.QDialogButtonBox(SetupDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SetupDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetupDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetupDialog)

    def retranslateUi(self, SetupDialog):
        SetupDialog.setWindowTitle(_translate("SetupDialog", "REC2 Plugin Setup", None))
        self.groupBoxRec.setTitle(_translate("SetupDialog", "REC River Network", None))
        self.comboBoxRecWMS.setItemText(0, _translate("SetupDialog", "http://gs.niwa.co.nz/geoserver/niwa/wms&layers=rec2_rivers&styles=", None))
        self.comboBoxRecWMS.setItemText(1, _translate("SetupDialog", "http://gis.niwa.co.nz/arcgis/services/HYDRO/REC_rivers/MapServer/WMSServer&layers=REC2_rivers5&layers=REC2_rivers4&layers=REC2_rivers3&layers=REC2_rivers2&layers=REC2_rivers1&styles=&styles=&styles=&styles=&styles=", None))
        self.labelRecTitle.setText(_translate("SetupDialog", "Layer title:", None))
        self.labelRecWMS.setText(_translate("SetupDialog", "WMS URL:", None))
        self.lineEditRecTitle.setText(_translate("SetupDialog", "NIWA REC v2.0", None))

