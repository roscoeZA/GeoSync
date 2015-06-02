from PyQt4 import QtCore
from PyQt4.uic.properties import QtGui
import sys
from PyQt4.Qt import *
import GeoSync
from Ui_GeoSync import _fromUtf8


class CommitDialog(QDialog):
    def __init__(self):
        QWidget.__init__(self)
        self.dlg_layout = QGridLayout(self)
        self.initUI()
        self.name = ''
        self.email = ''
        self.message = ''

    def initUI(self):
        self.lblName = QLabel(self)
        self.lblName.setText('Name: ')
        self.txtName = QLineEdit(self)
        self.txtName.setObjectName(_fromUtf8("txtName"))
        self.txtName.setText("Name")
        self.lblEmail = QLabel(self)
        self.lblEmail.setText('Email: ')
        self.txtEmail = QLineEdit(self)
        self.txtEmail.setObjectName(_fromUtf8("txtEmail"))
        self.txtEmail.setText("Email Address")
        self.lblMessage = QLabel(self)
        self.lblMessage.setText('Message: ')
        self.txtMessage = QLineEdit(self)
        self.txtMessage.setObjectName(_fromUtf8("txtMessage"))
        self.txtMessage.setText("Enter a message")
        # self.btnOk = QPushButton(self)
        # self.btnOk.setText("Ok")
        # self.btnOk.setObjectName(_fromUtf8("btnOK"))
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                           Qt.Horizontal, self)
        self.buttons.accepted.connect(self.get_values)
        self.buttons.rejected.connect(self.close)

        self.dlg_layout.addWidget(self.lblName)
        self.dlg_layout.addWidget(self.txtName)
        self.dlg_layout.addWidget(self.lblEmail)
        self.dlg_layout.addWidget(self.txtEmail)
        self.dlg_layout.addWidget(self.lblMessage)
        self.dlg_layout.addWidget(self.txtMessage)
        self.dlg_layout.addWidget(self.buttons)


    def get_values(self):
        #dialog = CommitDialog()
        # result = dialog.exec_()
        name = self.txtName.text()
        email = self.txtEmail.text()
        message = self.txtMessage.text()
        self.hide()
        return name, email, message

    def reject(self):
        self.hide()



