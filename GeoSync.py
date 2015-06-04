#!/usr/bin/python
# -*- coding: utf-8 -*-
# Import the PyQt and QGIS libraries

"""
/***************************************************************************
Name............ .... : GeoSync Plugin
Description          : Simplifies geogig workflow.
Date                 : 25/May/15 
copyright            : (C) 2015 by Roscoe Lawrence
email                : roscoelawrence@gmail.com 
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

from PyQt4 import QtCore
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, QObject, SIGNAL
from PyQt4.QtGui import QAction, QIcon
from qgis.core import QgsMapLayerRegistry
from Controller import connect2repo
from Controller import export_to_geojson
from Ui_GeoSync import Ui_GeoSync
from SavedRepos import SavedRepos

# Initialize Qt resources from file resources.py

import resources

# Import the code for the dialog

from GeoSyncDialog import GeoSyncDialog


class GeoSync:

    def __init__(self, iface):

    # Save reference to the QGIS interface

        self.iface = iface
    # Added this
        self.dlg = GeoSyncDialog()

    def initGui(self):

    # Create action that will start plugin configuration

        self.action = QAction(QIcon(':/plugins/GeoSync/icon.png'),
                              'GeoSync', self.iface.mainWindow())

    # connect the action to the run method

        QObject.connect(self.action, SIGNAL('activated()'), self.run)

    # Add toolbar button and menu item

        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu('&GeoSync', self.action)

    def unload(self):

    # Remove the plugin menu item and icon

        self.iface.removePluginMenu('&GeoSync', self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work

    def run(self):

    # create and show the dialog

        dlg = GeoSyncDialog()
        saved_repos = SavedRepos().get_fields()
        for index in range(len(saved_repos)):
            dlg.ui.txtCurrentRepo.addItem(saved_repos[index])

    # show the dialog

        dlg.show()
        result = dlg.exec_()

    # See if OK was pressed

        if result == 1:

            pass