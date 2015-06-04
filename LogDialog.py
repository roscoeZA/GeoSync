from Ui_GeoSync import _fromUtf8
from PyQt4.Qt import *

class LogDialog(QDialog):
    def __init__(self, _repos):
        QWidget.__init__(self)
        self.dlg_layout = QGridLayout(self)
        self.repos = _repos
        self.initUI()
        self.populate_list()
    def initUI(self):
        self.lstLog=QListWidget(self)
        self.lstLog.setObjectName(_fromUtf8("lstLog"))
        self.dlg_layout.addWidget(self.lstLog)
    def populate_list(self):
        log = self.repos.log()
        message = None
        message = message or "\n".join([commit.message for commit in log[:3]])
        self.lstLog.addItem(message)