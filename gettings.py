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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import * 

# return list of names of all layers (vector, raster or both types) in QgsMapLayerRegistry 
def getLayersNames( layerType ):
	layermap = QgsMapLayerRegistry.instance().mapLayers()
	layerlist = []
	if layerType == "all":
		for name, layer in layermap.iteritems():
			layerlist.append( unicode( layer.name() ) )
	elif layerType == "vector":
		for name, layer in layermap.iteritems():
			if layer.type() == QgsMapLayer.VectorLayer:
				layerlist.append( unicode( layer.name() ) )
	else:
		for name, layer in layermap.iteritems():
			if layer.type() == QgsMapLayer.RasterLayer:
				layerlist.append( unicode( layer.name() ) )
	return layerlist
 
 # return list of names of all fields from input QgsVectorLayer
def getFieldNames( vlayer ):
	fieldmap = getFieldList( vlayer )
	fieldlist = []
	for name, field in fieldmap.iteritems():
		if not field.name() in fieldlist:
			fieldlist.append( unicode( field.name() ) )
	return fieldlist

# return QgsVectorLayer from a layer name (as string)
def getVectorLayerByName( myName ):
	layermap = QgsMapLayerRegistry.instance().mapLayers()
	for name, layer in layermap.iteritems():
		if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
			if layer.isValid():
				return layer
			else:
				return None

# return the field list of a vector layer
def getFieldList( vlayer ):
          myFields= vlayer.createJoinCaches()
          myFields= vlayer.updateFieldMap()
          return myFields
 
