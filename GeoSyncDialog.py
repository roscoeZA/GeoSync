"""
/***************************************************************************
Name			 	 : GeoSync Plugin
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
from PyQt4 import QtCore, QtGui
from PySide.QtGui import QFileDialog
from Ui_GeoSync import Ui_GeoSync
from Controller import *

class GeoSyncDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_GeoSync()
        self.ui.setupUi(self)
        self.ui.btnGetMapLayers.clicked.connect(self.populate_list_widget)
        self.ui.btnLayertoRepo.clicked.connect(self.add_layer_to_repo)
        self.ui.btnLoadfromRepo.clicked.connect(self.populate_map)
        self.ui.btnDir.clicked.connect(self.set_repo_dir)

        # Add progress bar


    def populate_list_widget(self):
        layers = get_map_layers()
        for layer in layers:
            self.ui.listMapLayers.addItem(layer)

    def set_repo_dir(self):
        self.current_repo = str(QFileDialog.getExistingDirectory(None, "Select a directory"))
        self.ui.txtCurrentRepo.setText(self.current_repo)
        print file

    def populate_map(self):

        repos = connect2repo(self.current_repo)
        export_to_geojson(repos, self.current_repo)
        all_geojson_to_memory(self.current_repo)

    def add_layer_to_repo(self):
        print 'Save memory, then import, then add and commit'
        selected_layers = self.ui.listMapLayers.selectedItems()
        for layer in selected_layers:
            count = self.ui.listMapLayers.row(layer)
            print "Name: %s Index: %s" % (layer.text(), count)
