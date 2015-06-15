# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_UpstreamDownstreamDialog.ui'
#
# Created: Thu Apr 30 16:47:02 2015
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

class Ui_UpstreamDownstreamDialog(object):
    def setupUi(self, UpstreamDownstreamDialog):
        UpstreamDownstreamDialog.setObjectName(_fromUtf8("UpstreamDownstreamDialog"))
        UpstreamDownstreamDialog.resize(400, 105)
        self.gridLayout = QtGui.QGridLayout(UpstreamDownstreamDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonSearchUpstream = QtGui.QPushButton(UpstreamDownstreamDialog)
        self.pushButtonSearchUpstream.setEnabled(False)
        self.pushButtonSearchUpstream.setObjectName(_fromUtf8("pushButtonSearchUpstream"))
        self.horizontalLayout.addWidget(self.pushButtonSearchUpstream)
        self.pushButtonSearchDownstream = QtGui.QPushButton(UpstreamDownstreamDialog)
        self.pushButtonSearchDownstream.setEnabled(False)
        self.pushButtonSearchDownstream.setObjectName(_fromUtf8("pushButtonSearchDownstream"))
        self.horizontalLayout.addWidget(self.pushButtonSearchDownstream)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.lineEditPosition = QtGui.QLineEdit(UpstreamDownstreamDialog)
        self.lineEditPosition.setObjectName(_fromUtf8("lineEditPosition"))
        self.gridLayout.addWidget(self.lineEditPosition, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(UpstreamDownstreamDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 3)
        self.labelPosition = QtGui.QLabel(UpstreamDownstreamDialog)
        self.labelPosition.setObjectName(_fromUtf8("labelPosition"))
        self.gridLayout.addWidget(self.labelPosition, 0, 0, 1, 1)
        self.toolButtonSelectPosition = QtGui.QToolButton(UpstreamDownstreamDialog)
        self.toolButtonSelectPosition.setText(_fromUtf8(""))
        self.toolButtonSelectPosition.setObjectName(_fromUtf8("toolButtonSelectPosition"))
        self.gridLayout.addWidget(self.toolButtonSelectPosition, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)

        self.retranslateUi(UpstreamDownstreamDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), UpstreamDownstreamDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), UpstreamDownstreamDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UpstreamDownstreamDialog)

    def retranslateUi(self, UpstreamDownstreamDialog):
        UpstreamDownstreamDialog.setWindowTitle(_translate("UpstreamDownstreamDialog", "Upstream/Downstream Search", None))
        self.pushButtonSearchUpstream.setText(_translate("UpstreamDownstreamDialog", "Search Upstream", None))
        self.pushButtonSearchDownstream.setText(_translate("UpstreamDownstreamDialog", "Search Downstream", None))
        self.labelPosition.setText(_translate("UpstreamDownstreamDialog", "Position:", None))
        self.toolButtonSelectPosition.setToolTip(_translate("UpstreamDownstreamDialog", "Select reach", None))

