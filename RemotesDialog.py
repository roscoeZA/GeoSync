from Ui_GeoSync import _fromUtf8
from PyQt4.Qt import *

class RemotesDialog(QDialog):
    def __init__(self, _repos):
        QWidget.__init__(self)
        self.dlg_layout = QGridLayout(self)
        self.repos = _repos
        self.initUI()
    def initUI(self):
        self.lblRemotes = QLabel(self)
        self.lblRemotes.setText('Remotes:')
        self.lstRemotes = QListWidget(self)
        self.lstRemotes.setObjectName(_fromUtf8('lstRemotes'))
        self.populate_list()
        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok,
                                        Qt.Horizontal, self)
        self.buttons.accepted.connect(self.hide)
        self.dlg_layout.addWidget(self.lblRemotes)
        self.dlg_layout.addWidget(self.lstRemotes)
        self.dlg_layout.addWidget(self.buttons)

    def accept(self):
        print 'accept'

    def populate_list(self):
        for key in self.repos.remotes.keys():
            value = self.repos.remotes[key]
            self.lstRemotes.addItem(key + " (" + value + ")")
        print "Key: %s" % self.repos.remotes.values()
        print "Value: %s" % self.repos.remotes
