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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "Changement Viewer"
def description():
    return "Temporal evolution viewer for statistical calculations"
def version():
    return "Version 0.1"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load ChangementViewer class from file ChangementViewer
    from changementviewer import ChangementViewer
    return ChangementViewer(iface)
def icon():
    return "icon.png"
