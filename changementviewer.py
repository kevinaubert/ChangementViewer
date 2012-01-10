"""
/***************************************************************************
 ChangementViewer
                                 A QGIS plugin
 Temporal evolution viewer for statistic visualisation
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from PyQt4 import uic	
from PyQt4 import QtGui
import os, sys,re
import pdb
sys.path.append("~/.qgis/python")
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from changementviewerdialog import ChangementViewerDialog
import gettings
class ChangementViewer:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.settingsDialog = None
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/changementviewer/icon.png"), \
            "Changement Viewer", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Changement Viewer", self.action)

        # load the form
        path = os.path.dirname( os.path.abspath( __file__ ) )
        self.dock = uic.loadUi( os.path.join( path, "ui_changementviewer.ui" ) )
        self.iface.addDockWidget( Qt.BottomDockWidgetArea, self.dock )
        QObject.connect(self.dock.btnSettings, SIGNAL('clicked()'),self.showSettingsDialog)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Changement Viewer",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    
    def run(self):
        self.dock = True
        # create and show the dialog
        #ChangementViewerDialog.
        #result = dlg.exec_()
        # See if OK was pressed
        #if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
        #    pass
    
    def updateFields( self ):
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        self.settingsDialog.ltbFields.clear()
        if layName != "Layers":
            vLayer = gettings.getVectorLayerByName( layName )
            lstFields = vLayer.dataProvider().fields()
            for i in lstFields:
              self.settingsDialog.ltbFields.addItem( unicode( lstFields[i].name() ) )
              
    def updateSelectedFields (self ):
        # update selected fields
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        vLayer = gettings.getVectorLayerByName( layName )
        lstFields = vLayer.dataProvider().fields()
        myfields = self.settingsDialog.ltbFields
        self.settingsDialog.ltbSelectedFields.clear()
        for i in range(len(myfields)):  
            if myfields.item(i).isSelected() == True:
                #self.settingsDialog.ltbSelectedFields.addItem(lstFields[i].name())
                self.settingsDialog.ltbSelectedFields.addItem(unicode(re.findall(r'\d+',lstFields[i].name())))
        #range selected fields
        #for i in lstFields:
        #    re.findall(r'\d+',lstFields[i].name())
            
        #pyqtRemoveInputHook()
        #pdb.set_trace()      
        
              
    def ApplyClicked(self):
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        if layName != "Layers":
            vLayer = gettings.getVectorLayerByName( layName )
        else:
            vLayer=self.iface.mapCanvas().currentLayer()
        self.iface.showLayerProperties(vLayer)
              
    def showSettingsDialog(self):
        # load the form
        path = os.path.dirname( os.path.abspath( __file__ ) )
        self.settingsDialog = uic.loadUi(os.path.join(path,"settings.ui"))
        self.settingsDialog.show()
                
        # fill layers combobox
        self.settingsDialog.cmbLayers.clear()
        self.settingsDialog.cmbLayers.addItem( "Layers" )
        lstLayers = gettings.getLayersNames( "vector" )
        self.settingsDialog.cmbLayers.addItems( lstLayers )
        if len(lstLayers) == 0:
            QtGui.QMessageBox.warning(None,'Error','There are no unmanaged vector layers in the project !')
            pass
        # for tracking layers change
        QObject.connect( self.settingsDialog.cmbLayers, SIGNAL( "currentIndexChanged(QString)" ), self.updateFields )
        # for tracking fields selection
        QObject.connect( self.settingsDialog.ltbFields, SIGNAL( 'itemSelectionChanged()' ), self.updateSelectedFields )        
        # load layer properties dialog        
        QObject.connect(self.settingsDialog.btnCancel, SIGNAL('clicked()'),self.settingsDialog.close)
        QObject.connect(self.settingsDialog.btnApply, SIGNAL('clicked()'),self.ApplyClicked)
