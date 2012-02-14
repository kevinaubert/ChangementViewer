"""
/***************************************************************************
 ChangementViewerDialog
                                 A QGIS plugin
 Temporal evolution viewer for statistical calculations
                             -------------------
        begin                : 2012-01-06
        copyright            : (C) 2012 by Kevin Aubert
        email                : kevin.aubert@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.core import *
from qgis.gui import * 
from PyQt4 import QtCore, QtGui
from ui_changementviewer import Ui_ChangementViewer
from settings import Ui_settings
# create the dialog for zoom to point
class ChangementViewerDialog(QtGui.QDialog, Ui_ChangementViewer):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_ChangementViewer()
        self.ui.setupUi(self)

