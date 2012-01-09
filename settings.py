# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Mon Jan  9 11:39:20 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_settings(object):
    def setupUi(self, settings):
        settings.setObjectName(_fromUtf8("settings"))
        settings.resize(400, 300)
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(settings)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.ltbFields = QtGui.QListWidget(settings)
        self.ltbFields.setGeometry(QtCore.QRect(130, 30, 256, 192))
        self.ltbFields.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ltbFields.setObjectName(_fromUtf8("ltbFields"))
        self.cmbLayers = QtGui.QComboBox(settings)
        self.cmbLayers.setGeometry(QtCore.QRect(20, 40, 85, 27))
        self.cmbLayers.setObjectName(_fromUtf8("cmbLayers"))

        self.retranslateUi(settings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), settings.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), settings.reject)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    settings = QtGui.QDialog()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())

