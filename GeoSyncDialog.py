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
from qgis.core import QgsVectorFileWriter
from qgis.core import QgsCoordinateReferenceSystem
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
        self.ui.listMapLayers.clear()
        self.legend_layers = get_map_layers()
        for layer in self.legend_layers:
            self.ui.listMapLayers.addItem(layer.name())

    def set_repo_dir(self):
        self.current_repo_dir = str(QFileDialog.getExistingDirectory(None, "Select a directory"))
        self.ui.txtCurrentRepo.setText(self.current_repo_dir)

    def populate_map(self):
        self.repos = connect2repo(self.current_repo_dir)
        export_to_geojson(self.repos, self.current_repo_dir)
        print self.current_repo_dir
        all_geojson_to_memory(self.current_repo_dir)
        delete_files(self.current_repo_dir)

    def add_layer_to_repo(self):
        # shift aloat of this functionality into the Controller module.
        self.repos = connect2repo(self.current_repo_dir)
        print 'Save memory, then import, then add and commit'
        selected_layers = self.ui.listMapLayers.selectedItems()
        crsSrc = QgsCoordinateReferenceSystem(3857)
        for layer in selected_layers:
            name=list(layer.text())
            fixed_name=""
            for i in range(0, len(name)):
                if name[i] == ' ':
                    fixed_name += "_"
                elif name[i] != " ":
                    fixed_name += name[i]

            count = self.ui.listMapLayers.row(layer)
            print self.legend_layers[count]
        # geogig import has issues with 'crs:OGC:1.3:CRS84' in the geojson file. CRS 3857, seems to work though
            writer = QgsVectorFileWriter.writeAsVectorFormat(self.legend_layers[count],
                                                             os.path.join(self.current_repo_dir,
                                                                          str(fixed_name) + '.geojson'),
                                                             "utf-8",
                                                             crsSrc,
                                                             "GeoJSON")
        import_all_geojosn(self.repos, self.current_repo_dir)
        add_commit(self.repos)
        delete_files(self.current_repo_dir)

