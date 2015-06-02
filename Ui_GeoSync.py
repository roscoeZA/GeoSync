# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GeoSync.ui'
#
# Created: Tue Jun  2 23:22:26 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GeoSync(object):
    def setupUi(self, GeoSync):
        GeoSync.setObjectName(_fromUtf8("GeoSync"))
        GeoSync.resize(365, 612)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        GeoSync.setWindowIcon(icon)
        self.btnOK = QtGui.QDialogButtonBox(GeoSync)
        self.btnOK.setGeometry(QtCore.QRect(-10, 560, 341, 32))
        self.btnOK.setOrientation(QtCore.Qt.Horizontal)
        self.btnOK.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnLayertoRepo = QtGui.QPushButton(GeoSync)
        self.btnLayertoRepo.setGeometry(QtCore.QRect(230, 520, 98, 27))
        self.btnLayertoRepo.setObjectName(_fromUtf8("btnLayertoRepo"))
        self.listMapLayers = QtGui.QListWidget(GeoSync)
        self.listMapLayers.setGeometry(QtCore.QRect(20, 130, 321, 291))
        self.listMapLayers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listMapLayers.setObjectName(_fromUtf8("listMapLayers"))
        self.btnGetMapLayers = QtGui.QPushButton(GeoSync)
        self.btnGetMapLayers.setGeometry(QtCore.QRect(20, 490, 311, 27))
        self.btnGetMapLayers.setObjectName(_fromUtf8("btnGetMapLayers"))
        self.btnLoadfromRepo = QtGui.QPushButton(GeoSync)
        self.btnLoadfromRepo.setGeometry(QtCore.QRect(20, 460, 311, 27))
        self.btnLoadfromRepo.setObjectName(_fromUtf8("btnLoadfromRepo"))
        self.btnDir = QtGui.QPushButton(GeoSync)
        self.btnDir.setGeometry(QtCore.QRect(80, 50, 261, 27))
        self.btnDir.setObjectName(_fromUtf8("btnDir"))
        self.txtCurrentRepo = QtGui.QLineEdit(GeoSync)
        self.txtCurrentRepo.setGeometry(QtCore.QRect(100, 20, 241, 27))
        self.txtCurrentRepo.setObjectName(_fromUtf8("txtCurrentRepo"))
        self.lblCurrentRepo = QtGui.QLabel(GeoSync)
        self.lblCurrentRepo.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.lblCurrentRepo.setObjectName(_fromUtf8("lblCurrentRepo"))
        self.lblMapLayers = QtGui.QLabel(GeoSync)
        self.lblMapLayers.setGeometry(QtCore.QRect(20, 110, 241, 17))
        self.lblMapLayers.setObjectName(_fromUtf8("lblMapLayers"))
        self.btnRemotes = QtGui.QPushButton(GeoSync)
        self.btnRemotes.setGeometry(QtCore.QRect(240, 80, 98, 27))
        self.btnRemotes.setObjectName(_fromUtf8("btnRemotes"))
        self.btnLog = QtGui.QPushButton(GeoSync)
        self.btnLog.setGeometry(QtCore.QRect(100, 520, 98, 27))
        self.btnLog.setObjectName(_fromUtf8("btnLog"))

        self.retranslateUi(GeoSync)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL(_fromUtf8("accepted()")), GeoSync.accept)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL(_fromUtf8("rejected()")), GeoSync.reject)
        QtCore.QMetaObject.connectSlotsByName(GeoSync)

    def retranslateUi(self, GeoSync):
        GeoSync.setWindowTitle(_translate("GeoSync", "GeoSync", None))
        self.btnLayertoRepo.setText(_translate("GeoSync", "Save", None))
        self.btnGetMapLayers.setText(_translate("GeoSync", "Get layers from map", None))
        self.btnLoadfromRepo.setText(_translate("GeoSync", "Load layers from repository", None))
        self.btnDir.setText(_translate("GeoSync", "Select repository directory", None))
        self.lblCurrentRepo.setText(_translate("GeoSync", "Repository:", None))
        self.lblMapLayers.setText(_translate("GeoSync", "Layers to add to repository:", None))
        self.btnRemotes.setText(_translate("GeoSync", "Remotes", None))
        self.btnLog.setText(_translate("GeoSync", "Log", None))

