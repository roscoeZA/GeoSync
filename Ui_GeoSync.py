# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GeoSync.ui'
#
# Created: Sat May 30 18:12:28 2015
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
        GeoSync.resize(559, 507)
        self.btnOK = QtGui.QDialogButtonBox(GeoSync)
        self.btnOK.setGeometry(QtCore.QRect(210, 460, 341, 32))
        self.btnOK.setOrientation(QtCore.Qt.Horizontal)
        self.btnOK.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnLoadfromRepo = QtGui.QPushButton(GeoSync)
        self.btnLoadfromRepo.setGeometry(QtCore.QRect(20, 340, 131, 27))
        self.btnLoadfromRepo.setObjectName(_fromUtf8("btnLoadfromRepo"))
        self.btnLayertoRepo = QtGui.QPushButton(GeoSync)
        self.btnLayertoRepo.setGeometry(QtCore.QRect(190, 370, 98, 27))
        self.btnLayertoRepo.setObjectName(_fromUtf8("btnLayertoRepo"))
        self.listMapLayers = QtGui.QListWidget(GeoSync)
        self.listMapLayers.setGeometry(QtCore.QRect(20, 30, 321, 291))
        self.listMapLayers.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listMapLayers.setObjectName(_fromUtf8("listMapLayers"))
        self.btnGetMapLayers = QtGui.QPushButton(GeoSync)
        self.btnGetMapLayers.setGeometry(QtCore.QRect(150, 340, 141, 27))
        self.btnGetMapLayers.setObjectName(_fromUtf8("btnGetMapLayers"))

        self.retranslateUi(GeoSync)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL(_fromUtf8("accepted()")), GeoSync.accept)
        QtCore.QObject.connect(self.btnOK, QtCore.SIGNAL(_fromUtf8("rejected()")), GeoSync.reject)
        QtCore.QMetaObject.connectSlotsByName(GeoSync)

    def retranslateUi(self, GeoSync):
        GeoSync.setWindowTitle(_translate("GeoSync", "GeoSync", None))
        self.btnLoadfromRepo.setText(_translate("GeoSync", "Load repo layers", None))
        self.btnLayertoRepo.setText(_translate("GeoSync", "Save", None))
        self.btnGetMapLayers.setText(_translate("GeoSync", "List Map Layers", None))

