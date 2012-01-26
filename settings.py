# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Jan 26 12:11:21 2012
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
        settings.resize(697, 280)
        settings.setWindowTitle(QtGui.QApplication.translate("settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.ltbFields = QtGui.QListWidget(settings)
        self.ltbFields.setGeometry(QtCore.QRect(130, 30, 256, 192))
        self.ltbFields.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.ltbFields.setObjectName(_fromUtf8("ltbFields"))
        self.cmbLayers = QtGui.QComboBox(settings)
        self.cmbLayers.setGeometry(QtCore.QRect(20, 30, 85, 27))
        self.cmbLayers.setObjectName(_fromUtf8("cmbLayers"))
        self.btnApply = QtGui.QPushButton(settings)
        self.btnApply.setGeometry(QtCore.QRect(350, 240, 97, 27))
        self.btnApply.setText(QtGui.QApplication.translate("settings", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.btnApply.setAutoDefault(True)
        self.btnApply.setDefault(False)
        self.btnApply.setObjectName(_fromUtf8("btnApply"))
        self.btnCancel = QtGui.QPushButton(settings)
        self.btnCancel.setGeometry(QtCore.QRect(460, 240, 97, 27))
        self.btnCancel.setText(QtGui.QApplication.translate("settings", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setAutoDefault(False)
        self.btnCancel.setDefault(True)
        self.btnCancel.setFlat(False)
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.tabSelectedFields = QtGui.QTableWidget(settings)
        self.tabSelectedFields.setGeometry(QtCore.QRect(410, 30, 256, 192))
        self.tabSelectedFields.setAcceptDrops(False)
        self.tabSelectedFields.setObjectName(_fromUtf8("tabSelectedFields"))
        self.tabSelectedFields.setColumnCount(2)
        self.tabSelectedFields.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("settings", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSelectedFields.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("settings", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.tabSelectedFields.setHorizontalHeaderItem(1, item)
        self.tabSelectedFields.horizontalHeader().setDefaultSectionSize(128)
        self.tabSelectedFields.horizontalHeader().setStretchLastSection(True)
        self.snbClasses = QtGui.QSpinBox(settings)
        self.snbClasses.setGeometry(QtCore.QRect(30, 130, 59, 27))
        self.snbClasses.setMinimum(1)
        self.snbClasses.setProperty("value", 4)
        self.snbClasses.setObjectName(_fromUtf8("snbClasses"))
        self.cmbMode = QtGui.QComboBox(settings)
        self.cmbMode.setGeometry(QtCore.QRect(20, 70, 85, 27))
        self.cmbMode.setObjectName(_fromUtf8("cmbMode"))
        self.btnOk = QtGui.QPushButton(settings)
        self.btnOk.setGeometry(QtCore.QRect(570, 240, 97, 27))
        self.btnOk.setText(QtGui.QApplication.translate("settings", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setObjectName(_fromUtf8("btnOk"))
        self.ccbAbsolu = QtGui.QCheckBox(settings)
        self.ccbAbsolu.setGeometry(QtCore.QRect(10, 240, 191, 22))
        self.ccbAbsolu.setText(QtGui.QApplication.translate("settings", "Absolute discretization", None, QtGui.QApplication.UnicodeUTF8))
        self.ccbAbsolu.setObjectName(_fromUtf8("ccbAbsolu"))
        self.label = QtGui.QLabel(settings)
        self.label.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.label.setText(QtGui.QApplication.translate("settings", "Classes number", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(settings)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 91, 20))
        self.label_2.setText(QtGui.QApplication.translate("settings", "Play interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.snbPlay = QtGui.QDoubleSpinBox(settings)
        self.snbPlay.setGeometry(QtCore.QRect(30, 190, 62, 27))
        self.snbPlay.setDecimals(1)
        self.snbPlay.setMaximum(1000000000.0)
        self.snbPlay.setProperty("value", 5.0)
        self.snbPlay.setObjectName(_fromUtf8("snbPlay"))

        self.retranslateUi(settings)
        QtCore.QMetaObject.connectSlotsByName(settings)

    def retranslateUi(self, settings):
        self.tabSelectedFields.setSortingEnabled(True)
        item = self.tabSelectedFields.horizontalHeaderItem(0)
        item = self.tabSelectedFields.horizontalHeaderItem(1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    settings = QtGui.QDialog()
    ui = Ui_settings()
    ui.setupUi(settings)
    settings.show()
    sys.exit(app.exec_())

