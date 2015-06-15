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
from ui_AboutDialog import Ui_AboutDialog


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, pluginDir, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        result = self.metadata(pluginDir)

        self.setWindowTitle(self.tr("About %s %s") % (result["name"], result["version"]))
        self.lblVersion.setText(self.tr("Version: %s") % result["version"])
        self.tabWidget.setTabText(0, result["name"])
        self.tabWidget.setTabText(1, self.tr("Author"))
        self.tabWidget.setTabText(2, self.tr("Contact"))
        self.tabWidget.setTabText(3, self.tr("Change Log"))

        aboutString = result["description"]

        contribString = "<p><center><b>%s</b></center></p>" % self.tr("Author(s):")
        contribString += "<p>%s</p>" % result["author"]

        licenseString = self.tr("Sourcepole AG - Linux & Open Source Solutions") + "\n"
        licenseString += self.tr("Weberstrasse 5, 8004 Zürich, Switzerland") + "\n"
        licenseString += "\n"
        licenseString += self.tr("Contact:") + "\n"
        licenseString += result["author"] + "\n"
        licenseString += result["email"] + "\n"
        licenseString += result["homepage"] + "\n"
        licenseString += result["tracker"] + "\n"
        licenseString += result["repository"] + "\n"

        self.memAbout.setText(aboutString)
        self.memContrib.setText(contribString)
        self.memAcknowl.setText(licenseString)
        self.memChangeLog.setText(result["changelog"])

    def metadata(self, pluginDir):
        mdFile = QFile(pluginDir + "/metadata.txt")
        mdFile.open(QIODevice.ReadOnly | QIODevice.Text)
        inFile = QTextStream(mdFile)

        changeLog = ""
        result = {
            "version": "",
            "description": "",
            "name": "",
            "qgisMinimumVersion": "",
            "qgisMaximumVersion": "",
            "author": "",
            "email": "",
            "homepage": "",
            "tracker": "",
            "repository": "",
            "changelog": ""
        }

        while not inFile.atEnd():
            line = inFile.readLine()
            lineArr = line.split("=")

            if lineArr[0] == "changelog":
                line = inFile.readLine()
                while len(line.split("=")) == 1:
                    if line[0:1] != "#":
                        result["changelog"] += line + "\n"
                    line = inFile.readLine()
            elif lineArr[0] in result:
                result[lineArr[0]] = lineArr[1]

        return result
