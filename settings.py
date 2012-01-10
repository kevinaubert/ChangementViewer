# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Tue Jan 10 12:19:13 2012
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
        settings.resize(687, 300)
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.ltbFields = QtGui.QListWidget(settings)
        self.ltbFields.setGeometry(QtCore.QRect(130, 30, 256, 192))
        self.ltbFields.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ltbFields.setObjectName(_fromUtf8("ltbFields"))
        self.cmbLayers = QtGui.QComboBox(settings)
        self.cmbLayers.setGeometry(QtCore.QRect(20, 30, 85, 27))
        self.cmbLayers.setObjectName(_fromUtf8("cmbLayers"))
        self.btnApply = QtGui.QPushButton(settings)
        self.btnApply.setGeometry(QtCore.QRect(290, 250, 97, 27))
        self.btnApply.setText(QtGui.QApplication.translate("settings", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.btnApply.setObjectName(_fromUtf8("btnApply"))
        self.btnCancel = QtGui.QPushButton(settings)
        self.btnCancel.setGeometry(QtCore.QRect(180, 250, 97, 27))
        self.btnCancel.setText(QtGui.QApplication.translate("settings", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.ltbSelectedFields = QtGui.QListWidget(settings)
        self.ltbSelectedFields.setGeometry(QtCore.QRect(410, 30, 256, 192))
        self.ltbSelectedFields.setObjectName(_fromUtf8("ltbSelectedFields"))

        self.retranslateUi(settings)
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

