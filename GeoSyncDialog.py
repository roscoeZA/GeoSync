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
from PyQt4.QtCore import QRect
from PySide.QtGui import QFileDialog, QDialog, QApplication
from qgis.core import QgsVectorFileWriter
from qgis.core import QgsCoordinateReferenceSystem
import sys
from Ui_GeoSync import Ui_GeoSync
from Controller import *
from CommitDialog import CommitDialog
from RemotesDialog import RemotesDialog
from LogDialog import LogDialog
from RepoDialog import RepoDialog

class GeoSyncDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_GeoSync()
        self.ui.setupUi(self)
        self.ui.btnGetMapLayers.clicked.connect(self.populate_list_widget)
        self.ui.btnLayertoRepo.clicked.connect(self.add_layer_to_repo)
        self.ui.btnLoadfromRepo.clicked.connect(self.populate_map)
        # self.ui.btnDir.clicked.connect(self.set_repo_dir)
        self.ui.btnRemotes.clicked.connect(self.show_remote_dialog)
        self.ui.btnLog.clicked.connect(self.show_log_dialg)
        self.ui.btnConfigRepos.clicked.connect(self.show_repo_dialog)
        self.ui.txtCurrentRepo.currentIndexChanged.connect(self.set_repo_dir)


        # Add progress bar


    def populate_list_widget(self):
        self.ui.listMapLayers.clear()
        self.legend_layers = get_map_layers()
        for layer in self.legend_layers:
            self.ui.listMapLayers.addItem(layer.name())

    def set_repo_dir(self):
        print self.ui.txtCurrentRepo.currentText()
        self.current_repo_dir = self.ui.txtCurrentRepo.currentText()#str(QFileDialog.getExistingDirectory(None, "Select a directory"))
        # self.ui.txtCurrentRepo.setText(self.current_repo_dir)
        self.repos = connect2repo(self.current_repo_dir)

    def populate_map(self):
        self.repos = connect2repo(self.current_repo_dir)
        export_to_geojson(self.repos, self.current_repo_dir)
        all_geojson_to_memory(self.current_repo_dir)
        delete_files(self.current_repo_dir)


    def add_layer_to_repo(self):
        # shift aloat of this functionality into the Controller module.
        self.repos = connect2repo(self.current_repo_dir)
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
        # geogig import has issues with 'crs:OGC:1.3:CRS84' in the geojson file. CRS 3857, seems to work though
            writer = QgsVectorFileWriter.writeAsVectorFormat(self.legend_layers[count],
                                                             os.path.join(self.current_repo_dir,
                                                                          str(fixed_name) + '.geojson'),
                                                             "utf-8",
                                                             crsSrc,
                                                             "GeoJSON")
        import_all_geojosn(self.repos, self.current_repo_dir)
        name, email, message = self.show_commit_dialog()
        add_commit(self.repos, name, email, message)
        # should probably add all files to memory here
        delete_files(self.current_repo_dir)

    def show_commit_dialog(self):
        dlg = CommitDialog()
        dlg.show()
        dlg.exec_()
        name, email, message = dlg.get_values()
        return name, email, message

    def show_remote_dialog(self):
        dlg = RemotesDialog(self.repos)
        dlg.show()
        dlg.exec_()

    def show_log_dialg(self):
        dlg=LogDialog(self.repos)
        dlg.show()
        dlg.exec_()

    def show_repo_dialog(self):
        dlg = RepoDialog()
        dlg.show()
        dlg.exec_()

    def test(self):
        print 'test'