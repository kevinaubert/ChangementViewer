# -*- coding: latin1 -*-
"""
/***************************************************************************
 ChangementViewer
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from PyQt4 import uic	
from PyQt4 import QtGui
import os, sys,re
import pdb
import time
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
        self.tmpRenderer = None
        self.timer = QTimer()
        
    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/changementviewer/icon.png"), \
            "Changement Viewer", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("Changement Viewer", self.action)

        # load the forms and connect actions
        path = os.path.dirname( os.path.abspath( __file__ ) )
        self.dock = uic.loadUi( os.path.join( path, "ui_changementviewer.ui" ) )
        self.iface.addDockWidget( Qt.BottomDockWidgetArea, self.dock )
        path = os.path.dirname( os.path.abspath( __file__ ) )
        self.settingsDialog = uic.loadUi(os.path.join(path,"settings.ui"))
        QObject.connect(self.dock.btnSettings, SIGNAL('clicked()'),self.showSettingsDialog)
        QObject.connect(self.dock.timeSlide,SIGNAL('valueChanged(int)'),self.selectedField)
        self.settingsDialog.cmbLayers.addItem( "Layers" )
        lstLayers = gettings.getLayersNames( "vector" )
        self.settingsDialog.cmbLayers.addItems( lstLayers )
        QObject.connect(self.dock.pushButtonBack,SIGNAL('clicked()'),self.stepBackward)
        QObject.connect(self.dock.pushButtonForward,SIGNAL('clicked()'),self.stepForward)
        QObject.connect(self.dock.pushButtonPlay,SIGNAL('clicked()'),self.stepPlay) 
        QObject.connect(self.dock.pushButtonStop,SIGNAL('clicked()'),self.stepStop) 
        QObject.connect(self.dock.btnQ,SIGNAL('clicked()'),self.refresh) 

    def refresh(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Changement Viewer",self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.removeDockWidget(self.dock)
        self.initGui()

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Changement Viewer",self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.removeDockWidget(self.dock)

    def run(self):
        self.dock.show()
        
    def showSettingsDialog(self):
        # fill layers combobox
        #self.settingsDialog.cmbLayers.clear()
        #self.settingsDialog.cmbLayers.addItem( "Layers" )
        lstLayers = gettings.getLayersNames( "vector" )
        #self.settingsDialog.cmbLayers.addItems( lstLayers )
        if len(lstLayers) == 0:
            QtGui.QMessageBox.warning(None,'Error','There are no unmanaged vector layers in the project !')
            pass
        else:
            # show the form
            self.settingsDialog.show()
            #connect
            QObject.connect( self.settingsDialog.cmbLayers, SIGNAL( "currentIndexChanged(QString)" ), self.updateFields ) #for tracking layers change      
            QObject.connect( self.settingsDialog.ltbFields, SIGNAL( 'itemSelectionChanged()' ), self.updateSelectedFields ) # for tracking fields selection              
            QObject.connect(self.settingsDialog.btnCancel, SIGNAL('clicked()'),self.settingsDialog.close) # close the settings dialog
            QObject.connect(self.settingsDialog.btnOk, SIGNAL('clicked()'),self.settingsDialog.hide) # close the settings dialog
            QObject.connect(self.settingsDialog.btnOk, SIGNAL('clicked()'),self.selectedField) # load the layer properties dialog
            QObject.connect(self.settingsDialog.btnApply, SIGNAL('clicked()'),self.selectedField) # load the layer properties dialog

        
    def updateFields( self ):
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        self.settingsDialog.ltbFields.clear()
        if layName != "Layers":
            self.showModelist()
            vLayer = gettings.getVectorLayerByName( layName )
            # Modif RC ici
            lstFields = vLayer.pendingFields()
            #proFields = vLayer.dataProvider().fields()
            for i in lstFields:
              self.settingsDialog.ltbFields.addItem( unicode( lstFields[i].name() ) )
        #Joined fields control for absolute discretization
        if len(lstFields.items()) > vLayer.dataProvider().fieldCount():
            self.settingsDialog.ccbAbsolu.setVisible(0)
            self.settingsDialog.ccbAbsolu.setChecked(0)
        else:
            self.settingsDialog.ccbAbsolu.setVisible(1)
            self.settingsDialog.ccbAbsolu.setChecked(0)
              
    def updateSelectedFields (self ):
        # update selected fields
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        vLayer = gettings.getVectorLayerByName( layName )
        
        lstFields = vLayer.pendingFields()
        #lstIndex = dict([(field.name(), index) for index, field in lstFields.iteritems()])
        #lstFields = vLayer.dataProvider().fields()
        myfields = self.settingsDialog.ltbFields     
        self.settingsDialog.tabSelectedFields.clear()
        self.settingsDialog.tabSelectedFields.setRowCount(0)
        for i in range(len(myfields)):  
        #for i in range(len(lstIndex)): 
            if myfields.item(i).isSelected() == True:
                date=re.findall(r'\d+',lstFields[i].name())
                if len(date)!=1:
                    QtGui.QMessageBox.warning(None,'Error','Warning : there is no date information for this attribute !')                
                for u in range(len(date)):
                        layerName=lstFields[i].name()
                        sdate=date[u]
                        self.addRowToOptionsTable(layerName,sdate)
        self.settingsDialog.tabSelectedFields.sortItems(1,order = Qt.AscendingOrder)
        n=self.settingsDialog.tabSelectedFields.rowCount()
        self.dock.timeSlide.setMinimum(0)
        self.dock.timeSlide.setMaximum(n-1)

        # Selected fields table headers
        item1 = QtGui.QTableWidgetItem()
        item1.setText(QtGui.QApplication.translate("settings", "Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsDialog.tabSelectedFields.setHorizontalHeaderItem(0, item1)
        item2 = QtGui.QTableWidgetItem()
        item2.setText(QtGui.QApplication.translate("settings", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.settingsDialog.tabSelectedFields.setHorizontalHeaderItem(1, item2)
       
    def addRowToOptionsTable(self,layerName,sdate):
        #insert selected fields in tabSelectedFields
        
        # insert row
        row=self.settingsDialog.tabSelectedFields.rowCount()
        self.settingsDialog.tabSelectedFields.insertRow(row)
        
        # insert values
        layerItem = QTableWidgetItem()
        layerItem.setText(layerName)
        self.settingsDialog.tabSelectedFields.setItem(row,0,layerItem)

        dateItem = QTableWidgetItem()
        dateItem.setText(sdate)
        self.settingsDialog.tabSelectedFields.setItem(row,1,dateItem)
        
    def showModelist(self):
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        vLayer=gettings.getVectorLayerByName(layName)
        self.settingsDialog.cmbMode.clear()
        self.settingsDialog.cmbMode.addItem( "Mode" )
        if vLayer.isUsingRendererV2():
            # new symbology - subclass of QgsFeatureRendererV2 class
            lstModes = ["EqualInterval", "Quantiles", "Jenks", "StdDev" ,"Pretty"]

        else:
            # old symbology - subclass of QgsRenderer class
            lstModes = ["EqualInterval", "Quantiles", "Empty"] 
        #fill the mode combobox    
        self.settingsDialog.cmbMode.addItems( lstModes )
       
    def selectedField(self):
        layName = unicode( self.settingsDialog.cmbLayers.currentText() )
        if layName != "Layers":
            vLayer = gettings.getVectorLayerByName( layName )
        else:
            vLayer=self.iface.mapCanvas().currentLayer()
        u=self.dock.timeSlide.value()
        fieldName=self.settingsDialog.tabSelectedFields.item(u,0)
        date=self.settingsDialog.tabSelectedFields.item(u,1)
        if self.settingsDialog.tabSelectedFields.rowCount()!=0:
            self.dock.labelDate.setText(date.text())
            if self.settingsDialog.ccbAbsolu.isChecked():
                # absolu discretization
                self.absolu(vLayer,fieldName.text())
            else:
                #relative discretization
                self.ApplyClicked(vLayer,fieldName.text())
        self.dock.timeSlide.setPageStep(1)

    def totalLayer(self,vLayer):
        vLayer.updateFieldMap()
        # Create temp layer with an attribute that will contain all the selected fields values
        geometryTypes = ['POINT', 'LINESTRING', 'POLYGON']
        tmpLayer = QgsVectorLayer(geometryTypes[vLayer.geometryType()], "tmpLayer", "memory")
        tmpProvider = tmpLayer.dataProvider()
        tmpProvider.addAttributes([QgsField("myvalues", QVariant.Double)])
        tmpLayer.commitChanges()
        # We access to features with the dataProviders, for reading (in vLayer) and writing (in tmpLayer)
        vProvider = vLayer.dataProvider()
        #lstFields = vLayer.pendingAllAttributesList()
        allAttrs = vProvider.attributeIndexes()
        vProvider.select(allAttrs)
        # We select all the attributes, and will access the ones with need later
        # Loop from 0 to the count of selected Fields
        for i in range(self.settingsDialog.tabSelectedFields.rowCount()):
            tmpLayer.startEditing()
            fldName = self.settingsDialog.tabSelectedFields.item(i,0)
            fldIndex = vLayer.fieldNameIndex(fldName.text())
            # fldIndex is the number of the field we want to access
            feat = QgsFeature()
            # Creation of a new feature
            #joinInfo=vLayer.joinForFieldIndex([int(fldIndex)].toDouble()[0],vProvider.maximumIndex(),int(0))
            while vProvider.nextFeature(feat):
                #tmpLayer.addJoinedFeatureAttributes(feat, joinInfo, fldName.text(), QVariant(feat.attributeMap()[int(fldIndex)].toDouble()[0]), lstFields, int(0) )  
                newfeat = QgsFeature()
                # We give this feature the same geometry as in the origin layer
                newfeat.setGeometry(feat.geometry())      
                # Adding the value of the selected fieldindex/feature inside the newfeature                          
                newfeat.addAttribute(int(0), QVariant(feat.attributeMap()[int(fldIndex)].toDouble()[0]))     
                tmpProvider.addFeatures( [newfeat] )
                tmpLayer.commitChanges()
        tmpLayer.updateExtents() 
        
        numberOfClasses =self.settingsDialog.snbClasses.value()
        mode=(self.settingsDialog.cmbMode.currentIndex()-1)
        sym = QgsSymbolV2.defaultSymbol(vLayer.geometryType())
        ramp=QgsVectorGradientColorRampV2(QColor(0,255,0),QColor(255,0,0))
        self.tmpRenderer = QgsGraduatedSymbolRendererV2().createRenderer ( tmpLayer, "myvalues", numberOfClasses, mode, sym, ramp )
        
    def absolu(self,vLayer,fieldName):
        #if self.tmpRenderer == None:
        self.totalLayer(vLayer)
        modeName = unicode( self.settingsDialog.cmbMode.currentText() )
        if modeName != "Mode":
            absoluteRenderer = QgsGraduatedSymbolRendererV2(fieldName, self.tmpRenderer.ranges())
            absoluteRenderer.setRotationField(fieldName)
            vLayer.setRendererV2( absoluteRenderer )
            self.iface.mapCanvas().refresh()
            self.iface.legendInterface().refreshLayerSymbology(vLayer)
        else:
            QtGui.QMessageBox.warning(None,'Error','You have to choose a discretization mode')
        
              
    def ApplyClicked(self,vLayer,fieldName):
        # Set the numeric field and the number of classes to be generated
        numberOfClasses =self.settingsDialog.snbClasses.value()
        # Get the field index based on the field name
        fieldIndex = vLayer.fieldNameIndex(fieldName)
        # Set the discretization mode
        modeName = unicode( self.settingsDialog.cmbMode.currentText() )
        if modeName != "Mode":
            mode=(self.settingsDialog.cmbMode.currentIndex()-1)
            if self.iface.mapCanvas().currentLayer().isUsingRendererV2():
            # new symbology - subclass of QgsFeatureRendererV2 class
                sym = QgsSymbolV2.defaultSymbol(vLayer.geometryType())
                ramp=QgsVectorGradientColorRampV2(QColor(0,255,0),QColor(255,0,0))
                rendererV2 = QgsGraduatedSymbolRendererV2.createRenderer ( vLayer, fieldName, numberOfClasses, mode, sym, ramp )
                rendererV2.setRotationField(fieldName)        
                vLayer.setRendererV2( rendererV2 )
            else:
                # old symbology - subclass of QgsRenderer class
                # Create the renderer object to be associated to the layer later
                renderer = QgsGraduatedSymbolRenderer( vLayer.geometryType() )        
                # Here you may choose the renderer mode from EqualInterval/Quantile/Empty
                renderer.setMode( mode )     
                # Define classes (lower and upper value as well as a label for each class)
                provider = vLayer.dataProvider()
                minimum = provider.minimumValue( fieldIndex ).toDouble()[ 0 ]
                maximum = provider.maximumValue( fieldIndex ).toDouble()[ 0 ]        
                for i in range( numberOfClasses ):
                    # Switch if attribute is int or double
                    lower = ('%.*f' % (2, minimum + ( maximum - minimum ) / numberOfClasses * i ) )
                    upper = ('%.*f' % (2, minimum + ( maximum - minimum ) / numberOfClasses * ( i + 1 ) ) )
                    label = "%s - %s" % (lower, upper)
                    color = QColor(255*i/numberOfClasses, 255-255*i/numberOfClasses, 0)
                    sym = QgsSymbol( vLayer.geometryType(), lower, upper, label, color )
                    renderer.addSymbol( sym )       
                # Set the field index to classify and set the created renderer object to the layer
                renderer.setClassificationField( fieldIndex )        
                vLayer.setRenderer( renderer )
                #self.iface.showLayerProperties(vLayer)
            self.iface.mapCanvas().refresh()
            self.iface.legendInterface().refreshLayerSymbology(vLayer)
        else:
            QtGui.QMessageBox.warning(None,'Error','You have to choose a discretization mode')
            
    def stepForward(self):
        u=self.dock.timeSlide.value()
        self.dock.timeSlide.setValue(u+1)
        n=self.settingsDialog.tabSelectedFields.rowCount()
        umax=n-1
        if u == umax:
            self.timer.stop()
            self.dock.timeSlide.setValue(0)
            
    def stepBackward(self):
        u=self.dock.timeSlide.value()
        self.dock.timeSlide.setValue(u-1)
        
    def stepPlay(self):
        self.timer.stop()
        self.timer.timeout.connect(self.stepForward)
        self.timer.start(self.settingsDialog.snbPlay.value()*1000)

    def stepStop(self):
        self.timer.stop()
